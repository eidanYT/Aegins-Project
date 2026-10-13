# Plan M5 — Metrología de aristas y caras cerradas

**TBR.** La finalidad es distinguir cambio real de geometría de incertidumbre de medida. Criterios de aceptación, espesor, material y hardware: TBD.

## Magnitudes y registro

La geometría nominal se define en [SRR-GEO-001](../../system/caso_srr.json). M1 debe asociar caras/aristas con trayectoria y marco de mecanismo. Registrar la transformación con referencias externas estables; ajustar libremente la pieza contra el nominal puede ocultar desplazamientos o deformaciones que interesan al experimento.

Para aristas: posición de centro de cordón por segmento y continuidad según criterio acordado. Para caras: distancia normal de la superficie exterior reconstruida a la superficie nominal, regiones visibles y cobertura; definir estadísticos antes de comparar. El espesor y el interior requieren un método adicional o comprobación en etapas previas al cierre, no se deducen de la vista exterior.

No reemplazar zonas ocultas por puntos inventados. Reportar cobertura, datos inválidos y regiones excluidas junto con resultados.

## Alternativas de adquisición

| Opción | Qué puede aportar | Limitación |
|---|---|---|
| Vistas simultáneas calibradas | Correspondencias para reconstrucción tridimensional del exterior | Sombras, transparencia/brillo, textura, baseline y ventana de cámara pueden impedir correspondencias |
| Vistas sucesivas de pieza estable | Inspección después del proceso con menos cámaras simultáneas | Necesita poses conocidas/estabilidad; no resuelve por sí sola observación dinámica ni el interior |
| Inspección por etapas antes de cerrar | Evidencia de cara interior, uniones y espesor si existe un método apropiado | Requiere coordinación con M1/M2/M3 y método de espesor todavía por elegir |

Propuesta inicial: estudiar vistas simultáneas para comparación exterior y complementarlas con inspección por etapas. Es una arquitectura, no una elección de cámaras.

OpenCV documenta calibración de cámaras y triangulación a partir de observaciones correspondientes [S2]. Su residuo de reproyección no equivale a incertidumbre completa del material. La viabilidad depende del montaje, óptica, textura, calibración y condiciones.

## Calibración y verificación futura

Definir patrón con dimensiones y trazabilidad conocidas, montaje, volumen/poses de calibración, enfoque, iluminación y ventanas. Incluir el efecto de observación a través de una ventana según la configuración real. Reservar un patrón/medida independiente para comprobar el resultado, en varias posiciones/orientaciones.

Distinguir sesgo, repetibilidad, estabilidad temporal y cobertura. No validar con el mismo dato que se usó para ajustar el modelo. La cámara debe comprobarse en las condiciones de adquisición aplicables; las pruebas terrestres no demuestran automáticamente operación en vuelo.

## Presupuesto de incertidumbre

NIST TN1297 distingue contribuciones de incertidumbre estándar y contempla covarianzas; las correcciones sistemáticas y su incertidumbre también importan [S1]. Para contribuciones no correlacionadas ya propagadas a la salida en m: u_c=√Σu_i². Si hay correlaciones, usar el modelo completo; no aplicar RSS indiscriminadamente.

| Contribución | Evaluación requerida | Estado |
|---|---|---|
| Patrón y escala | Certificado/dimensión conocida, calibración y condiciones | TBD |
| Calibración/distorsión/ventana | Sensibilidad y comprobación independiente en el volumen | TBD |
| Correspondencia/segmentación | Variabilidad con material, iluminación y zonas visibles | TBD |
| Pose y registro | Estabilidad y transformación externa a la pieza | TBD |
| Sincronización/movimiento | Banda, exposición e incertidumbre temporal | TBD |
| Reconstrucción | Sensibilidad de triangulación y distancia/profundidad | TBD |

No hay valores para sumar todavía. Un presupuesto vacío no se representa como incertidumbre cero. El código rechaza una lista de contribuciones vacía.

La incertidumbre expandida U=k·u_c necesita factor y fundamento para su cobertura; no afirmar automáticamente 95 % con k=2 [S3]. El objetivo de 0,10 mm que aparece en el ejercicio histórico sigue siendo didáctico, no requisito seleccionado.

## Ejemplo conservado y límites

El ejercicio histórico usa ancho ideal de 0,1 m y 1920 píxeles: escala nominal 5,2083×10⁻⁵ m/píxel. La conversión se comprueba independientemente en mm, pero no demuestra exactitud, profundidad o capacidad de medir espesor.

La [evidencia de cálculos](../../evidence/srr_integracion_calculos.md) documenta hipótesis y resultados. La demostración de curado, resistencia, cierre o seguridad exige evidencias específicas que estas imágenes/cálculos no proporcionan.

## Fuentes
- S1: [NIST TN1297 — incertidumbre combinada](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty).
- S2: [OpenCV 4.13.0 — calibración y reconstrucción](https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html).
- S3: [NIST TN1297 — reporte](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty).

Consultadas el 12 de octubre de 2026 (Lima). Fuentes metodológicas; no contienen datos de desempeño de FORGE-UG.
