# Cómo trabajamos (Si lo hizo chat gpt xd)
## Un ciclo completo
1. una Issue; un responsable y una entrega de 1–3 días como máximo orientativo.
2. En Desktop selecciona main → Fetch origin → Pull origin si hay cambios.
3. Crea una rama desde main: por ejemplo m2/caudal-caso-demo.
4. Edita los archivos de tu tarea. Incluye unidades, fuentes, supuestos y resultado.
5. Commit con un mensaje concreto; Publish branch o Push origin.
6. Create pull request hacia main. Enlaza la Issue; “Closes #N” si la resuelve al integrarse.
7. Pide revisión al paquete afectado. Contesta observaciones y sube correcciones.
8. Cuando cumple aceptación, merge; actualiza el tablero y luego main en tu equipo.

Ejemplo: una persona propone más velocidad. El PR actualiza parámetro compartido, modelo, ICD y evidencia; M2 revisa caudal/transitorios y M3 revisa exposición. Hasta acordarlo, main conserva el valor anterior.

## Terminado significa
- Requisito y tarea enlazados.
- Fuente/versiones y unidades presentes.
- Resultado reproducible o procedimiento claramente descrito.
- Supuestos e incertidumbres visibles.
- Interfaces impactadas actualizadas y conformidad registrada.
- Evidencia enlazada y revisada.
Un PDF extenso o un cálculo generado por IA sin fuentes no basta.

## Concurrencia
Una rama por tarea, no una rama permanente por persona.
Para editar simultáneamente el mismo documento, dividir por secciones/archivos y acordar quién integra.
CAD binario: un editor por pieza/ensamble a la vez; registrar la reserva en la Issue.
Quien cambia un parámetro compartido debe buscar sus dependencias y revisar los resultados afectados.
Los resultados antiguos se conservan con su versión; no se presentan como vigentes.

## Datos y versiones
Internamente usar SI. Mostrar mm, mL/min o mW/cm² solo con conversión explícita.
Un parámetro tiene una fuente de verdad. El ejemplo vive en config/caso_demo.json.
Status: EJEMPLO, TBD, TBR, APROBADO o VERIFICADO; APROBADO no significa validado físicamente.
Un resultado de simulación se etiqueta como análisis, nunca como ensayo real.

Para fuentes guardar enlaces, DOI y ficha resumida. Las versiones CAD externas se registran en cad/registro.md.
La entrega se identifica con un tag y una lista de documentos en reviews/SRR/README.md.
El documento original de Claude es una referencia de análisis, no una autoridad que aprueba requisitos.
