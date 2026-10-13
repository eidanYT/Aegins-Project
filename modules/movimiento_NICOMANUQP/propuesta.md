# Propuesta — M1: Movimiento

**Estado: TBR, propuesta para revisión; versión 0.1, 2026-10-12.** Autor: agente técnico por encargo de Eidan. Revisor propuesto: NICOMANUQP, sin conformidad registrada. Rama `tecnico/m1-m3-srr`.

[Alcance](ALCANCE_TECNICO.md) · [Requisitos](../../system/requisitos.md) · [Modelo reproducible](../../models/srr_agente_tecnico/README.md) · [Ficha de arquitecturas](candidatos.md)

## Objetivo y necesidad de orientación

Proponer un brazo para posicionar la boquilla y dirigir su eje/iluminación sobre aristas y caras de la pieza. La orientación sirve para estudiar su efecto sobre la deposición y el curado, y para acceder a caras de distinta normal. El protocolo científico y los errores admisibles se acuerdan con M5; un brazo complejo por sí solo no aporta evidencia científica.

El prompt original conserva plataforma/base/tipo de impresión abiertos. Este análisis usa **condicionalmente** una bipirámide regular cuadrada, aristas 0,05 m y caras cerradas, coincidente con aclaraciones de Eidan en el chat. El integrador debe formalizarlas. No se asume ISS, montaje rígido certificado ni interfaces de host disponibles. Se conserva el brazo solicitado y se compara con una arquitectura más simple como pide R1.

## Alternativas y criterio de elección

| Opción | Qué cubre / ventaja | Complejidad / limitación | Estado |
|---|---|---|---|
| A — brazo serial compacto, 5 articulaciones; sexto eje si se justifica | Posición 3D y dirección del eje de boquilla. Muñeca orientable para caras; un sexto giro permite roll de óptica/cámara asimétricas o gestión de manguera. | Calibración, holguras, singularidades, cables y colisiones. Es un concepto propio; actuadores/masa no seleccionados. | TBR, opción preferida para desarrollo conceptual por decisión de conservar brazo. |
| B — XYZ cartesiano con dos giros de cabezal | También cubre cinco variables de tarea; ejes traslacionales sencillos de calibrar y menor dependencia de cinemática serial. | Guías y marco pueden ocupar más volumen/ocultar caras; no es automáticamente más ligero. Requiere muñeca y acceso inferior o posicionador. | TBR, comparación de menor complejidad cinemática. |
| Referencia terrestre UR5e | Referencia documental de seis ejes, no modelo del payload. | Dimensiones/recursos de catálogo no justifican usarlo en estación; ver F05 y ficha. | Candidato comparativo, no seleccionado ni calificado para vuelo. |

Cinco grados de libertad bastan **como número de variables** para posición y dirección si el cabezal es axialmente simétrico. El modelo evalúa un brazo ideal específico; no demuestra que todo mecanismo de cinco ejes alcance cualquier pose. Mantener seis ejes como alternativa si M2/M3 muestran que roll es una variable independiente. No sumar un eje sin explicar qué tarea lo necesita.

Antes de puntuar coste/masa: exigir alcance de poses, margen de colisión, retención y parada, compatibilidad del cabezal y montaje del host. No hay pesos arbitrarios ni ganador cuantitativo por masa/potencia sin datos. La decisión provisional A se revisa si B cubre el experimento con menor coste/volumen, o si A exige un posicionador adicional.

## Trayectoria, anclaje y alcance

Caso TBR: marco de probeta en su centro, base del brazo (−0,12,0,0) m; enlaces 0,12/0,10 m y herramienta 0,03 m. No son dimensiones de un fabricante. La pieza externa ocupa 0,05×0,05×0,07071 m, tiene 12 aristas y 8 caras. No se reemplaza el caso didáctico compartido.

Secuencia conceptual: comprobar retención y estado de módulos; cebar en recipiente contenido; formar aristas con anclaje de inicio y uniones; después rellenar caras por pistas; terminar y registrar inspección. El anclaje deberá dejar accesibles ambas mitades y retener la pieza durante una parada. **Todavía no está resuelto cómo apoyar las primeras pistas de cada cara ni cerrar la última cara sin colisiones.** Comparar marco de aristas ya gelificado con fijación temporal/soporte retirado; son propuestas por revisar con M2/M4, no prueba de impresión libre.

El [raster sintético](../../models/srr_agente_tecnico/raster.csv) representa segmentos de cara, sin traslados ni uniones; no es un programa de fabricación. En el modelo se orienta la boquilla hacia cada cara y se evalúan extremos/centro de sus pistas: **888/888 poses** cumplen los límites articulares supuestos. La cinemática directa reproduce posición/dirección con residuos numéricos menores que 10⁻¹². Resultado de análisis, no exactitud física.

q4 toca ±π: no hay margen respecto a sus topes supuestos; revisar continuidad/desenvolvimiento y tubos antes de declarar MOT-001 satisfecho. No se han probado las 12 aristas como trayectoria ejecutable, movimientos entre caras, singularidades globales, velocidades articulares, rigidez ni colisiones de cuerpos. La malla OBJ describe solo la pieza ideal.

## Cargas y recursos

En microgravedad permanecen inercia, presión, fuerzas de contacto y tensión de mangueras. Para el cabezal F≈m aTCP más fuerzas de proceso/tubo; reacción de base requiere sumas de momentos e inercias de **todos** los enlaces. El peso terrestre es relevante en pruebas/montaje; no sustituye el caso en vuelo. Microgravedad no prueba ausencia de cargas ni permite elegir actuadores sin torque.

| Recurso | Valor / unidad / condición / fuente | Estado / dato que falta |
|---|---|---|
| Masa total y del cabezal | TBD kg; masa/CG/inercia de motor, enlace, cartucho y óptica | TBD; BOM y CAD de M1/M2/M3. El inventario de resina no es masa total del cabezal. |
| Volumen/envolvente del brazo | Alcance matemático máximo de muñeca 0,22 m; no envolvente de máquina. Entradas del modelo 0.1. | TBR; cuerpos, base, recorrido, anclaje y recinto TBD m³. |
| Potencia normal/pico | TBD W; se necesitan torque-velocidad, fricción, aceleración, drivers y frenado | TBD; no usar potencia de UR5e como presupuesto del brazo compacto. |
| Energía / calor | TBD J y W, por fase de operación | TBD; perfiles temporales y eficiencia. |
| Coste | TBD USD por unidad y desarrollo, consulta 2026-10-12 sin cotización | TBD; fabricación de enlaces, actuadores, encoders, integración y revisión. |

M2 entregará depósito/tubos/presión y fuerzas; M3 óptica/calor; M4 rigidez y cargas admisibles de base. Para estación, una base fijada se usa únicamente como **hipótesis cinemática**; límites de perturbación del alojamiento siguen abiertos. Si se compara satélite, el mismo cálculo de base fija no acredita dinámica acoplada ni control de actitud.

## Interfaces y preguntas para revisión

| ICD / requisito | Propuesta / pregunta concreta | Revisor / estado |
|---|---|---|
| ICD-001 / MOT-001 / SCI-001 | ¿Qué poses y orientación se necesitan para una comparación controlada, y qué error distingue su resultado? Velocidad constante 0,005 m/s solo EJEMPLO. | NICOMANUQP y Eidan/M5; pendiente. |
| ICD-002 / MOT-001 | Confirmar masa/CG/inercia y brida TCP; ¿cartucho en muñeca o remoto? ¿Roll necesario por óptica/tubos? | Gabriel/M2, M3, NICOMANUQP; pendiente. |
| ICD-002/004 / MOT-002 | ¿Dónde se fija brazo/pieza y qué fuerzas, momentos, rigidez y volumen admite M4? | Shelton/M4 y sistemas; pendiente. |
| ICD-003 / SCI-002 | Registrar marco, posición comandada/estimada y confianza; ¿cámaras ven caras inferiores, nodos y TCP? | Eidan/M5 y Shelton/M4; pendiente. |
| ICD-005 / SAF-001 | Retener pieza; parada coordinada que considere extrusión residual y UV, sin imponer “apagar todo” universalmente. | M2/M3/M4/M5; pendiente. |

## Verificación y próximo avance

Método A: geometría, poses y consistencia directa/inversa del modelo ideal, [resultado reproducible](../../models/srr_agente_tecnico/resultados.json). Revisión independiente pendiente; no ensayo T/D ni aprobación. Completar CAD de cuerpos/recorrido, barrido continuo, colisiones y cargas para PDR; identificar actuadores y presupuesto sustentado. Contrastar fuentes y revisar con NICOMANUQP y afectados, fecha por acordar.

[Fuentes F01/F05/F06/F07](../../models/srr_agente_tecnico/fuentes.md) · [Síntesis de integración](../../reviews/SRR/aportes_agente_tecnico.md)
