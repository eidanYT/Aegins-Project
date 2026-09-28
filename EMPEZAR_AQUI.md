# Preparar el repositorio y al equipo

## 1. Lo que necesitas
- Cuenta individual de GitHub y nombre de usuario de cada integrante.
- GitHub Desktop en Windows; editor de texto como VS Code. Para documentos pequeños basta el navegador.
- CAD que el equipo ya maneje; acordar versión y formato neutral de intercambio.
- Una persona responsable de cada paquete y una coordinación de sistemas con tiempo asignado.
- Carpeta compartida de Drive para CAD pesado, videos y originales; GitHub conserva el índice de versiones.
- Agenda y rúbrica del programa, MDR, evaluación del jurado y referencias técnicas.
- Una primera reunión de 60–75 minutos.
No hace falta comprar hardware ni licencias de simulación para empezar.

## 2. Crear el repositorio en GitHub
Ruta recomendada para iniciar hoy: repositorio privado bajo tu cuenta; una organización AEGINS puede evaluarse después.
1. Inicia sesión en [GitHub](https://github.com/).
2. Pulsa + → New repository.
3. Owner: tu cuenta. Repository name: forge-ug.
4. Description: “AEGINS — FORGE-UG: requisitos, interfaces, modelos y diseño conceptual de un payload de fabricación en microgravedad”.
5. Visibility: Private, como opción inicial propuesta para el trabajo interno.
6. Activa Add a README file; deja la licencia sin seleccionar hasta que el equipo acuerde cómo compartir su trabajo.
7. Create repository.

## 3. Cargar el kit con GitHub Desktop
1. Instala [GitHub Desktop](https://desktop.github.com/) e inicia sesión.
2. File → Clone repository → selecciona forge-ug → Clone.
3. Descarga y extrae este ZIP en otra carpeta.
4. Copia TODO el contenido de forge-ug-starter dentro de la carpeta clonada; incluye .github, .gitignore y .gitattributes.
5. Reemplaza solo el README inicial que acabas de crear. No copies la carpeta externa: README.md debe quedar directamente en la raíz.
6. En Desktop revisa Changes; escribe “Añade estructura inicial SRR” y pulsa Commit to main.
7. Pulsa Push origin. Abre GitHub y comprueba que README e instrucciones se muestran.
Este primer commit inicializa la estructura. Después trabajen por ramas y pull requests.

Alternativa para cambios pequeños: GitHub → archivo → editar → proponer cambio en una rama.
Para cargar todo el kit se recomienda Desktop: mantiene carpetas y archivos de configuración.
No subir únicamente el ZIP al repositorio; su contenido debe quedar accesible para revisión.

## 4. Invitar a tus compañeros
En el repositorio: Settings → Collaborators → Add people. Busca sus usuarios exactos y envía las invitaciones; cada persona debe aceptarla.
Después cada miembro clona el mismo repositorio. Para esta colaboración interna no necesita un fork.
En un repositorio personal los colaboradores tienen capacidad de escritura amplia: asignarles una carpeta no restringe sus permisos a esa carpeta.
Si más adelante necesitan roles administrativos compartidos o permisos más finos, evalúen una organización.

## 5. Preparar el tablero y los hitos
Crea un Project desde tu perfil → Projects → New project → Board. Nombre sugerido: FORGE-UG SRR.
Configura Status: Pendiente, En curso, En revisión, Bloqueado, Terminado.
Añade campos Paquete, Prioridad y Fecha objetivo. Assignees identifica al responsable.
Añade las Issues del repositorio al Project; el tablero no se rellena por copiar estos archivos.

En Issues → Milestones crea:
- SRR entrega: 10/10/2026, fecha DERIVADA pendiente de confirmar.
- SRR revisión: 17/10/2026, usando provisionalmente 2026.
- PDR entrega: 28/11/2026, también derivada.
Usen el hito de entrega para las tareas que deben estar en la documentación.
La agenda tiene título 2026 y filas 2027: la tarea B01 incluye confirmar el año.

Etiquetas sugeridas: M1, M2, M3, M4, M5, sistema, interfaz, requisito, riesgo, evidencia.
Una tarea bloqueada debe indicar qué decisión o entrega falta y quién la resolverá.

## 6. Acordar revisiones
Regla de trabajo: ningún cambio técnico importante se integra sin revisión de otra persona.
Cambios de interfaz: conformidad explícita de ambos paquetes y coordinación de sistemas.
El autor puede registrar la conformidad de su propio paquete en la descripción; otro responsable revisa el lado receptor. Si una persona cubre ambos, incluir un revisor independiente.

Si el plan contratado lo permite, en Settings → Branches o Rules configura main para exigir pull request y aprobación.
GitHub Free permite colaboración privada, pero determinadas protecciones y CODEOWNERS en repositorios privados requieren otro plan. No hace falta contratarlo para comenzar: documenten y apliquen revisión manual.
El archivo CODEOWNERS.example es opcional e inactivo. Sustituye los nombres de ejemplo, comprueba acceso de escritura y renómbralo solo si van a usar la función.
Varios propietarios en una misma línea de CODEOWNERS NO garantizan la aprobación de todos; la revisión de ambos lados de una interfaz sigue siendo una regla explícita.

## 7. Primera reunión: agenda de 75 minutos
- 0–10: objetivo científico y alcance CAD/análisis del concurso.
- 10–25: elegir escenario de referencia o asignar decisión con plazo de 48 horas.
- 25–35: nombrar responsables y suplentes; completar management/equipo.md.
- 35–50: revisar caso demostrativo y primer conjunto de requisitos.
- 50–65: repartir tareas B01–B09 y revisar dependencias.
- 65–75: cada persona practica una rama, un commit y un pull request pequeño.

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
