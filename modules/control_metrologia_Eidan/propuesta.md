# Propuesta — M5: Control y metrología

**Estado: TBR — propuesta conceptual para revisión.** Responsable de módulo: Eidan. Redacción: Codex a solicitud de Eidan, 12 de octubre de 2026. Rama: integracion/m4-m5-srr. No se ha elegido hardware ni verificado desempeño físico.

## Objetivo y caso común

Coordinar movimiento, alimentación y UV, conservar trazabilidad temporal y medir la geometría obtenida. El escenario elegido es estación espacial con tripulación y cámara de proceso. La [pieza común](../../system/caso_srr.json) tiene base cuadrada, aristas de 0,05 m y caras cerradas; material, espesor, tolerancias y estrategia de impresión todavía no están elegidos.

No se exige que la orientación variable mejore el resultado: se comparan orientación fija y variable y se permite confirmar, limitar o rechazar la hipótesis.

## Arquitecturas de control alternativas

| Concepto | Ventaja a evaluar | Riesgo / condición | Estado |
|---|---|---|---|
| A: controlador del mecanismo + controlador de proceso + ordenador de visión/registro | Permite separar adquisición/temporización del procesamiento de imágenes | Comunicación, relojes, fallos de enlaces y presupuesto de recursos deben justificarse | TBR |
| B: control de proceso e integración en un único controlador compatible, con visión/registro como servicio separado | Menos enlaces entre órdenes de proceso y movimiento si la interfaz del mecanismo lo permite | Capacidad temporal, aislamiento, compatibilidad de interfaces y recuperación no demostrados | TBR |

Propuesta inicial: desarrollar el contrato de A porque separa funciones y permite medir retrasos de cada enlace. No equivale a seleccionar MCU, ordenador, cámara ni un sistema certificado. Si M1 entrega un controlador con sincronización apropiada, comparar B con datos reales antes de cerrar la arquitectura.

## Instrumentación candidata por función

Los [candidatos para un demostrador terrestre](candidatos_prototipo.md) concretan controlador de proceso, visión y cámara con fuentes del fabricante. Siguen sin seleccionar; no se trasladan sus prestaciones a un equipo de vuelo.

| Función | Concepto a comparar | Dato que falta |
|---|---|---|
| Geometría tridimensional | Cámaras calibradas con vistas simultáneas; alternativa de vistas sucesivas para pieza estable | Cobertura, correspondencia, óptica, montaje, resolución y calibración |
| Presión del circuito de material | Transductor con punto de medida definido por M2 | Rango, compatibilidad, respuesta, calibración y presión residual |
| Temperatura | Medida en puntos definidos por M3/M4 | Rangos, ubicación, contacto/no contacto, respuesta y error |
| Contención y acceso | Estado de cierre e instrumentos derivados del análisis de peligros | No elegir detector químico sin conocer los contaminantes |
| Movimiento/UV/alimentación | Estado y datos del controlador de cada módulo | Protocolos, señales disponibles, significado y tiempos |

No usar el encoder del brazo como medida de la pieza ni una consigna UV como irradiancia medida.

## Estados, datos y sincronización

El [ICD-003](../../interfaces/ICD-003.md) mantiene la definición compartida de señales. Usar tiempo monótono común, identificador de reloj, secuencia y origen commanded/estimated/measured. Conservar instante de adquisición y recepción, calibración y validez; no reemplazar un dato ausente por cero.

La [máquina de estados conceptual](../../models/srr_integracion/control_conceptual.py) recorre IDLE → CHECK → READY → PRIME → PRINT → FINISH → INSPECT → IDLE. Eventos de fallo llevan lógicamente a HOLD, que exige autorización y nueva comprobación para reanudar. No emite órdenes a hardware ni define por sí sola una secuencia de seguridad.

Para empezar proceso se requiere, como propuesta: cierre y ruta de contención definidos, datos válidos, calibración/tiempo vigentes y respuesta de fallo acordada. Umbrales y cadencias se fijarán desde requisitos, banda del proceso y hardware, no mediante un número genérico.

## Métricas y medición

- Geometría de aristas y superficies: comparar reconstrucción contra nominal en un marco registrado mediante referencias independientes de la pieza. Definir regiones visibles y exclusiones.
- Diámetro de cordón y espesor de caras: son magnitudes distintas. La inspección óptica exterior no mide automáticamente espesor ni superficie interior de una pieza cerrada.
- Continuidad/cierre: registrar discontinuidades y zonas no observables; una malla nominal cerrada no demuestra que la pieza fabricada sea estanca.
- Curado: mantener el método que defina M3; la apariencia, dosis nominal o color no sustituyen caracterización de material.
- Condiciones del proceso: presión, temperatura, movimiento, exposición disponible, comandos y calidad temporal.

El [plan de metrología](metrologia.md) desarrolla alternativas, calibración e incertidumbre.

## Presupuesto temporal inicial

Si la velocidad permanece acotada por v_max durante el intervalo, el desplazamiento asociado a desfase total satisface e_t≤v_max·Δt_total. De una asignación e_t,asignada se deriva Δt_total≤e_t,asignada/v_max.

La asignación incluye reloj, adquisición, transporte y actuación según el modelo, evitando contar dos veces el mismo retardo. No sustituye la dinámica hidráulica ni corrige automáticamente retrasos.

El [ejercicio reproducible](../../evidence/srr_integracion_calculos.md) conserva únicamente los números didácticos existentes: 5 mm/s y 50 ms dan 0,25 mm; asignar hipotéticamente 0,10 mm al tiempo permite 20 ms para ese tramo. **No son límites de misión aprobados ni un máximo de velocidad verificado.**

## Recursos y fallos

Definir consumo y almacenamiento por estado, datos de imagen y telemetría, operaciones autónomas y recuperación. El [presupuesto compartido](../../system/presupuestos.md) identifica entradas aún desconocidas.

La respuesta a pérdida de energía debe existir en hardware/contención o reserva de energía justificada; que el modelo de software tenga un evento power_lost no garantiza ejecución después de quedar sin alimentación. Revisar [ICD-005](../../interfaces/ICD-005.md) con M2/M3/M4/M1.

## Verificación y revisión

Para SRR: inspección de arquitectura/diccionario, cálculos de sensibilidad temporal, pruebas del modelo lógico y presupuesto de incertidumbre pendiente de datos. Para prototipo futuro: sincronización medida, calibración con patrón independiente y respuesta de fallos con hardware.

| Punto | Pregunta concreta | Revisor | Estado |
|---|---|---|---|
| Nominal y referencias | ¿Cómo se imprimen caras y aristas y qué transformaciones entrega M1? | NICOMANUQP / M1 | Pendiente |
| Alimentación | ¿Qué retraso, lectura de presión y dinámica residual hay? | Gabriel / M2 | Pendiente |
| UV/temperatura | ¿Qué señales existen y qué iluminación interfiere con medición? | M3 | Pendiente |
| Cámara y acceso | ¿Qué vistas/ventanas y criterio de acceso permite M4? | Shelton / M4 | Pendiente |
| Metrología y fallos | ¿Qué diferencia relevante, incertidumbre y recuperación se aceptan? | Eidan y equipo | Pendiente |

Fuentes metodológicas: [NIST TN1297](https://www.nist.gov/pml/nist-technical-note-1297) y [OpenCV 4.13.0](https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html). La implementación de visión no está realizada; citar una biblioteca no verifica la medida.

Seguimiento: [metrología, temporización y fallos físicos](https://github.com/eidanYT/Aegins-Project/issues/4). Fecha de resolución y conformidades: por acordar.

Próximo avance: integrar protocolos y señales de M1/M2/M3, elegir instrumentación por prestaciones justificadas y cerrar el presupuesto de incertidumbre/cadencia con el equipo.
