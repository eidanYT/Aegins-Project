# FORGE-UG — AEGINS
Kit inicial para organizar el SRR. Preparado el 27/09/2026, hora de Lima.

**Estado: propuesta editable.** No contiene una selección definitiva de hardware ni evidencia de vuelo.
El programa plantea un payload para satélite o estación; no fija ocupación humana, presión ni alojamiento.
La decisión de plataforma está ABIERTA: no asumir cabina tripulada ni vacío a partir del nombre del vehículo.

Empieza por [EMPEZAR_AQUI.md](EMPEZAR_AQUI.md).
Después abre [misión](system/mision.md), [requisitos](system/requisitos.md) e [interfaces](interfaces/README.md).

Para ver un caso completado paso a paso: [ejemplo de trazabilidad](system/ejemplo_trazabilidad.md).

## Cinco paquetes
| ID | Paquete | Carpeta |
|---|---|---|
| M1 | Movimiento | [modules/movimiento](modules/movimiento/README.md) |
| M2 | Material y extrusión | [modules/extrusion](modules/extrusion/README.md) |
| M3 | UV y térmica | [modules/uv_termica](modules/uv_termica/README.md) |
| M4 | Recinto e integración | [modules/integracion](modules/integracion/README.md) |
| M5 | Control y metrología | [modules/control_metrologia](modules/control_metrologia/README.md) |

[Plan y tareas](management/plan.md) · [Responsables](management/equipo.md) · [Cómo colaborar](CONTRIBUTING.md) · [Fuentes](references/fuentes.md)

## Regla central
Necesidad → requisito → candidato → interfaz → verificación → evidencia.
Cada dato debe indicar unidad, procedencia, condiciones y estado.
**TBD:** por determinar. **TBR:** valor propuesto pendiente de revisión.
Una simulación puede verificar el modelo; no demuestra automáticamente el comportamiento físico.

Las carpetas no son repositorios separados ni submódulos Git.
GitHub Projects, Issues, permisos, hitos y reglas se configuran en GitHub: copiar este kit no los crea.
