# Aportes técnicos M1–M3 para integración del SRR

**Versión 0.1 — 2026-10-12; BORRADOR TBR, sin revisión independiente ni conformidades.** Rama `tecnico/m1-m3-srr`, base leída `d1b064ee53fec257597b8675a81d27660007ed80`. Se sigue el prompt original de Eidan. El otro agente conserva M4/M5 y documentación compartida.

## Entrega y alcance establecido

Quedan redactadas [M1 movimiento](../../modules/movimiento_NICOMANUQP/propuesta.md), [M2 material/extrusión](../../modules/extrusion_Gabriel/propuesta.md) y [M3 UV/térmica](../../modules/uv_termica/propuesta.md), con alternativas, fichas, recursos/datos faltantes y preguntas. El [modelo reproducible](../../models/srr_agente_tecnico/README.md) añade entradas SI, resultados, raster, poses y malla externa de referencia. Las [fuentes](../../models/srr_agente_tecnico/fuentes.md) registran versiones y diferencias entre texto completo y extracto indexado. El [registro de tarea](../../management/agent_runs/tecnico_m1-m3-srr.json) permite reanudar.

Se ha comprobado **aritmética y consistencia del modelo condicional**: geometría por métodos distintos, cierre, 888 poses del brazo ideal y conversiones. No hay ensayos, mediciones, precisión de máquina demostrada ni curado/resistencia acreditados. No existe revisión técnica independiente. El raster no demuestra que las caras se sostengan, unan ni sean estancas.

## Contexto que debe reconciliar el integrador

El prompt reenviado y main registran plataforma/base/impresión abiertas. En este chat Eidan había indicado estación espacial, conservar brazo, base cuadrada, aristas de 5 cm y aristas+caras cerradas. Este paquete conserva esas aclaraciones como procedencia y analiza el caso **condicional**, sin cerrar D-001 ni editar documentos comunes. Formalizar una estación conceptual no identifica ISS, alojamiento, atmósfera ni interfaces de gases disponibles.

El programa culmina en documentación/diseño CAD según Eidan. Los ensayos descritos son verificaciones futuras, no fabricación comprometida hoy ni resultados del programa. La estimación de tecnología futura y el coste del trabajo documental deben separarse en el presupuesto integrado; este paquete no transforma un importe sugerido en cotización o financiación.

## Entradas y salidas propuestas, sin sustituir ICD vigentes

| Variable / intercambio | Valor y unidad SI; conversión | Fuente / condiciones | Estado |
|---|---|---|---|
| Geometría M1↔todos | a=0,05 m; 6 vértices/12 aristas/8 caras; 0,05×0,05×0,07071 m | Declaración usuario y geometría regular condicional | TBR en documentos comunes |
| Espesor/anchura cara | t=0,0005 m; w=0,0012 m | Hipótesis de pista rectangular; no espesor elegido por usuario | TBR |
| v_path_cmd | 0,005 m/s=5 mm/s | ICD-001 EJEMPLO; tramos constantes, no crecimiento medido | EJEMPLO |
| Diámetro arista / boquilla | d=0,0012 m | EJEMPLO; igualar diámetro de filamento a boquilla es hipótesis | EJEMPLO |
| q_cmd geométrico arista/cara | 5,65487×10⁻⁹ / 3,00×10⁻⁹ m³/s = 0,339292 / 0,180 mL/min | Ac v; se cambia sección al cambiar modo; no lectura real | EJEMPLO / TBR |
| Cantidad parte+reserva | 6,14230×10⁻⁶ m³=6,14230 mL; masa 0,0108104 kg GE680 | Aristas+raster, sin corregir cruces; reserva 20% ilustrativa | TBR |
| Volumen muerto tubo remoto | 6,28319×10⁻⁶ m³=6,28319 mL | Ø interior 4 mm, 0,5 m; no incluye otros accesorios | TBR |
| Espectro / exposición | Banda de referencia 365 nm; E=2500 W/m², zona 0,002 m, Hnom=1000 J/m² | F01/F02 y EJEMPLO ICD-001; banda no acredita dosis/proceso | TBR / EJEMPLO |
| Masa/CG/inercia del cabezal | TBD kg/m/kg·m² | Cartucho, motor, óptica, soporte, tubo y cableado según ubicación | TBD |
| Montaje/alcance | Base (−0,12,0,0) m; links 0,12/0,10 m; herramienta 0,03 m | Modelo de 5R ideal, sin cuerpos ni fijación; 888 poses muestreadas | TBR |
| Presión | Sensibilidad ΔP=84300 / 44722,5 Pa | Newtoniano con η de referencia, no máximos seguros/reales | TBR |
| Consumo eléctrico UV / calor | 15,4 W típicos / 10,24 W locales LED | Cuatro emisores equivalentes F04, sin driver/reacción; ~Pel si óptica absorbida en recinto | TBR |
| Energía UV | 24640 J=6,8444 Wh, durante 1600 s de deposición ideal | Sin postcurado, standby ni pérdidas/otros módulos | TBR |
| Potencia/pico/masa/volumen/coste conjunto | TBD W/kg/m³/USD | Sin BOM, alojamiento, fase coincidente ni cotización | TBD |
| Señales / latencias | Tiempo s; pose m/rad; Q m³/s; P Pa; E W/m²; T K; incertidumbre/validez/origen | ICD-001/003; frecuencia, desfase y puntos de medida TBD | TBR |

Una única fuente de verdad se acordará en ICD/config de integración; las entradas de este modelo son una **instancia de análisis**, no una nueva configuración global. No se modificó el caso didáctico. Los precios actuales, tolerancias y datos de lote no están disponibles. No sumar picos de fases distintas ni sumar Pel y su partición óptica/térmica por duplicado.

## Filas de requisitos propuestas para revisión

Mantener IDs y padres vigentes; el integrador puede incorporar estas precisiones, **todas TBR**. “A realizado” significa análisis limitado, no requisito aprobado o físicamente verificado.

| ID / padre | Texto/criterio propuesto | Evidencia actual y futura | Revisión |
|---|---|---|---|
| MOT-001 / SCI-001 | Cubrir poses de aristas/caras y traslados con margen articular, orientación y colisión especificados; criterio geométrico/margen TBD | A limitado: 888 muestras de raster ideal. A futuro: CAD de cuerpos, trayectoria continua/aristas, tubos/topes y singularidades | NICOMANUQP/M2/M3/M4 |
| MOT-002 / SYS-001 | Respetar cargas/reacciones de montaje según ambiente y fases; N/N·m TBD | A futuro con masa/CG/inercia y límites host; no demostrado por base fija del modelo | M1/M4/sistemas |
| EXT-001 / SCI-001 | Entregar Q por modo arista/cara con error/retardo compatibles con precisión asignada; límites TBD | A geométrico actual. T futuro: Q/presión en escalones, rampas y parada; encoder no mide entrega | Gabriel/M1/M5 |
| EXT-002 / SYS-001 | Mantener materiales, presión máxima creíble y resina dentro del circuito/retención aprobados | I de SDS/TDS/BOM pendiente; A de sensibilidad actual; T futuro de compatibilidad/fugas/bloqueo | Gabriel/M4/M3 |
| UV-001 / SCI-001 | Entregar espectro e historia H(t) dentro de ventana material de gel/curado/unión; ventana TBD | A nominal/angular actual; T futuro radiometría y material; Hnom no valida conversión | M3/M2/M1/M5 |
| THM-001 / SYS-001 | Mantener límites por componente/material/host con reacción, driver y absorción incluidos | A de partición/sensibilidad actual; A/T futuro con ruta térmica y cinética | M3/M4 |
| INT-001 / SYS-001 | Retener inventario de líquidos, partes/partículas y contaminantes en operación y fallos; eficacia y límites TBD | Inventario preliminar M2/M3; A/I/T de barreras/ruta/apertura a cargo de integración | M2/M3/M4/M5 |
| INT-002 / SYS-001 | Presupuestar masa/volumen/energía/picos por fase, incluidos cebado, almacenamiento y seguridad | A parcial actual; BOM, tolerancias, asignación host y suma de fases pendientes | M4 con todos |
| CTL-001 / SCI-001 | Diferenciar commanded/estimated/measured, reloj común y validez; límite temporal derivado de error asignado | A de sensibilidad: Δx=vΔt; umbral TBD; D/T futuro de secuencia/sincronía | M5 con M1–M3 |
| SCI-001/SCI-002/MET-001 | Comparación orientaciones con trayectoria accesible a ambos casos y variables controladas; incertidumbre capaz de distinguir efecto | Protocolo/umbral TBD; comparar una cara accesible con otra inaccesible confunde orientación y cobertura/dosis | M5/sistemas |
| SAF-001 / SYS-001 | Estado seguro por acceso, bloqueo, fuga, térmica y pérdida de energía, considerando presión residual | Propuestas abajo; A/D/T futuros, tiempo y criterio de apertura TBD | M4/M5 con M1–M3 |

## Filas de interfaces propuestas

| ICD | Intercambio / propuesta concreta | Fallo / condición | Conformidades requeridas, pendientes |
|---|---|---|---|
| ICD-001 | process_mode=arista/cara; q_geom según sección; t_s común; UV objetivo vs medido; pendiente rampa/parada con Cef/gel | v=0 invalida L/v; no comandar dosis infinita ni asumir Qsalida=0 al parar pistón | M1/M2/M3/M5 |
| ICD-002 | Marco de probeta, base, TCP y eje +z documentados; masa/CG/inercia/brida y roll con unidades; anclaje y recorridos reales TBD | Límite q4 tocado, colisiones y manguera, acceso inferior/última cara no resueltos | M1/M2/M3/M4 |
| ICD-003 | Fuente/origen/incertidumbre/calibración/punto de lectura en Q/P/E/T/pose, t_monótono y validez; mode/version de entradas en registro | Saturación de cámara, sensor inválido/desfase y compresión de gas; no atribuir medición a consigna | M5/M1/M2/M3; M4 montaje |
| ICD-004 | Masa y calor/energía por fases cebado–deposición–postexposición–inspección–standby; almacenamiento y soporte térmico host TBD | Sin límites de montaje, presión/temperatura y picos host no hay compatibilidad acreditada | M4/todos y contacto host |
| ICD-005 | Inventario resina/tubo/envases/residuos, bloqueo/rezume/acceso, protección UV y retención; secuencia por fallo | Corte eléctrico puede apagar UV mientras sigue rezume; abrir solo según criterios revisados de presión, química y UV | M2/M3/M4/M5; M1 movimiento |

Ninguna fila está conforme. No basta que el autor cubra varios módulos: sigue haciendo falta revisión independiente de interfaces.

## R1, peligros y efectos en recursos

| Seguimiento / evento | Cambio propuesto y evidencia | Límite / coste a integrar |
|---|---|---|
| EXP-01, complejidad del brazo | Cinco variables de tarea justificadas; sexto giro condicionado; comparación cartesiana y poses de brazo ideal | No demuestra mecanismo en microgravedad. Calibración, cuerpos/rigidez, actuadores, tubos y base deben presupuestarse |
| EXP-02, gases/polvo | Inventario M2, SDS vigentes pendientes, modos de líquido/partículas/emisiones con temperaturas/proceso registrados | No identificar sustancias ni eficacia de filtros sin datos. Costes de retención, caracterización, instrumentación y recuperación |
| EXP-03, seguridad/costes | UV, presión, fugas, térmica, acceso, energía y control coordinados; partición térmica y volumen muerto cuantificados | Barreras/interlock/sensores y revisión especializada aumentan recursos. No estimación monetaria sustentada aún |
| Atasco/presión residual | Limitar esfuerzo/presión por capacidades reales; retención secundaria y diagnóstico; alivio si procede a contención definida | Valores/compatibilidad TBD; ΔP nominal no presión máxima de diseño |
| Acceso con UV/resina no curada | Interlock, atenuación, señalización y recuperación condicionada a evaluación química | Validar hardware/atenuación y SDS; no eficacia afirmada |
| Calor/exotermia | Conducción al soporte, sensores ubicados y límite térmico por componente; no asumir enfriamiento terrestre | Entalpía/conversión y conductancia faltantes; fuente óptica también calienta el recinto |
| Desprendimiento/colisión | Anclaje de pieza y geometría de retención, paro coordinado | CAD/visibilidad y estado seguro pendientes |

**Atribución por revisar:** el PDF R1 tiene dos tablas de puntuación de expertos; el comentario de ampliar seguridad aparece firmado por ACHIEVED Orbital Team. La matriz compartida lo atribuye a experto 2. Se conserva su contenido técnico y se propone corregir la atribución al integrar, sin editar aquí el archivo fuera de ámbito. Las observaciones permanecen abiertas, sin aceptación del jurado.

## Verificación, revisión y próximos pasos

| Pendiente / impacto | Responsable propuesto | Fecha / siguiente acción |
|---|---|---|
| Formalizar geometría y estación conceptual; fijar ambiente/asignaciones sin afirmar alojamiento | Integrador/sistemas con Eidan | Hoy como objetivo; revisión por acordar. Actualizar D-001/documentos comunes |
| Contrastar fuentes e independientemente rehacer geometría/caudal/poses/balance | NICOMANUQP, Gabriel, humano M3 por designar y revisor independiente | Por acordar; registrar método, versiones, diferencias y conformidad |
| SDS/TDS vigentes, material y compatibilidad; presión máxima creíble / respuesta | Gabriel con M3/M4 | Por acordar; obtiene documentos por canal autorizado, sin comunicación enviada por este agente |
| Mecanismo/actuadores, continuidad, colisiones, base, tubos y anclaje para caras | NICOMANUQP/M4 con M2/M3 | Por acordar; CAD y análisis para PDR |
| Gel, apoyo inicial, unión entre pistas y última cara | M2/M3/M1/M4 | Por acordar; revisar concepto y plan de futura caracterización. Bloquea afirmación de imprimibilidad |
| Óptica/ruta térmica; presupuesto de driver/reacción/postexposición | Humano M3 por designar y Shelton/M4 | Por acordar; completar BOM/mapa y límites |
| Métricas, sincronía, cámaras y estados seguros | Eidan/M5 con afectados | Por acordar; cerrar tolerancias y diccionario de datos |
| Costes de CAD/concepto vs tecnología futura, seguridad y verificación | Integrador/sistemas | Por acordar; cantidades, base de estimación, fase, incertidumbre y cotizaciones |

Se realizaron 12 comprobaciones internas del modelo y el control local de ámbito/registro/enlaces se ejecuta antes de publicación; consultar resultado real en registro/PR. La CI estructural no verifica física ni sustituye conformidad. No hay afirmaciones VERIFICADO de hardware ni evidencia ficticia. Para integrar el informe, citar estas cifras como análisis preliminar bajo supuestos y conservar todos los pendientes.

## Texto breve reutilizable en el informe

AEGINS propone un brazo orientable para dirigir la deposición y la iluminación sobre una probeta, comparado con una arquitectura cartesiana. Para el caso condicional de una bipirámide cuadrada de aristas de 50 mm y caras cerradas, un modelo ideal de cinco articulaciones alcanza las 888 poses muestreadas del raster de caras, sin demostrar continuidad, colisiones ni precisión física. La necesidad de un sexto giro depende de la óptica y el recorrido de tubos. El cálculo diferencia cordones de aristas y pistas de caras, e incorpora el efecto del volumen muerto de una alimentación remota. El material, su ventana de gel/curado y la seguridad de emisiones siguen sujetos a documentación y caracterización. La exposición nominal y el balance eléctrico/térmico son análisis preliminares; la imprimibilidad de las caras, la compatibilidad con un alojamiento y la verificación física permanecen pendientes.
