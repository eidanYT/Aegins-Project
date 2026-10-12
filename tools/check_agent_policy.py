"""Validate agent scope and task/evidence records; never execute PR contents."""
import argparse
import json
import posixpath
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

HEX = re.compile(r"[0-9a-f]{40}")
BRANCH = re.compile(r"[A-Za-z0-9._/-]+")
STATES = {"borrador", "en_revision", "listo_revision", "bloqueado"}
DATA_STATES = {"EJEMPLO", "TBD", "TBR", "APROBADO", "VERIFICADO"}
POLICY = "management/agent_policy.json"
SCRIPT = "tools/check_agent_policy.py"
LINK = re.compile(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)")

def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], stderr=subprocess.PIPE)

def read(repo, ref, path):
    data = git(repo, "show", ref + ":" + path)
    if len(data) > 1_000_000:
        raise ValueError("Archivo demasiado grande para esta comprobación: " + path)
    return data.decode("utf-8")

def tree(repo, ref):
    result = {}
    for record in git(repo, "ls-tree", "-rz", ref).split(b"\0"):
        if record:
            meta, path = record.split(b"\t", 1)
            result[path.decode("utf-8")] = meta.split()[0].decode()
    return result

def nonempty(value):
    return isinstance(value, str) and bool(value.strip())

def path_allowed(path, allowed):
    return any(path.startswith(p) if p.endswith("/") else path == p for p in allowed)

def profile_for(branch, policy):
    matches = [name for name, value in policy["profiles"].items()
               if any(branch.startswith(p) for p in value["prefixes"])]
    return matches[0] if len(matches) == 1 else None

def record_path(branch):
    return "management/agent_runs/" + branch.replace("/", "_") + ".json"

def validate_record(record, profile, paths):
    errors = []
    if not isinstance(record, dict):
        return ["Registro de tarea debe ser un objeto JSON."]
    if record.get("version") != 1 or record.get("profile") != profile:
        errors.append("Versión/perfil del registro no coincide con la rama.")
    for key in ("objective", "next_action"):
        if not nonempty(record.get(key)):
            errors.append("Falta " + key + " en registro.")
    if record.get("status") not in STATES:
        errors.append("Estado de ejecución inválido.")
    for key in ("completed", "sources", "reviewers"):
        values = record.get(key)
        if not isinstance(values, list) or not values or not all(nonempty(x) for x in values):
            errors.append("Lista " + key + " debe contener texto no vacío.")
    pending = record.get("pending")
    if not isinstance(pending, list):
        errors.append("pending debe ser una lista.")
    else:
        for item in pending:
            if not isinstance(item, dict) or not all(nonempty(item.get(k)) for k in ("item", "owner", "due")):
                errors.append("Cada pendiente necesita item, owner y due.")
    estimates = record.get("estimates")
    if not isinstance(estimates, list):
        errors.append("estimates debe ser una lista.")
    else:
        for item in estimates:
            if not isinstance(item, dict) or not all(nonempty(item.get(k)) for k in ("name", "unit", "source")) or "value" not in item or item.get("status") not in DATA_STATES:
                errors.append("Estimación sin valor, unidad, fuente o estado.")
            elif item["status"] == "VERIFICADO":
                errors.append("Datos VERIFICADO deben ir en verified_claims, con evidencia.")
    claims = record.get("verified_claims")
    if not isinstance(claims, list):
        errors.append("verified_claims debe ser una lista.")
    else:
        for item in claims:
            if not isinstance(item, dict) or not all(nonempty(item.get(k)) for k in ("claim", "method", "scope", "evidence")):
                errors.append("Afirmación verificada sin método, alcance o evidencia.")
            elif item["method"] not in {"A", "T", "I", "D"} or not item["evidence"].startswith("evidence/") or item["evidence"] not in paths:
                errors.append("Método o archivo de evidencia inválido.")
    return errors

def broken_links(path, content, paths):
    errors = []
    for match in LINK.finditer(content):
        target = match.group(1).strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        target_path = unquote(parsed.path)
        destination = posixpath.normpath(posixpath.join(posixpath.dirname(path), target_path))
        if destination.startswith("../") or destination.startswith("/") or destination not in paths:
            errors.append("Enlace local inválido en " + path + ": " + target)
    return errors

def validate(repo, base, head, branch):
    if not HEX.fullmatch(base) or not HEX.fullmatch(head) or not BRANCH.fullmatch(branch):
        return ["Referencias o rama inválidas."]
    if ".." in branch.split("/") or any(not p for p in branch.split("/")):
        return ["Rama inválida."]
    base_paths, paths = tree(repo, base), tree(repo, head)
    bootstrap = POLICY not in base_paths or SCRIPT not in base_paths
    trusted = head if bootstrap else base
    policy = json.loads(read(repo, trusted, POLICY))
    if policy.get("version") != 1:
        return ["Versión de política inválida."]
    profile = profile_for(branch, policy)
    if profile is None:
        return ["Rama sin perfil permitido."]
    if bootstrap and profile != "gobernanza":
        return ["El bootstrap solo admite una rama de gobernanza."]
    changed = [p.decode("utf-8") for p in git(repo, "diff", "--name-only", "--no-renames", "-z", base + "..." + head).split(b"\0") if p]
    checkpoint = record_path(branch)
    allowed = policy["profiles"][profile]["allowed"]
    errors = []
    for path in changed:
        if path != checkpoint and not path_allowed(path, allowed):
            errors.append("Fuera de ámbito " + profile + ": " + path)
        if path in paths and paths[path] not in {"100644", "100755"}:
            errors.append("No se admiten symlinks/submódulos nuevos: " + path)
    if checkpoint not in changed or checkpoint not in paths:
        errors.append("Falta actualizar el registro " + checkpoint)
    else:
        try:
            errors.extend(validate_record(json.loads(read(repo, head, checkpoint)), profile, paths))
        except (ValueError, subprocess.CalledProcessError):
            errors.append("Registro JSON inválido.")
    # Check changed links and regressions caused by deleting their targets.
    deleted = set(base_paths) - set(paths)
    for path in paths:
        if path.endswith(".md") and (path in changed or deleted):
            try:
                new = broken_links(path, read(repo, head, path), paths)
                old = set(broken_links(path, read(repo, base, path), base_paths)) if path in base_paths else set()
                errors.extend(error for error in new if error not in old)
            except (ValueError, subprocess.CalledProcessError):
                errors.append("No se puede leer Markdown: " + path)
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--branch", required=True)
    args = parser.parse_args()
    try:
        errors = validate(Path(args.repo), args.base, args.head, args.branch)
    except (ValueError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print("ERROR: no se pudo comprobar la política (" + type(exc).__name__ + ").")
        return 1
    for error in errors:
        # Avoid treating untrusted filenames as workflow commands.
        print("ERROR: " + error.replace("\n", " ").replace("\r", " "))
    print("Política rechazada." if errors else "Política comprobada; la revisión científica/humana sigue siendo necesaria.")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
