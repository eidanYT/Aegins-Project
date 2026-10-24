# Reparto de trabajo del equipo activo de FORGE UG

24 de octubre de 2026 · Equipo AEGINS · Acuerdo de organización de Eidan

## Objetivo y alcance

Organizamos el trabajo de los cinco integrantes activos alrededor de cuatro frentes conectados: arquitectura en Capella, componentes y adaptaciones, CAD preliminar y modelo matemático con control y metrología. La primera entrega común es una configuración preliminar compatible del brazo 6R, cabezal, sensores y cámara, que alimentará el PDR y el desarrollo posterior.

Eidan confirma que Isaac ya no participa y asume M5 además de la coordinación. Los documentos SRR y registros históricos conservan sus autores y reparto de origen. Este plan establece el reparto operativo actual; los IDs PDR y ADV existentes se conservan como criterios técnicos y trazabilidad, sin imponer tres trabajos independientes a cada persona. La organización del trabajo no acredita resultados técnicos ni aceptación de interfaces.

## Responsabilidades principales

| Integrante activo | Trabajo principal | Primera entrega |
|---|---|---|
| Shelton Yauri Huamani | Arquitectura e interfaces en Capella | Modelo nativo y vistas de funciones, componentes e intercambios con pendientes identificados |
| Andres Zelada Solano | Datos de componentes, compatibilidad y adaptaciones | Catálogo con fuentes, dimensiones, espacio de instalación y matriz de compatibilidad |
| Nicolas Quispe Papuico | CAD preliminar del brazo y distribución mecánica, con Gabriel | Ensamble inicial con seis ejes, eslabones, posiciones y dimensiones principales |
| Gabriel Hurtado Curi | CAD con Nicolas y distribución del cabezal y circuito de resina | Cabezal, depósito/dosificador, conductos, boquilla y sensores ubicados en el ensamble |
| Eidan Ajahuana Quiroz | Modelo matemático, factibilidad integrada, control, metrología y coordinación | Definición del modelo, entradas requeridas y método de medición; apoyo al CAD |

Los nombres siguen el registro del equipo; confirmar el nombre completo de Andres antes de una nueva portada oficial. Las revisiones técnicas se realizan con los integrantes activos, sin asignar tareas nuevas a Isaac.

## Shelton Yauri Huamani

Continúa el trabajo de arquitectura en Capella, declarado en curso por Eidan. Relaciona funciones con componentes y registra intercambios mecánicos, eléctricos, de datos, material y calor. Incorpora escenarios nominales y de fallo e identifica los valores todavía por acordar. Recibe las decisiones del CAD, del catálogo de componentes y del modelo matemático para mantener coherentes las vistas y los ICD.

Entrega el archivo nativo, vistas exportadas y una lista de interfaces con emisor, receptor, magnitud o conexión, unidad, estado y responsable de resolver pendientes. Eidan coordina la revisión de sistemas. La cámara y contención conservan su referencia M4; su detalle se programa con el equipo para mantener viable la carga de Capella.

## Andres Zelada Solano

Revisa los componentes seleccionados y confirma fabricante, modelo y variante exacta. Obtiene dimensiones y masa de fichas, planos o CAD del fabricante, con enlace, revisión y condiciones; los datos desconocidos quedan como TBD. Incluye fijaciones, conectores, alimentación, señales, protocolos, límites térmicos y acceso para mantenimiento cuando correspondan.

Registra tanto el volumen del componente como el espacio para montarlo y operarlo: enchufes, salida y curvatura de cables o tubos, refrigeración y desmontaje. Entrega modelos simplificados o archivos del fabricante cuando estén disponibles para incorporarlos al CAD.

La matriz distingue compatibilidad directa documentada, adaptación propuesta y compatibilidad pendiente. Para cada adaptación describe el problema, la solución propuesta, su impacto en espacio, masa, potencia o calor y qué comprobación falta. Adaptar puede requerir una brida, soporte, alimentación externa, acondicionamiento o interfaz; las modificaciones internas de equipos comerciales requieren justificación específica y consulta al fabricante cuando proceda. La adaptación de montaje no equivale a calificación espacial.

Empieza por los elementos que condicionan el brazo y el cabezal. UV y térmica conservan su referencia M3; la disposición de emisores, sombras y ruta térmica se acuerda con CAD y Eidan, registrando responsable y alcance de cada cálculo antes de asignarle más trabajo.

## Nicolas Quispe Papuico

Prepara con Gabriel el CAD preliminar en SolidWorks, con apoyo de Eidan. Define posiciones y orientaciones de los seis ejes, longitudes iniciales, forma aproximada de eslabones, base, brida, espacio del cabezal y ubicación de la pieza. Integra los datos y espacios de instalación que aporta Andres.

Entrega el ensamble nativo, una exportación STEP y vistas dimensionadas. Documenta unidades, revisión, ejes y marcos de base, pieza y punta de boquilla, con dimensiones provisionales y pendientes claramente identificados. Conserva espacio para tubos, cableado, sensores y acceso. Las masas estimadas se acompañan de su procedencia.

Su entrega principal es geométrica. Eidan lleva el modelo matemático de movimiento y cargas con su apoyo; la asignación del CAD no le exige entregar de antemano una simulación completa. Los cálculos pueden motivar cambios de geometría y una nueva versión del CAD.

## Gabriel Hurtado Curi

Colabora con Nicolas en el CAD y se concentra en la distribución física del cabezal y del circuito de resina. Propone dónde van depósito, dosificador, boquilla y sensor de presión, qué partes quedan fijas o móviles y por dónde pasan tubos y conexiones. Coordina con Andres las dimensiones, variantes y adaptadores necesarios.

Entrega el subensamble del cabezal, el esquema del circuito y sus dimensiones iniciales, interfaces, volumen ocupado y masa móvil estimada con fuente o supuesto. Reserva espacio para UV y sensores. Ayuda a Eidan a revisar las entradas del modelo de extrusión y la secuencia de construcción de la probeta. La simulación de resina y el modelo de transitorios se desarrollan con el alcance que se acuerde después de esta primera configuración.

## Eidan Ajahuana Quiroz

Coordina la configuración común y apoya el CAD. Lleva el modelo matemático y la evaluación integrada de factibilidad con los datos de los demás: relación entre articulaciones y pose de boquilla, alcance de la trayectoria, cargas y pares, entrega de resina, exposición UV y secuencia de fabricación de la bipirámide. Cada modelo explicita ecuaciones, entradas, unidades, supuestos, límites y datos pendientes; los especialistas revisan su parte.

En control define señales, consignas, tiempos, estados nominales y de fallo y coordinación entre movimiento, extrusión y UV. En metrología define cómo se medirá la pieza, qué métricas y tolerancias se evaluarán, ubicación y visibilidad de cámaras, calibración e incertidumbre. Mantiene separados comandos, estimaciones y mediciones independientes.

Integra progresivamente los modelos en una simulación común con ayuda de Gabriel, Nicolas y los demás según la necesidad. Una geometría inicial permite empezar; el diseño detallado y los modelos se refinan por versiones. Las conclusiones analíticas se expresan dentro de sus supuestos; la precisión y el comportamiento físicos necesitan mediciones y ensayos posteriores.

Reúne el PDR a partir del SRR, los aportes de Capella, el CAD y los análisis. Actualiza los requisitos, presupuestos y riesgos afectados, y conserva un registro de evidencia y decisiones sin marcar cumplimiento por la mera existencia de un documento.

## Orden de trabajo y primera revisión común

1. Acordar marcos, ubicación de pieza y base, espacio disponible como supuesto de estudio e interfaz inicial del cabezal. La probeta sigue siendo una bipirámide de base cuadrada con doce aristas de 0,05 m y ocho caras cerradas; el espesor y la secuencia de apoyo, unión y cierre siguen abiertos.
2. Avanzar en paralelo: Shelton con Capella, Andres con los datos prioritarios, Nicolas y Gabriel con el CAD y Eidan con la formulación del modelo, control y medición. Evitar bloquear todo el CAD por fichas todavía pendientes.
3. Revisar una primera versión del ensamble con componentes ubicados, medidas principales, seis ejes definidos, recorrido propuesto de tubos y espacio reservado para óptica y metrología. Una vista estática no demuestra ausencia de colisiones durante el movimiento.
4. Usar esa versión para cálculos y simulación progresiva: línea, esquina y cara antes de evaluar toda la bipirámide. Revisar límites, formación de caras y cierre final; devolver al CAD las correcciones necesarias.
5. Incorporar al PDR la configuración preliminar y su justificación, y continuar hacia planos, tolerancias y análisis de mayor detalle. Las fechas internas de entregas por integrante se acuerdan con su disponibilidad; no se fijan aquí compromisos individuales nuevos.

## Qué se reutiliza y cómo se verifica el avance

La misión, escenario, selección de componentes, requisitos, estimaciones, riesgos y plan PV01 a PV06 del SRR son la base existente. Capella está en desarrollo según Eidan; SolidWorks está elegido y el modelado se inicia. El presupuesto conserva su carácter preliminar y se revisa cuando el diseño cambie datos.

Cada entrega identifica responsable, archivos y revisión, entradas y fuentes, resultado, límites, pendientes y siguiente acción. Los criterios PDR/ADV se enlazan según corresponda; el estado se actualiza únicamente con evidencia. Las cuestiones de UV/térmica, contención, fabricación de caras y metrología permanecen visibles y se asignan explícitamente antes de evaluar sus resultados.

Para el PDR se reúne diseño preliminar, arquitectura, interfaces, cálculos iniciales y planes de verificación; para el desarrollo avanzado se profundiza en fabricación, tolerancias, dinámica y simulación. La entrega PDR prevista es el 28 de noviembre y la revisión el 5 de diciembre de 2026. La final del 19 de diciembre depende de la selección del programa. El formato oficial PDR debe comprobarse al publicarse.

## Trazabilidad

Fuente del reparto: instrucciones de Eidan del 24 de octubre de 2026. Este acuerdo actualiza responsables y prioridades; no comunica compras, ensayos ni prestaciones verificadas.

[Equipo activo](../management/equipo.md) · [Criterios técnicos PDR y ADV](objetivos_pdr_y_desarrollo.md) · [Registro CAD](../cad/registro.md) · [Requisitos](requisitos.md) · [Software](software_simulacion.md).
