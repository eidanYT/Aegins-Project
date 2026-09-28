# Preparar el repositorio y al equipo (Si fue hecho por chatgpt)

## 6.  revisiones
Regla de trabajo: ningún cambio técnico importante se integra sin revisión de otra persona.
Cambios de interfaz: conformidad explícita de ambos paquetes y coordinación de sistemas.
El autor puede registrar la conformidad de su propio paquete en la descripción; otro responsable revisa el lado receptor. Si una persona cubre ambos, incluir un revisor independiente.

Si el plan contratado lo permite, en Settings → Branches o Rules configura main para exigir pull request y aprobación.
GitHub Free permite colaboración privada, pero determinadas protecciones y CODEOWNERS en repositorios privados requieren otro plan. No hace falta contratarlo para comenzar: documenten y apliquen revisión manual.
El archivo CODEOWNERS.example es opcional e inactivo. Sustituye los nombres de ejemplo, comprueba acceso de escritura y renómbralo solo si van a usar la función.
Varios propietarios en una misma línea de CODEOWNERS NO garantizan la aprobación de todos; la revisión de ambos lados de una interfaz sigue siendo una regla explícita.

## 7. Primera reunión (No completado)
-  objetivo científico y alcance CAD/análisis del concurso.
-  elegir escenario de referencia o asignar decisión con plazo de 48 horas.
-  nombrar responsables y suplentes; completar management/equipo.md.
-  revisar caso demostrativo y primer conjunto de requisitos.
-  repartir tareas B01–B09 y revisar dependencias.
-  cada persona practica una rama, un commit y un pull request pequeño.

Resultado: cada miembro sabe qué entregará, a quién le sirve y qué evidencia permite aceptarlo.
La reunión no termina con “investigar el brazo”, sino con una entrega delimitada y una fecha.

## 8. Documentos que deben completar primero
1. system/mision.md: escenario, objetivo, probeta y límites.
2. management/equipo.md: personas reales.
3. system/requisitos.md: valores TBR revisados y TBD asignados.
4. interfaces/README.md e ICD-001.md: contratos entre paquetes.
5. Una ficha de candidato por opción crítica, con templates/componente.md.
6. system/presupuestos.md: recursos y costes con incertidumbre.
7. system/riesgos.md: peligros y pruebas que faltan.
8. management/plan.md: convertir el trabajo inicial en Issues.

## 9. Qué significa estar listo para trabajar
- Todos pueden acceder al repositorio y al Project.
- Los cinco paquetes tienen responsable.
- Hay un escenario elegido o una decisión acotada con fecha de cierre.
- Existe una probeta común y métricas definidas.
- Cada integrante tiene una primera Issue con criterio de aceptación.
- El equipo ha integrado un cambio pequeño mediante pull request.
- Los TBD críticos tienen propietario y fecha.
- Hay una revisión de integración reservada para el 3 de octubre.

## 10. Glosario para el primer día
Repositorio: carpeta del proyecto con historial.
Clone: copia local conectada al repositorio.
Branch/rama: espacio de trabajo para un cambio.
Commit: versión local guardada con explicación.
Push: subir tus commits.
Pull: traer cambios del servidor.
Issue: tarea, problema o decisión pendiente.
Pull request/PR: propuesta de integrar cambios.
Review: revisión técnica.
Merge: incorporar la propuesta.
Main: versión compartida aceptada.
Tag: marca de una versión concreta, por ejemplo srr-v0.1.
ICD: documento que define una interfaz.
ConOps: secuencia de operación del sistema.
Trazabilidad: relación entre necesidad, requisito, diseño y evidencia.

Pasos verificados contra documentación oficial; enlaces en references/fuentes.md.
