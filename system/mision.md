# Misión y modelo de investigación

## Estado y procedencia
Confirmado por el usuario: el programa pide un payload para satélite o estación y no especifica si es tripulada.
La plataforma, ambiente interno, operación y recursos están TBD. No se declara cumplimiento de requisitos de la ISS.
Entrega del concurso: concepto, requisitos, modelos y CAD; pruebas físicas son un plan futuro.

## Pregunta científica propuesta (Esto puede cambiar)
¿Cómo cambia el error geométrico de una estructura no coplanar al orientar la boquilla con la trayectoria y coordinar caudal/UV, comparado con orientación fija, bajo un ambiente de microgravedad definido?

Hipótesis de trabajo: esa coordinación puede mejorar continuidad y geometría para ciertas trayectorias.
Resultado válido: confirmar, limitar o rechazar la hipótesis con incertidumbre explícita.
No imponer como requisito “demostrar una mejora” antes de obtener evidencia.

## Qué medir (pendiente de revision, tomenlo como propuesta|ejemplo)
| Métrica | Definición propuesta | Cómo obtenerla | Limitación |
|---|---|---|---|
| Error geométrico | RMS de distancias del centro del cordón a la trayectoria nominal, con registro definido | Reconstrucción óptica/calibración; inicialmente geometría sintética | Error de TCP no equivale a error del material |
| Diámetro | Media, desviación y CV = desviación/media sobre secciones acordadas | Imágenes calibradas con corrección de perspectiva | Identificar sombras, sección no circular e incertidumbre |
| Continuidad | Fracción de segmentos completados sin ruptura o desprendimiento | Criterio de fallo y registro de video | Pocos casos no definen fiabilidad de vuelo |
| Curado | Conversión o propiedad mecánica mínima elegida | Ensayo/material caracterizado en fase futura | Dosis y color no demuestran curado suficiente |
| Proceso | Temperatura, presión, comandos y estimaciones temporales | Telemetría sincronizada | Comando no es medición |

Comparar el mismo robot y misma geometría con orientación fija y variable, manteniendo el resto o registrando diferencias.
Para evaluar el ambiente: diseño factorial orientación × gravedad, cuando haya recursos experimentales.
Aleatorizar orden, tratar piezas como réplicas y estimar número de réplicas con variabilidad/efecto objetivo.
Una simulación puede explorar sensibilidad; no estima beneficios reales sin un modelo validado.

## Por qué microgravedad
El cordón antes de curar puede responder a gravedad, tensión superficial, viscosidad y fuerzas de alimentación.
Reducir la gravedad cambia ese equilibrio y la convección natural. Eso permite preguntar qué limita el proceso cuando disminuye el peso propio.
DREPP aporta antecedentes experimentales [P1]; no prueba por sí solo que FORGE-UG vaya a mejorar.
No basta escribir “en el espacio es mejor”: identificar qué observable cambiaría y por qué no lo resuelve un ensayo terrestre equivalente.

## Decisión D-001: plataforma de referencia
| Opción | Ambiente que DEBE definirse | Consecuencia |
|---|---|---|
| Dentro de estación | Presión/temperatura, alojamiento, acceso y ocupación humana | Posible protección de tripulación; calor y emisiones hacia alojamiento |
| Payload autónomo de satélite con cámara | Presión interna elegida, autonomía, estructura e interfaces con bus | Contención, disipación hacia nave y reacción del brazo sobre actitud |
| Expuesto al exterior | Vacío, radiación, iluminación y ciclos térmicos | Materiales, lubricación, contaminación y gestión térmica cambian sustancialmente |

Recomendación de método: comparar opciones en 48 horas y escoger UNA para la línea base SRR.
No sumar prestaciones de distintos escenarios en un diseño sin demostrar compatibilidad.
Seleccionar solo satélite no determina que la resina esté expuesta a vacío; puede existir una cámara.
Seleccionar estación no determina presión ni presencia de tripulación en el alojamiento.

## ConOps inicial
Integración/lanzamiento con material y piezas retenidos → comprobación y calibración → preparación de semilla/anclaje → cebado contenido → impresión → estabilización/curado definido → inspección y datos → almacenamiento seguro.
Rama de fallo: detección → secuencia coordinada específica → diagnóstico → recuperación autorizada o fin de operación.
Incluir energía perdida, atasco, material desprendido y sensor no válido.

## Caso común
Ver config/caso_demo.json. Geometría, velocidad y diámetro son EJEMPLOS didácticos.
La geometría es una polilínea no coplanar en un marco local; sus esquinas requieren transiciones antes de planificar movimiento continuo.
El transformado entre marco de pieza y robot, el soporte y la factibilidad están TBD.

## Pieza de demostración propuesta por Eidan

Actualización de contexto del 12 de octubre de 2026 — **TBR, pendiente de revisión del equipo**.

Eidan propone imprimir una estructura formada por **dos pirámides unidas por su base**, con **cada arista de 5 cm (0,05 m)**. La denominación geométrica general es bipirámide; no es un prisma. El polígono de la base común y el número de aristas no se han especificado: no se asume automáticamente un octaedro de base cuadrada.

Quedan por definir: base común, geometría final y tolerancias, si se imprimen solo aristas o también caras, diámetro del cordón, anclaje, trayectoria y orden de impresión, transiciones, orientación y viabilidad cinemática. Esta propuesta no cambia todavía config/caso_demo.json, que sigue siendo un ejemplo didáctico.

Se mantienen **estación espacial y satélite como plataformas alternativas**, sin selección D-001. Eidan propone que la impresora opere dentro de una cámara y plantea una salida de gases cuya conexión aún desconoce. El [borrador de contención para el SRR](../reviews/SRR/contencion_gases_borrador.md) recoge la observación del jurado, alternativas y verificaciones pendientes.
