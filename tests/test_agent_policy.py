import copy
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("policy", ROOT / "tools/check_agent_policy.py")
policy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy)

def run_record():
    return {"version": 1, "profile": "tecnico", "objective": "Proponer material",
            "status": "borrador", "completed": ["Fuentes consultadas"], "sources": ["Ficha de material v1"],
            "reviewers": ["Revisor independiente"], "pending": [{"item": "Curado", "owner": "M3", "due": "Por acordar"}],
            "next_action": "Comparar UV", "estimates": [], "verified_claims": []}

class PolicyTests(unittest.TestCase):
    def test_record_accepts_explicit_pending_work(self):
        self.assertEqual(policy.validate_record(run_record(), "tecnico", {}), [])

    def test_record_rejects_missing_context(self):
        r = run_record()
        del r["next_action"]
        self.assertTrue(policy.validate_record(r, "tecnico", {}))

    def test_record_rejects_unowned_pending(self):
        r = run_record()
        r["pending"] = [{"item": "Datos"}]
        self.assertTrue(policy.validate_record(r, "tecnico", {}))

    def test_estimate_requires_units_and_source(self):
        r = run_record()
        r["estimates"] = [{"name": "Masa", "value": 1, "status": "TBR"}]
        self.assertTrue(policy.validate_record(r, "tecnico", {}))

    def test_verified_claim_requires_real_evidence_path(self):
        r = run_record()
        r["verified_claims"] = [{"claim": "Fugas", "method": "T", "scope": "Cámara", "evidence": "evidence/ausente.md"}]
        self.assertTrue(policy.validate_record(r, "tecnico", {}))
        self.assertEqual(policy.validate_record(r, "tecnico", {"evidence/ausente.md": "100644"}), [])

    def test_scope_does_not_accept_prefix_collision(self):
        self.assertFalse(policy.path_allowed("modules/m1-other/a.md", ["modules/m1/"]))
        self.assertFalse(policy.path_allowed("system/mision.md", ["reviews/SRR/"]))

    def test_encoded_link_cannot_escape_repository(self):
        self.assertTrue(policy.broken_links("README.md", "[x](%2e%2e/private.md)", {"private.md": "100644"}))

    def test_links_accept_relative_paths_and_external_urls(self):
        self.assertEqual(policy.broken_links("a/readme.md", "[b](../b.md#anchor) [web](https://example.org)", {"b.md": "100644"}), [])

class GitIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="aegins-policy-test-")
        self.repo = Path(self.tmp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Policy Test")
        self.git("config", "user.email", "policy-test@example.invalid")
        self.write("management/agent_policy.json", (ROOT / "management/agent_policy.json").read_text(encoding="utf-8"))
        self.write("tools/check_agent_policy.py", "# trusted validator")
        self.write("README.md", "[material](modules/extrusion_Gabriel/source.md)\n")
        self.write("modules/extrusion_Gabriel/source.md", "Fuente\n")
        self.base = self.commit()

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args], stderr=subprocess.PIPE).decode().strip()

    def write(self, path, content):
        target = self.repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        return self.git("rev-parse", "HEAD")

    def checkpoint(self):
        self.write(policy.record_path("tecnico/prueba"), json.dumps(run_record()))

    def test_technical_change_passes(self):
        self.write("modules/extrusion_Gabriel/propuesta.md", "[fuente](source.md)\n")
        self.checkpoint()
        self.assertEqual(policy.validate(self.repo, self.base, self.commit(), "tecnico/prueba"), [])

    def test_technical_change_to_shared_file_fails(self):
        self.write("system/requisitos.md", "Cambio fuera de ámbito\n")
        self.checkpoint()
        self.assertTrue(any("Fuera de ámbito" in e for e in policy.validate(self.repo, self.base, self.commit(), "tecnico/prueba")))

    def test_head_cannot_relax_base_policy(self):
        p = json.loads((self.repo / "management/agent_policy.json").read_text())
        p["profiles"]["tecnico"]["allowed"].append("system/")
        self.write("management/agent_policy.json", json.dumps(p))
        self.write("system/requisitos.md", "Intento de ampliar permisos\n")
        self.checkpoint()
        self.assertTrue(any("Fuera de ámbito" in e for e in policy.validate(self.repo, self.base, self.commit(), "tecnico/prueba")))

    def test_missing_checkpoint_fails(self):
        self.write("modules/extrusion_Gabriel/propuesta.md", "Trabajo\n")
        self.assertTrue(any("registro" in e for e in policy.validate(self.repo, self.base, self.commit(), "tecnico/prueba")))

    def test_new_broken_link_fails(self):
        self.write("modules/extrusion_Gabriel/propuesta.md", "[inexistente](missing.md)\n")
        self.checkpoint()
        self.assertTrue(any("Enlace" in e for e in policy.validate(self.repo, self.base, self.commit(), "tecnico/prueba")))

    def test_deletion_of_link_target_fails(self):
        (self.repo / "modules/extrusion_Gabriel/source.md").unlink()
        self.checkpoint()
        self.assertTrue(any("Enlace" in e for e in policy.validate(self.repo, self.base, self.commit(), "tecnico/prueba")))

if __name__ == "__main__":
    unittest.main()
