# Datos y decisiones pendientes

Este registro reúne preguntas técnicas abiertas. Las fechas del proyecto están únicamente en [el plan de hitos](../management/plan.md); puedes trabajar en cualquiera de estos puntos desde ahora.

| ID | Qué falta | Dónde documentar la respuesta | Seguimiento |
|---|---|---|---|
| T01 | Formatos leídos: informe máximo 30 páginas y exposición 10 min + 15 min preguntas; falta agenda/prórroga confirmada | [Plan](../management/plan.md) y [paquete SRR](../reviews/SRR/README.md) | Issue por crear o enlazar |
| T02 | Escenario elegido: estación tripulada con cámara; falta host, alojamiento, ambiente e interfaces | [Misión](mision.md) | Issue por crear o enlazar |
| T03 | Base cuadrada, aristas de 0,05 m y caras cerradas elegidas; falta espesor, anclaje, trayectoria y métricas/criterios | [M1](../modules/movimiento_NICOMANUQP/propuesta.md), [M5](../modules/control_metrologia_Eidan/propuesta.md) y misión | Issue por crear o enlazar |
| T04 | Resina y óptica preliminares | [M2](../modules/extrusion_Gabriel/propuesta.md), [M3](../modules/uv_termica/propuesta.md) e [ICD-001](../interfaces/ICD-001.md) | Issue por crear o enlazar |
| T05 | Alimentación y sincronización | [ICD-001](../interfaces/ICD-001.md) e [ICD-003](../interfaces/ICD-003.md) | Issue por crear o enlazar |
| T06 | Recursos de plataforma y cargas | [Presupuestos](presupuestos.md), [ICD-002](../interfaces/ICD-002.md) e [ICD-004](../interfaces/ICD-004.md) | Issue por crear o enlazar |
| T07 | Metrología y muestreo | [M5](../modules/control_metrologia_Eidan/propuesta.md) e ICD-003 | Issue por crear o enlazar |
| T08 | Contención, térmica y fallos | [Riesgos](riesgos.md) e [ICD-005](../interfaces/ICD-005.md) | Issue por crear o enlazar |

Al abrir la Issue, enlázala aquí e identifica quién resolverá la pregunta. No marques un punto cerrado sin respuesta documentada.

## Responsables y siguiente decisión

| Punto | Responsable de trabajo propuesto | Fecha | Estado |
|---|---|---|---|
| Host/ambiente/interfaces | Sistemas con Shelton y Eidan | Por acordar | TBD |
| Trayectorias de caras y volumen barrido | NICOMANUQP / otro agente técnico | Por acordar | TBD |
| Material/espesor/emisiones | Gabriel / otro agente técnico | Por acordar | TBD |
| UV, curado, sombras y calor | M3 / otro agente técnico; responsable humano por asignar | Por acordar | TBD |
| Metrología y tiempo | Eidan / M5 con M1/M3/M4 | Por acordar | Propuesta TBR publicada para revisión |
| Cámara y acceso | Shelton / M4 con M2/M3/M5/host | Por acordar | Propuesta TBR publicada para revisión |

Las decisiones de Eidan están en [SRR-GEO-001](caso_srr.json) y misión. Estas asignaciones no son aceptación de tareas ni conformidades; las fechas deben acordarse. El trabajo de propuestas puede continuar mientras se resuelven los datos faltantes.

Seguimiento M4/T02/T06/T08: [cámara, emisiones y alojamiento](https://github.com/eidanYT/Aegins-Project/issues/3). Seguimiento M5/T03/T05/T07/T08: [metrología, tiempo y fallos](https://github.com/eidanYT/Aegins-Project/issues/4). Los aportes M1/M2/M3 se coordinan mediante sus propuestas y estas dependencias; el material/UV de T04 todavía debe documentarse.
