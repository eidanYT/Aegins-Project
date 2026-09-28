# Registro de CAD y archivos grandes
Para empezar: carpeta compartida de Drive con versiones explícitas y exportación STEP/PDF o imágenes revisables.
GitHub contiene este índice. La referencia debe apuntar a una versión congelada, no a un “último archivo” que cambie silenciosamente.

| ID | Pieza/ensamble | Responsable/editor actual | Revisión | Nativo/versión CAD | Exportación | Enlace | Hash o identificación de versión | Interfaces |
|---|---|---|---|---|---|---|---|---|
| CAD-001 | Envolvente común | TBD | TBD | TBD | TBD | TBD | TBD | ICD-002/004 |

Antes de modificar CAD avisar en la Issue y reservar edición de la pieza.
No renombrar versiones como final_final2; usar revisión y registro.
Para integrar CAD directamente en Git se puede evaluar Git LFS con todo el equipo; requiere configuración y revisar cuotas.
GitHub bloquea archivos Git ordinarios mayores de 100 MiB; carga por navegador limitada a 25 MiB por archivo [G7].
