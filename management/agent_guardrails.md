# Reglas persistentes y controles de agentes

## Estado de implantación
Esta propuesta añade reglas, comprobaciones y registros de tarea. Se activan para todos los agentes al integrar esta propuesta en main y reanudar las tareas desde esa versión. **La protección de ramas no está activada por esta propuesta.** La conexión GitHub rechazó la lectura administrativa de protección; no se puede afirmar cómo está configurada actualmente.

## Trabajo de los agentes
Usar las ramas tecnico/, integracion/ (también docs/srr- para la propuesta existente) o gobernanza/. La política limita los archivos de cada perfil. El registro de tarea tiene nombre derivado de la rama: tecnico/m1-m3 usa management/agent_runs/tecnico_m1-m3.json. Leer la plantilla, sustituir su contenido y mantenerla al retomar/cambiar de fase. No escribir prompts largos en el registro: objetivo, resultados comprobados, pendientes con dueño/fecha, fuentes, siguiente acción, revisores y estimaciones.

El comprobador rechaza cambios fuera de perfil, registros incompletos, enlaces locales nuevos rotos y evidencias declaradas verificadas sin método/archivo. Protege el caso didáctico de modificaciones de estos perfiles. No comprueba que una fuente sea fiable, una aprobación auténtica o una cifra científicamente correcta; eso se revisa técnicamente.

Los registros no son cerrojos ni asignan permisos reales: dos sesiones que usan una misma identidad pueden seleccionar otra rama. El reparto necesita supervisión y revisión.

## Activación en GitHub después de revisión independiente
1. Revisar e integrar la propuesta de gobernanza; los usuarios reales verificados con escritura son eidanYT y nicomanuQP.
2. Ejecutar la comprobación Aegins agent policy / agent-policy y comprobar su resultado. La primera ejecución es un bootstrap sin una política previa en main; requiere revisión humana del código y del workflow.
3. En Settings → Branches, proteger main: exigir PR, al menos una aprobación independiente, revisión de CODEOWNERS, descartar aprobaciones tras cambios, resolver conversaciones y exigir la comprobación agent-policy con la rama actualizada.
4. Aplicar restricciones también a administradores/bypass; prohibir force-push y borrado. Mantener credenciales de los agentes sin administración ni capacidad de cambiar estas reglas.
5. Si ambos agentes usan eidanYT, nicomanuQP puede revisar sus PR con otra identidad. GitHub no distingue al dueño humano de un agente que usa sus credenciales. No dar a los agentes acceso a la identidad del revisor.
6. Revisar y actualizar el PR SRR existente y el prompt del agente técnico con el nuevo prefijo de rama y un registro. Un prompt creado antes de esta política no implica que ya la esté usando.
7. Comprobar que un PR fuera de ámbito falla y que GitHub bloquea la integración. Hasta completar esos pasos no describir los controles como obligatorios.

CODEOWNERS requiere conformidad de un propietario de la línea cuando se configura la protección; no exige aprobación de todos los módulos. Los acuerdos de interfaces siguen teniendo su revisión técnica documentada.

## Confianza del workflow
El workflow usa pull_request, permiso de lectura y una acción fijada a un commit. Tras el bootstrap, lee validador y política desde el commit base y analiza blobs del PR como datos, sin ejecutar su código. Cambios de workflow/validador/política se reservan a gobernanza y requieren revisión humana. La comprobación puede ejecutarse localmente con Python estándar; no instala paquetes.

## Recuperar contexto
Al reanudar: leer AGENTS.md vigente, registro de la rama y archivos modificados; comparar el PR y el estado actual; actualizar completed/pending/next_action. Una lista de tareas no demuestra que se hicieron.

## Fuentes
[Instrucciones persistentes de Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [protección de ramas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) y [seguridad de Actions](https://docs.github.com/en/actions/reference/security/secure-use).
