# M5 Control y metrología

Participante de referencia: **Isaac Oscco Tomilla**. Estado de criterios nuevos: propuesta para revisión del equipo, 18 de octubre de 2026.

El módulo elige cómo alcanzar los resultados y aporta evidencia revisable. Interfaces: ICD-001, ICD-002, ICD-003, ICD-004 e ICD-005.

### PDR-M5-01 Definir control, señales y estados

**Resultado y aceptación.** Arquitectura GR740, SAMRH71, RTG4, seis EPOS4 y CAN para control; imágenes CASPEX por interfaz y buffer dimensionados por separado. Definir lazos, cadencias, relojes, latencia, validez y secuencia nominal/fallo. La seguridad física no depende solo del computador.

**Evidencia de cierre.** Arquitectura de software/hardware y diccionario ICD; estados con permisos, timeouts y recuperación autorizada.

### PDR-M5-02 Cerrar criterio geométrico y presupuesto de error

**Resultado y aceptación.** Definir error de posición y orientación TCP, eRMS de pieza, desviación máxima, espesor/diámetro, cobertura, muestras inválidas e incertidumbre. Separar error de máquina, proceso, tiempo y medición. Fijar valores numéricos justificados antes de aceptar resultados de diseño.

**Evidencia de cierre.** Presupuesto de errores y calibración a través de ventanas reales; comparación de orientación fija/variable con controles equivalentes.

### PDR-M5-03 Dimensionar cómputo, almacenamiento y energía

**Resultado y aceptación.** Presupuesto CPU, memoria, imágenes, telemetría y alimentación con ECC/estrategia de fallos/radiación. UT8MR2M8 de 2 MB se reserva a estados y parámetros; no se da por suficiente para imágenes. Resolver compatibilidad de sensores, encoders, controladores y buses.

**Evidencia de cierre.** Cronograma de tareas y tráfico, memoria por función y matriz de compatibilidad; TSIM es apoyo de software y no evidencia de latencia física.

## Desarrollo avanzado

### ADV-M5-01 Integrar simulación de brazo extrusor y UV

**Resultado y aceptación.** Un único reloj de simulación coordina seis articulaciones, trayectoria, caudal, presión, dosis, temperatura y material añadido. Separar comandos, estimaciones y mediciones. Modelos intercambian datos con unidades, marcos, secuencia, validez y latencia explícitos.

**Evidencia de cierre.** Escena reproducible de la bipirámide con doce aristas y ocho caras cerradas, más una segunda geometría, vídeo y logs temporales; estado de física/calibración declarado.

### ADV-M5-02 Verificar interfaces y recuperación

**Resultado y aceptación.** Ensayos de software en el lazo con emuladores de sensores/actuadores, retardos, jitter, pérdidas/reordenación, CRC/formato incorrecto, calibración inválida, atasco y fallo de energía. Pasar a hardware en el lazo cuando exista equipo. Distinguir emulación ROS del protocolo de vuelo.

**Evidencia de cierre.** Pruebas automáticas de contrato y de fallos con criterio temporal derivado del presupuesto, registro de eventos y trazabilidad a ICD-001/003/005.

### ADV-M5-03 Demostrar calidad y comparación de impresión

**Resultado y aceptación.** Reconstruir geometría simulada o medida sin usar los comandos como verdad de medición. Comparar orientación fija y variable en tareas accesibles a ambas, con registro de lote, exposición, apoyo y velocidad. Propagar incertidumbre y reportar fracasos.

**Evidencia de cierre.** Informe de error, espesor, cobertura, volumen y dosis; contraste de resultados con referencia independiente y conjunto de casos retenidos.

## Registro del resultado

Mantener en [propuesta](propuesta.md) las decisiones, fuentes y evidencias de cada ID. Toda cifra requiere unidades, condiciones y procedencia; los umbrales pendientes se cierran antes de declarar cumplimiento. [Requisitos comunes](../../system/requisitos.md) · [Interfaces](../../interfaces/README.md) · [Equipo](../../management/equipo.md).
