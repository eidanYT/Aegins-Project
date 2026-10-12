# Borrador SRR — Cámara de impresión y gestión de emisiones

**Estado: TBR — propuesta pendiente de revisión técnica.**  
Fecha: 12 de octubre de 2026. Origen: propuesta de Eidan y observación del jurado sobre emisiones que podrían afectar a la tripulación. No hay ensayos de contención ni una interfaz de gases aprobada.

## Texto para el informe

FORGE-UG propone alojar la impresora 3D en una cámara dedicada para estudiar la contención del material, los residuos y las emisiones potenciales durante la impresión. Esta propuesta responde a la observación del jurado sobre el posible efecto de gases y partículas en la tripulación. La gestión de gases se definirá junto con el material y la plataforma: se evaluarán retención y tratamiento dentro del payload, o una transferencia controlada a una interfaz aceptada por el alojamiento. La existencia de una cámara o de una salida no demuestra por sí sola protección de la tripulación. Antes de cerrar el diseño se identificarán los contaminantes, se dimensionará su gestión y se definirán criterios de aceptación y verificaciones. Estos puntos siguen abiertos para revisión por los módulos afectados.

## Escenarios y demostración

Se mantienen dos alternativas: payload para estación espacial y payload autónomo para satélite. **No se ha elegido una plataforma de referencia ni demostrado compatibilidad con ambas.** En estación se analiza explícitamente la posible exposición de la tripulación; en satélite, la contaminación y efectos sobre el propio vehículo. No se supone conexión disponible al soporte vital ni al exterior.

La pieza propuesta por Eidan se registra en [misión](../../system/mision.md#pieza-de-demostración-propuesta-por-eidan). Su geometría aún requiere precisar la base común y la trayectoria; no sustituye los parámetros del caso didáctico.

## Concepto de contención e interfaz pendiente

- Cámara de proceso con cierre, pasamuros y acceso cuya contención se evaluará. Materiales, presión, temperatura y límites de fuga: TBD.
- Inventario de resina y otros materiales, fichas de seguridad y emisiones en operación y fallo: TBD. Gases, vapores, aerosoles y partículas requieren evaluación según el inventario; no se declara que todos se produzcan.
- Ruta de gestión de emisiones: TBD. Las alternativas conceptuales son retención/tratamiento interno o transferencia controlada a una interfaz del host. La eficacia y capacidad del tratamiento necesitan justificación para cada contaminante.
- La descarga directa al volumen habitable no se adopta como solución. Una descarga al exterior tampoco se considera disponible ni aceptada sin evaluación del host.
- Acceso y apertura, pérdida de energía, salida obstruida, fuga y fallo de monitorización necesitan una secuencia coordinada de parada y contención, con límites y tiempos todavía por definir.
- Cámara, conductos, tratamiento, instrumentación y retención añaden masa, volumen, potencia, calor y coste que deberá integrar M4.

Los acuerdos compartidos se desarrollarán en [ICD-005](../../interfaces/ICD-005.md); las conexiones y recursos del host, en [ICD-004](../../interfaces/ICD-004.md). Este borrador no los aprueba.

## Verificación propuesta y decisiones abiertas

| Qué demostrar | Trabajo previsto | Criterio pendiente | Revisión propuesta |
|---|---|---|---|
| Emisiones identificadas | Inventario, fuentes del material y caracterización futura del proceso | Sustancias, cantidades y condiciones relevantes | M2 con M3/M4 |
| Contención adecuada | Análisis de vías de fuga y ensayos futuros de cierre/pasamuros | Límites de fuga y exposición definidos con el host | M4 y sistemas |
| Gestión de gases suficiente | Balance de generación/acumulación y capacidad del tratamiento; ensayo futuro | Concentraciones, capacidad, duración y condiciones de aceptación | M2/M4 y host |
| Respuesta ante fallos | Análisis de escenarios y demostración futura de secuencias | Detección, tiempos, estado seguro y apertura autorizada | M5 con M1/M2/M3/M4 |
| Compatibilidad del conjunto | Presupuestos y evaluación de contaminación, presión y calor | Asignaciones e interfaz aceptadas por el host | M4 y sistemas |

Para el SRR se puede presentar el concepto, los peligros y el plan de verificación. **La protección de tripulación y la aptitud de vuelo no están verificadas.** No se fijan límites numéricos sin material, ambiente y fuente aplicables.

Próximo avance: M2 propone material e inventario; M4 compara rutas de gestión y cámara; M3 aporta condiciones UV/térmicas; M5 propone detección y secuencias. Sistemas debe coordinar la elección de plataforma. Responsables definitivos de sistemas y M3, fechas y conformidades siguen por asignar.

## Fuentes y alcance

- Propuesta de Eidan en la conversación de trabajo del 12 de octubre de 2026: cámara de impresión, salida de gases aún sin definir y dos plataformas alternativas.
- Evaluación de AEGINS de la primera revisión, consultada en Drive: observaciones sobre seguridad de emisiones y complejidad del brazo. Este documento aborda contención; la justificación del brazo sigue pendiente.
- NASA, [Toxic Offgassing](https://www.nasa.gov/centers-and-facilities/white-sands/toxic-offgassing/): referencia sobre identificación y cuantificación de emisiones de materiales en ambientes habitables cerrados.
- NASA, [Natural and Induced Environments](https://www.nasa.gov/reference/6-0-natural-and-induced-environments-vol-2/): referencia sobre contaminación ambiental y protección de tripulación.

Las referencias NASA orientan la investigación. Su aplicabilidad contractual y los requisitos específicos se determinarán al elegir el host; citar estas fuentes no acredita cumplimiento.
