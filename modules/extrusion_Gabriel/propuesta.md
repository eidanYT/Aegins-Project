# Propuesta — M2: Material y extrusión

**Estado: TBR, propuesta para revisión; versión 0.1, 2026-10-12.** Autor: agente técnico por encargo de Eidan. Revisor propuesto: Gabriel Hurtado, sin conformidad. Rama `tecnico/m1-m3-srr`.

[Alcance](ALCANCE_TECNICO.md) · [Requisitos](../../system/requisitos.md) · [Fichas](candidatos.md) · [Cálculos](../../models/srr_agente_tecnico/README.md)

## Materiales y condiciones

| Formulación candidata | Motivo y comparación | Limitación / decisión |
|---|---|---|
| DELO **KATIOBOND GE680** | Referencia de extrusión fotoasistida en F01; punto de partida mejor documentado para aristas. Propiedades y condiciones exactas en F02. | TBR, recomendada para estudio de proceso, sin selección. Faltan SDS/TDS vigentes, reología de circuito, emisiones y criterio de autoapoyo de caras. No confundir con otro nombre comercial. |
| Dymax **4-20806** | Recubrimiento fotocurable con ficha primaria F03; contrasta una formulación de menor viscosidad nominal. | TBR, alternativa para estudiar pistas apoyadas/recubrimiento, no alternativa equivalente probada para aristas libres. No se conoce ventana de exposición aplicable ni estabilidad de caras. |

Las viscosidades provienen de métodos diferentes; no convertir su razón en predicción de caudal relativo. Densidad Dymax: 1,05 g/mL=1050 kg/m³, solo si se usa esa formulación. No transferir masa ni respuesta UV de GE680 a Dymax.

Se condiciona el concepto a un **recinto con ambiente controlado**, no a resina expuesta al vacío ni a cabina como única barrera. Plataforma, presión/temperatura/humedad, almacenamiento y compatibilidad del alojamiento se formalizan por integración. Los requisitos de frío de F02 afectan logística y energía; este paquete no asume que la estación proporcione refrigeración.

Selección: exigir primero TDS/SDS disponibles, compatibilidad química, evidencia de deposición/curado y evaluación de contaminantes. Comparar coste y disponibilidad después. No hay declaración de material inocuo, resistente en órbita ni “sin gases” por ser fotocurable o no tener solventes añadidos.

## Alimentación y ubicación

| Alternativa | Ventaja | Coste técnico y fallos |
|---|---|---|
| A — pistón motorizado en cartucho cerrado | Desplazamiento geométrico relacionable con Q; expulsión positiva sin superficie libre como principio de alimentación. Propuesta TBR preferida para CAD/control. | Sellos/compatibilidad, holgura, fricción, compliance y burbujas. Encoder de pistón **estima** entrega; no mide Q de boquilla. Requiere limitar fuerza/presión y contener rezume. |
| B — cartucho con pistón/barrera separadora y regulación de presión | Descarga masa de actuador del cabezal; antecedente neumático F01 como referencia terrestre. | Presión no fija Q ante cambios de viscosidad/boquilla; gas/regulador, alivio contenido, energía almacenada y parada residual. No se asume suministro neumático del host. |

Cartucho en muñeca reduce tubo/volumen muerto pero aumenta masa e inercia. Ubicación remota reduce masa transportada pero exige tubería, cebado, retención y respuesta. La comparación de A/B y esa ubicación se cierra con M1/M4; no se ha elegido un componente comercial.

## Caudal e inventario reproducibles

Para arista circular ideal, d=1,2×10⁻³ m y v=5×10⁻³ m/s (EJEMPLO de ICD-001): Q=πd²v/4=5,65487×10⁻⁹ m³/s=0,339292 mL/min. La boquilla no garantiza ese diámetro de cordón.

Para **caras**, pista rectangular hipotética w=1,2 mm y espesor t=0,5 mm: Q=wtv=3×10⁻⁹ m³/s=0,180 mL/min. Este cambio de modelo debe aparecer en control: no usar Q circular durante el relleno y declarar después pared de 0,5 mm. Contracción, fusión de pistas y sección real requieren datos.

Inventario TBR del caso geométrico condicional: 0,678584 mL en aristas; 4,440 mL en raster de caras; suma sin corregir cruces 5,11858 mL. Reserva ilustrativa de 20%: 6,14230 mL, masa 0,0108104 kg si se usa la densidad GE680 de F02. **El tubo supuesto de 0,5 m y Ø interior 4 mm retiene otros 6,28319 mL.** Parte+reserva+tubo=12,4255 mL; quedan por añadir boquilla, válvulas, purga y residuos no recuperables. No es margen de inventario validado.

Un depósito ilustrativo de 20 mL contiene 0,0352 kg de GE680. Si esos 20 mL alimentan también el cebado del tubo, el presupuesto anterior cabe nominalmente, pero no demuestra autonomía ni que la geometría se imprima. Si se llena aparte un tubo y además el depósito, inventariar ambos; no contar solo el cartucho.

## Presión, respuesta y balance

Modelo de sensibilidad estacionaria: ΔP=8ηLQ/(πr⁴), con η=54 Pa·s como valor de referencia **no como curva reológica**. Boquilla cilíndrica equivalente L=10 mm, r=0,6 mm; tubo L=0,5 m, r=2 mm. Resulta ΔP=84300 Pa para aristas y 44722,5 Pa para caras. Son caídas del modelo, no presión absoluta del circuito ni máximos seguros. Contrastar frente a reología, entrada cónica, relleno, filtros, temperatura y variación de lote.

La cizalla de pared ideal resulta 33,33/17,68 s⁻¹, distinta de la condición de F02; por eso no se presenta la predicción como dimensionamiento verificado. Un bloqueo puede generar presiones mayores: dimensionar contención por presión máxima creíble y capacidades reales, no por esas dos cifras.

Pistón Ø interior 20 mm supuesto: carrera útil ideal 63,662 mm para 20 mL; velocidad 1,80×10⁻⁵/9,55×10⁻⁶ m/s y fuerza hidrodinámica 26,4836/14,0500 N. Añadir fricción/sellos/transitorios y margen justificado al seleccionar actuador. Potencia hidráulica ΔPQ no es consumo eléctrico del motor.

Respuesta mínima del circuito: Qsalida≈Qpistón−Cef·dP/dt (y términos de fuga si existen), con Cef [m³/Pa]. Cef, fricción y burbujas son TBD; no se inventa una curva Q(t). En parada hay energía/presión residual y posible rezume; M5 debe separar orden, estimación y entrega real. Verificaciones futuras: masa recogida por tiempo, calibración gravimétrica/densidad, presión registrada, escalones/rampas y comportamiento tras corte de energía, dentro de una contención adecuada.

## Recursos y seguridad para integración

| Recurso | Valor / unidad / condición / fuente | Estado / dato faltante |
|---|---|---|
| Masa de material | 0,0352 kg por cartucho ilustrativo de 20 mL GE680; cálculo/F02 | TBR; depende del inventario total y volumen muerto. Hardware/CG/inercia TBD. |
| Volumen | 20×10⁻⁶ m³ útil de depósito; 6,28319×10⁻⁶ m³ interno de tubo del caso | TBR; dimensiones exteriores/actuador/segundo contenedor TBD m³. |
| Potencia normal/pico | TBD W | Motor/regulador/válvulas y secuencia, fuerza/velocidad/fricción reales. |
| Energía / calor | TBD J / W | Perfil de alimentación, eficiencia; calor de reacción con M3. |
| Coste | TBD USD, cantidades y fecha de consulta 2026-10-12; sin cotización | Resina/envase, almacenamiento, pistón/sellos, sensores, ensayos y contención. No precio histórico ni coste de vuelo. |

Inventario de peligros a caracterizar, **no composición química identificada**: resina líquida no curada y rezume; especies volátiles según formulación/SDS y temperatura; partículas por curado, rotura o abrasión; restos de envases/material de limpieza si se incorporan; presión atrapada y burbujas. Resina comercial y fraguada no son garantías de no emisión. No introducir disolventes de limpieza sin inventariarlos.

SDS regional vigente **TBD** para ambas formulaciones: no se dispone de clasificación, exposición admisible ni mitigación química sustentada. Compatibilidad de sellos, tubos, adhesivos y cartucho **TBD**; la ficha de resina no los valida. M4 debe diseñar retención primaria/secundaria, acceso y ruta de gases tras conocer inventario/host; no se propone descarga automática a cabina, soporte vital ni exterior.

## Interfaces y siguiente acción

| ICD / requisito | Propuesta / pregunta concreta | Revisor / estado |
|---|---|---|
| ICD-001 / EXT-001 | Qgeom aristas/caras y modo explícito; medir retardos/rezume. ¿Qué volumen de error permite M5 en una rampa o nodo? | Gabriel, NICOMANUQP, Eidan/M5; pendiente. |
| ICD-002 / EXT-002 | ¿Cartucho local/remoto, volumen muerto, fuerza de tubo, material de sellos y presión máxima admisible? | M1, Gabriel, Shelton/M4; pendiente. |
| ICD-003 / CTL-001 | pressure_Pa con punto y referencia, Q estimado con origen/incertidumbre, reloj común y calibración. | Eidan/M5; pendiente. |
| ICD-004 / INT-002 | Incluir frío de almacenamiento si se mantiene GE680, inventario inicial y componentes por fase. | Shelton/M4 y sistemas; pendiente. |
| ICD-005 / EXT-002 / INT-001 | SDS, fugas, bloqueo y material residual; ¿qué retiene cada barrera y cuándo se abre? | M3/M4/M5 y Gabriel; pendiente. |

Método A realizado: conversión SI, geometría de consumo y sensibilidad; comprobación interna del autor, independiente pendiente. Obtener/contrastar TDS/SDS vigentes y seleccionar circuito CAD; planificar caracterización futura sin decir que se construirá durante este programa. Revisión con Gabriel y afectados, fecha por acordar.

[Fuentes F01–F03/F06/F07](../../models/srr_agente_tecnico/fuentes.md) · [Resultados](../../models/srr_agente_tecnico/resultados.json) · [Síntesis](../../reviews/SRR/aportes_agente_tecnico.md)
