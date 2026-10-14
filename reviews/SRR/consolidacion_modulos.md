# Consolidación documental de los cinco módulos

**TBR — propuestas, sin conformidades ni ensayos.** Integra la entrega técnica publicada en [SRR: propuestas M1–M3 con cálculos preliminares y límites](https://github.com/eidanYT/Aegins-Project/pull/6) y la primera entrega M4/M5. El PR técnico se revisó e incorporó a main el 13 de octubre; integración actualizada sin conflictos. No se selecciona material/hardware. Ver [revisión conjunta y pendientes](revision_conjunta_2026-10-13.md).

La referencia común de Eidan está formalizada en D-001 y [SRR-GEO-001](../../system/caso_srr.json): estación espacial con tripulación, cámara y bipirámide cuadrada de aristas de 0,05 m con caras cerradas. Las hipótesis del análisis técnico no sustituyen esta decisión ni el caso didáctico.

## Propuestas disponibles y dependencias

| Módulo | Entrega disponible | Pendiente que impide cerrar el diseño |
|---|---|---|
| M1 movimiento | Brazo ideal orientable, comparación cartesiana y muestreo de poses; sexto giro condicionado a herramienta/tubos | Continuidad, cuerpos/colisiones, márgenes articulares, anclaje, actuadores y cargas reales |
| M2 extrusión | Alternativas de material/circuito, diferenciación de caudal de aristas y caras, sensibilidad de presión e inventario | Selección con TDS/SDS vigentes, reología/transitorios, compatibilidad, formación de superficies y emisiones |
| M3 UV/térmica | Exposición nominal, sombras angulares y partición eléctrica/óptica/térmica | Ventana material de gel/curado/unión, mapa óptico, driver, reacción y ruta de calor; responsable humano |
| M4 integración | Cámara, alternativas de gestión de gases, inventario, recursos y acceso | Alojamiento/asignaciones, generación de contaminantes, ruta aceptada y barreras dimensionadas |
| M5 control/metrología | Estados lógicos, diccionario temporal, alternativas de visión, calibración e incertidumbre | Datos/interfaces de hardware, criterio científico, cobertura, tiempos y respuesta física por fallo |

Fuentes técnicas fijadas a la versión revisada: [aporte M1–M3](https://github.com/eidanYT/Aegins-Project/blob/97ecaa8b791a9ba015076693d992796fa5ad2276/reviews/SRR/aportes_agente_tecnico.md), [modelo](https://github.com/eidanYT/Aegins-Project/blob/97ecaa8b791a9ba015076693d992796fa5ad2276/models/srr_agente_tecnico/README.md), [entradas](https://github.com/eidanYT/Aegins-Project/blob/97ecaa8b791a9ba015076693d992796fa5ad2276/models/srr_agente_tecnico/entradas.json) y [fuentes/acceso](https://github.com/eidanYT/Aegins-Project/blob/97ecaa8b791a9ba015076693d992796fa5ad2276/models/srr_agente_tecnico/fuentes.md). Algunos datos de catálogo solo provienen de extractos primarios; no se declara revisión completa de esas fichas.

## Contraste de integración

El integrador reconstruyó trece magnitudes en mm/mm³/mL y las convirtió a SI, sin importar ni ejecutar el código del agente técnico. Coinciden con sus resultados publicados: área/volumen nominal, caudales, longitud de raster, duración ideal, reserva/inventario, masa condicional y partición/energía UV. [Evidencia de contraste](../../evidence/contraste_tecnico_srr.json) y [programa](../../models/srr_integracion/contraste_tecnico.py).

Esto es una segunda comprobación de aritmética por otro agente, no revisión humana independiente ni validación de fuentes, robot, material o seguridad. No se contrastaron las poses ni la aplicabilidad hidráulica. Los resultados no cierran requisitos.

## Implicaciones para M4/M5

- Las caras necesitan sección de pista, espesor y modo de proceso diferentes de las aristas; el cambio se registra en ICD-001 y telemetría. El raster no resuelve apoyo inicial, unión ni última cara.
- El espesor de 0,0005 m y anchura de 0,0012 m son hipótesis técnicas TBR, no decisiones del usuario. Velocidad/diámetro didácticos tampoco son límites.
- Una alimentación remota incluye material del tubo, cebado, accesorios y presión residual; la reserva porcentual del material depositado no los cubre automáticamente.
- El calor local del LED no es toda la carga térmica del recinto. Si la luz se absorbe internamente, acaba contribuyendo al calor; incluir driver, reacción y otros módulos evitando doble conteo.
- Alcanzar muestras de poses con base fija no demuestra movimiento continuo, margen articular, cargas o compatibilidad de estación. La cámara no se dimensiona con la envolvente de la pieza solamente.
- Las vistas exteriores no verifican espesor, curado o interior de caras cerradas. Revisar inspección por etapas y acceso con M1/M2/M3.

## Próximo cierre documental

Revisar propuestas de ambos PR, aprobar decisiones y conformidades por módulos y consolidar versiones antes de maquetar el informe oficial. Mercado, presupuesto sustentado y cronograma con fechas reales siguen por completar. El CAD disponible es nominal de pieza y análisis ideal; falta ensamble del sistema. Seguimiento: [M1–M3](https://github.com/eidanYT/Aegins-Project/issues/5), [M4](https://github.com/eidanYT/Aegins-Project/issues/3), [M5](https://github.com/eidanYT/Aegins-Project/issues/4).
