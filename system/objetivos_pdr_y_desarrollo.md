# Objetivos de FORGE UG para el PDR y el desarrollo avanzado

## Organización vigente desde el 24 de octubre de 2026

El [reparto del equipo activo](reparto_trabajo_2026-10-24.md) actualiza las responsabilidades y primeras entregas: Shelton lleva Capella e interfaces; Andres, componentes y adaptaciones; Nicolas y Gabriel, CAD preliminar con apoyo de Eidan; Eidan, modelos matemáticos, factibilidad integrada, control, metrología e integración del PDR. Isaac ya no participa.

Los objetivos PDR/ADV se mantienen como criterios técnicos y se cubren con entregas compartidas, sin exigir tres paquetes nuevos por integrante. La entrega CAD describe geometría y distribución; los cálculos y simulación se desarrollan con Eidan y el apoyo de los especialistas. Capella se desarrolla desde ahora y aporta al PDR, aunque su criterio completo conserve el ID ADV-SYS-01. SolidWorks está elegido; la herramienta de simulación integrada sigue por decidir. Los estados de cumplimiento requieren evidencia.

Equipo AEGINS · Brazo de seis ejes · 18 de octubre de 2026

[Documento independiente en Drive](https://docs.google.com/document/d/1inMmWbgGPaS9qYh_PXo-mJs9juY8hWAyJhXr5WGR60M/edit)

El trabajo se organiza en dos resultados fundamentales: presentar un diseño preliminar integrado y defendible en el PDR, y desarrollar un expediente técnico con CAD dimensionado, modelos y simulación de impresión de mayor profundidad. Cada módulo elige sus métodos y organiza su trabajo para cumplir los requisitos, respetando las interfaces comunes y aportando evidencia revisable.

La probeta de referencia es una bipirámide de base cuadrada, doce aristas de 0,05 m y ocho caras cerradas. El brazo tiene seis articulaciones revolutas y controla posición y orientación completas del TCP. El espesor y las tolerancias de fabricación y de la pieza se deben cerrar mediante dimensionamiento y presupuesto de errores.

El escenario es una cámara intravehicular en estación tripulada en órbita baja. ISS es referencia ambiental, sin alojamiento contratado. El CAD completo, los ensayos físicos y la aceptación de vuelo siguen sujetos a desarrollo y evidencia.

## Cómo se acepta un objetivo

Cada requisito se registra con ID, módulo, criterio, método A análisis, I inspección, D demostración o T ensayo, evidencia, versión y revisor. Los resultados se expresan como cumple dentro del alcance, no cumple o inconcluso. TBD significa dato por determinar; TBR es propuesta por revisar. Un dato SELECCIONADO es una referencia de diseño, no prueba de prestación física ni compra realizada.

Los umbrales de exactitud, rigidez, presión, fuga, dosis, temperatura, latencia, holgura y vibración requieren valores numéricos justificados antes de declarar cumplimiento. Se asignan a requisitos y a ICD, con fecha de cierre. Una simulación con entradas provisionales conserva esa condición.

## Módulos y participantes

| Módulo | Referente para revisión técnica | Colaboración para el cierre |
| --- | --- | --- |
| M1 Movimiento y estructura del brazo | Nicolas Quispe Papuico | ICD-001, ICD-002, ICD-003 e ICD-004 |
| M2 Material y extrusión | Gabriel Hurtado Curi | ICD-001, ICD-002, ICD-004 e ICD-005 |
| M3 UV y térmica | Andres Zelada Solano | ICD-001, ICD-002, ICD-004 e ICD-005 |
| M4 Cámara e integración | Shelton Yauri Huamani | ICD-002, ICD-003, ICD-004 e ICD-005 |
| M5 Control y metrología | Eidan Ajahuana Quiroz | ICD-001, ICD-002, ICD-003, ICD-004 e ICD-005 |
| Sistemas y coordinación | Eidan Ajahuana Quiroz | Los cinco módulos y revisión independiente |

La tabla conserva las referencias de módulos con M5 actualizado a Eidan. Para las responsabilidades de ejecución y colaboración se aplica el reparto del 24 de octubre enlazado arriba. Cualquier integrante puede contribuir a otro módulo y los afectados revisan sus interfaces.

## Trabajo 1 PDR

**Objetivo final.** Entregar el diseño preliminar 6R integrado con requisitos claros, selección sustentada, arquitectura, CAD preliminar, cálculos, presupuestos, peligros y estrategia de verificación. La defensa debe distinguir resultados ya disponibles de trabajo pendiente y responder las observaciones del jurado.

**Hitos confirmados.** Entrega el 28 de noviembre de 2026, PDR el 5 de diciembre de 2026 y gran final el 19 de diciembre de 2026 si el equipo es seleccionado. La fecha de entrega se deriva de la indicación de entregar una semana antes. Verificar el formato específico PDR al publicarse; no heredar automáticamente los límites de páginas o exposición del SRR.


### PDR-SYS-01 Entregar el paquete PDR integrado

**Resultado y aceptación.** Informe y especificaciones del diseño 6R, requisitos verificables con trazabilidad, CAD preliminar, ICD-001 a ICD-005, presupuestos, riesgos, respuesta a jurado, AIV, cronograma, negocio y fuentes. Cumplir la convocatoria PDR vigente; los límites de 30 páginas y 10 minutos del SRR no se transfieren sin confirmación.

**Evidencia de cierre.** Lista de entrega con versiones, responsables de aceptación, pendientes críticos y revisión cruzada; congelación para entrega el 28 de noviembre de 2026.

### PDR-SYS-02 Gestionar decisiones y cierre por evidencia

**Resultado y aceptación.** Cada requisito tiene módulo, criterio numérico o condición de aceptación, método A/I/D/T, evidencia, estado y revisor. Cada TBD crítico tiene dueño y fecha; si impide una conclusión se declara inconclusa. El equipo elige cómo alcanzar el objetivo dentro de sus interfaces.

**Evidencia de cierre.** Matriz de cumplimiento y registro de decisiones; conformidades explícitas de los módulos afectados, sin convertir revisión documental en ensayo.

## M1 Movimiento y estructura del brazo para el PDR

Participante de referencia: Nicolas Quispe Papuico.

### PDR-M1-01 Definir el brazo 6R y su geometría

**Resultado y aceptación.** Ensamble preliminar con seis articulaciones revolutas, marcos base, pieza, brida y TCP, longitudes, offsets, límites de posición, velocidad y aceleración, y masas e inercias con procedencia. Cada dimensión crítica tiene valor y unidad o pendiente con fecha de cierre. La orientación incluye giro axial.

**Evidencia de cierre.** CAD preliminar, tabla cinemática y memoria FK/IK; revisión de M2, M3, M4 y M5.

### PDR-M1-02 Justificar capacidad y cargas

Ejecución actual: Eidan elabora el modelo matemático con la geometría de Nicolas y Gabriel y su revisión técnica.

**Resultado y aceptación.** Comparación 6R frente a movimiento cartesiano para la misma tarea accesible; dimensionamiento de par continuo y pico por articulación, rigidez, holgura y cargas de base/cabezal, incluyendo gravedad de ensayo terrestre y condición orbital por separado.

**Evidencia de cierre.** Memoria de cálculo y selección por eje; hipótesis de fricción, reductora y ciclo declaradas.

### PDR-M1-03 Demostrar factibilidad de trayectoria

Ejecución actual: Eidan integra el análisis de trayectoria; Nicolas y Gabriel aportan CAD, marcos y datos del mecanismo.

**Resultado y aceptación.** Trayectoria preliminar continua con posición y orientación completas, traslados sin extrusión, aproximaciones y salida. Identificar singularidades, colisiones y torsión finita de tubos; cualquier tramo no resuelto queda identificado, con impacto en la probeta.

**Evidencia de cierre.** Simulación 6R versionada, cobertura y lista de tramos factibles y pendientes; un vídeo aislado no cierra el criterio.

## M2 Material y extrusión para el PDR

Participante de referencia: Gabriel Hurtado Curi.

### PDR-M2-01 Cerrar la definición del circuito de resina

**Resultado y aceptación.** Referencia GE680, viproHEAD 5, boquilla de acero inoxidable, línea PTFE protegida de UV y sensor de presión Kulite. Documentar variantes, diámetros interiores, longitudes, volumen muerto, compatibilidad, almacenamiento y limpieza. SDS/TDS e inventario de peligros y emisiones con fuentes; no atribuir ausencia de emisiones sin datos.

**Evidencia de cierre.** Esquema fluídico, BOM y fichas; las variantes pendientes tienen criterio y fecha de selección.

### PDR-M2-02 Dimensionar entrega y transitorios

Ejecución actual: Eidan desarrolla el modelo con apoyo de Gabriel y los datos de circuito y componentes.

**Resultado y aceptación.** Derivar caudales de aristas y caras del perfil de velocidad, sección y espesor; estimar pérdidas de presión y límites del dosificador, considerando viscosidad, temperatura, compresibilidad, burbujas, arranque, parada y presión residual.

**Evidencia de cierre.** Modelo Q(t), presión y consumo; ventana de operación propuesta y plan de caracterización PV01.

### PDR-M2-03 Justificar formación de caras y contención del material

**Resultado y aceptación.** Secuencia de anclaje, deposición, unión entre pistas y cierre de ocho caras; identificar soportes, contracción, estabilidad antes de curar y criterios de calidad. Incluir atasco, fuga, cebado y fin de cartucho.

**Evidencia de cierre.** Protocolo de probeta con métricas y criterios propuestos; revisión M1/M3/M4/M5 e integración en PV01/PV02.

## M3 UV y térmica para el PDR

Participante de referencia: Andres Zelada Solano.

### PDR-M3-01 Definir óptica y ventana de curado

**Resultado y aceptación.** Nichia NVSU233B U365 a 365 nm, cuatro emisores de referencia; geometría y distancia de iluminación vinculadas a orientación, caudal y velocidad. La irradiancia en resina se calcula o mide; la potencia óptica del LED no la sustituye. Establecer criterios de gel, unión y curado final con GE680.

**Evidencia de cierre.** Mapa de irradiancia/dosis propuesto y plan de caracterización; sensibilidad a sombras e incidencia en las ocho caras.

### PDR-M3-02 Cerrar balance térmico preliminar y medición

**Resultado y aceptación.** Placa conductora y straps, Pt100 y fotodiodo SiC SG01D como referencias. Separar calor de LED, driver, motores, electrónica, absorción y reacción; definir ruta al host. Comprobar responsividad y margen de señal SG01D a 365 nm antes de confirmar variante.

**Evidencia de cierre.** Balance con incertidumbre, temperaturas límite por material y ubicación de sensores; PV03 e ICD-004.

### PDR-M3-03 Especificar protección UV y fallos

**Resultado y aceptación.** Definir inhibición física de UV ante puerta abierta, presión inválida o pérdida de permiso y el tratamiento del calor residual. Evaluar Lexan, Rosco R3114, adhesivo y Acktar a 365 nm, envejecimiento y limpieza.

**Evidencia de cierre.** Esquema de interbloqueo con M4/M5 y plan de transmisión/exposición PV03; límites de seguridad pendientes de fuente aplicable.

## M4 Cámara e integración para el PDR

Participante de referencia: Shelton Yauri Huamani.

### PDR-M4-01 Definir contención y acceso

**Resultado y aceptación.** Cámara tipo MSG con base 6061, paneles Lexan, película R3114 y acabado opaco Acktar. Circuito de aspiración, retorno y referencia filtrada HEPA/carbón, tres U51 con dos activos y uno de reserva; HM para cierre y sensor diferencial cámara/cabina. Diferenciar cierre de puerta, estanqueidad y depresión.

**Evidencia de cierre.** CAD preliminar y P&ID del aire; procedimientos de prueba aislada de presión, acceso y cambio de filtros PV02/PV04.

### PDR-M4-02 Cerrar presupuestos e interfaces del host

**Resultado y aceptación.** Sumar BOM, masa, envolvente, potencia por modo, picos, energía, calor, datos y costes de los cinco módulos sin doble conteo. Identificar cada partida no cuantificada y el responsable de cerrarla; 28 V y eficiencias son supuestos hasta aceptar el ICD del host.

**Evidencia de cierre.** Presupuesto trazable con reservas justificadas y lista de incompatibilidades/pendientes; no aceptar un subtotal parcial como total.

### PDR-M4-03 Preparar AIV y ambiente de lanzamiento

**Resultado y aceptación.** Definir montaje, configuración retenida para transporte, carga de material y límites del proveedor. Plan de verificación de vibración, EMC, radiación, materiales, incendio y contención, con instalaciones, instrumentación y costes pendientes identificados.

**Evidencia de cierre.** Matriz AIV, análisis de peligros y protocolo PV02/PV04/PV06 con criterios y estado de evidencia.

## M5 Control y metrología para el PDR

Participante de referencia: Eidan Ajahuana Quiroz.

### PDR-M5-01 Definir control, señales y estados

**Resultado y aceptación.** Arquitectura GR740, SAMRH71, RTG4, seis EPOS4 y CAN para control; imágenes CASPEX por interfaz y buffer dimensionados por separado. Definir lazos, cadencias, relojes, latencia, validez y secuencia nominal/fallo. La seguridad física no depende solo del computador.

**Evidencia de cierre.** Arquitectura de software/hardware y diccionario ICD; estados con permisos, timeouts y recuperación autorizada.

### PDR-M5-02 Cerrar criterio geométrico y presupuesto de error

**Resultado y aceptación.** Definir error de posición y orientación TCP, eRMS de pieza, desviación máxima, espesor/diámetro, cobertura, muestras inválidas e incertidumbre. Separar error de máquina, proceso, tiempo y medición. Fijar valores numéricos justificados antes de aceptar resultados de diseño.

**Evidencia de cierre.** Presupuesto de errores y calibración a través de ventanas reales; comparación de orientación fija/variable con controles equivalentes.

### PDR-M5-03 Dimensionar cómputo, almacenamiento y energía

**Resultado y aceptación.** Presupuesto CPU, memoria, imágenes, telemetría y alimentación con ECC/estrategia de fallos/radiación. UT8MR2M8 de 2 MB se reserva a estados y parámetros; no se da por suficiente para imágenes. Resolver compatibilidad de sensores, encoders, controladores y buses.

**Evidencia de cierre.** Cronograma de tareas y tráfico, memoria por función y matriz de compatibilidad; TSIM es apoyo de software y no evidencia de latencia física.

## Trabajo 2 Desarrollo avanzado y demostración final

**Objetivo final.** Disponer de un modelo digital coherente del brazo real 6R y de su cámara, con planos y tolerancias, dinámica, análisis estructural y de lanzamiento, arquitectura trazable e impresión simulada con movimiento, caudal y UV coordinados. La demostración incluye la bipirámide de referencia y una segunda geometría para mostrar que el método puede extenderse.

La meta para la final es presentar el avance avanzado que esté sustentado y sea reproducible. Los ensayos físicos costosos, la calificación de vuelo y el desarrollo de IA requieren recursos y puertas de decisión propios; su ausencia no impide cerrar el paquete documental PDR si queda declarada y planificada.


## M1 Movimiento y estructura del brazo en desarrollo avanzado

Participante de referencia: Nicolas Quispe Papuico.

### ADV-M1-01 Entregar CAD apto para fabricación y análisis

**Resultado y aceptación.** Todas las piezas y uniones del brazo y cabezal están dimensionadas; planos con datums, ajustes, tolerancias geométricas y dimensionales funcionales, materiales y acabados, BOM, masas, centros de gravedad e inercias. El presupuesto de tolerancias se propaga al TCP. Exportar nativos y STEP, además de URDF/Xacro o formato equivalente, sin perder unidades ni marcos.

**Evidencia de cierre.** Planos y ensamble revisados; comparación entre CAD y modelo cinemático; cadena de tolerancias y procedimiento de calibración.

### ADV-M1-02 Cerrar dinámica y elementos finitos

**Resultado y aceptación.** Modelo dinámico 6R con masas e inercias del CAD, cargas de tubos y proceso; FEA estático, modal y respuesta al ambiente de lanzamiento aplicable en configuración bloqueada. Incluir contactos, tornillos, precarga, rodamientos y retención de articulaciones; demostrar convergencia y sensibilidad a rigidez y amortiguamiento.

**Evidencia de cierre.** Casos reproducibles, reacciones, deformación TCP, tensiones, modos y márgenes frente a criterios acordados. Revisión con M4 y correlación física futura.

### ADV-M1-03 Ejecutar movimiento de impresión verificable

**Resultado y aceptación.** Toda la secuencia aprobada de la bipirámide y una geometría adicional se ejecutan con límites articulares y de actuadores respetados, sin colisiones dentro de la resolución declarada y con holgura mínima aprobada. Se evalúan orientaciones completas, cambios de rama IK, singularidades y envolvente de tubos.

**Evidencia de cierre.** Trayectoria temporizada, q1 a q6, velocidades, aceleraciones, pares, error TCP/orientación y distancia mínima; M5 integra con extrusor y UV.

## M2 Material y extrusión en desarrollo avanzado

Participante de referencia: Gabriel Hurtado Curi.

### ADV-M2-01 Correlacionar un modelo del extrusor

**Resultado y aceptación.** Modelo de entrega con retardo, cumplimiento del caudal, presión, elasticidad y rezume, ajustado a datos de banco cuando estén disponibles. La ley newtoniana solo se usa dentro de su aplicabilidad; calibrar reología dependiente de cizalla y temperatura si se necesita.

**Evidencia de cierre.** Curvas y residuos de ajuste, incertidumbre y casos de velocidad variable, esquina, pausa, reinicio, atasco y cartucho agotado.

### ADV-M2-02 Representar deposición y construcción de la pieza

**Resultado y aceptación.** Construcción incremental del material con caudal real estimado y pose del TCP, diferenciando aristas, pistas de caras, uniones y cierre. Conservar volumen integrado y declarar modelos de sección, contracción y apoyo. Progresar de cordón geométrico a modelo físico solo si una decisión lo requiere.

**Evidencia de cierre.** Mapa de cobertura, espesor, volumen, vacíos/solapes y material desperdiciado; contraste con probetas futuras junto con M3 y M5.

## M3 UV y térmica en desarrollo avanzado

Participante de referencia: Andres Zelada Solano.

### ADV-M3-01 Acoplar exposición y curado al movimiento

**Resultado y aceptación.** Integrar irradiancia sobre cada tramo depositado usando pose, sombras, velocidad y estado temporal del material. Relacionar dosis con gel, conversión, unión y contracción mediante datos de la formulación; identificar resultados solo cualitativos cuando falten datos.

**Evidencia de cierre.** Mapa temporal de dosis y estado de curado con incertidumbre; zonas deficientes y excesivas trazadas al plan de impresión.

### ADV-M3-02 Correlacionar térmica y protección óptica

**Resultado y aceptación.** Modelo térmico transitorio de cabezal, resina, electrónica y recinto con caminos conductivos, radiación y convección interna justificada. Incorporar peor caso y fallos, transmisión real del panel y calibración de sensores.

**Evidencia de cierre.** Temperaturas, flujo al host y exposición exterior frente a límites acordados, convergencia y plan/datos de correlación PV03.

## M4 Cámara e integración en desarrollo avanzado

Participante de referencia: Shelton Yauri Huamani.

### ADV-M4-01 Cerrar ensamble e interfaces físicas

**Resultado y aceptación.** Ensamble total del brazo, cabezal, recinto, tubos, conectores, filtros y sensores con barrido de movimiento, acceso y mantenimiento. Incluir fijaciones, pasamuros, sellos, arnés y disipación, con tolerancias y cargas acordadas.

**Evidencia de cierre.** Revisión de interferencias y montaje, BOM conciliada, planos y masas/inercias verificadas documentalmente con cada módulo.

### ADV-M4-02 Evaluar respuesta a lanzamiento y elaborar la campaña de ensayo

**Resultado y aceptación.** Junto con M1, evaluar configuración bloqueada con espectro de base y cargas del proveedor; respuesta modal, seno, vibración aleatoria por PSD y choque cuando aplique. Identificar respuesta de paneles, fijaciones, electrónica, depósitos y filtros. Proponer instrumentación, útiles, límites y pruebas funcionales antes y después.

**Evidencia de cierre.** Margen por modo de fallo, RMS y picos con factor justificado, sensibilidades y plan de correlación/ensayo. Sin proveedor: estudio paramétrico; aptitud de vuelo permanece pendiente.

### ADV-M4-03 Modelar aire, emisiones y fallos de contención

**Resultado y aceptación.** Balance por especie con generación, fugas, bypass, saturación y filtros cargados; punto operativo de ventiladores y válvulas. Evaluar pérdida de soplador, fallo del sensor y pérdida total de energía; la retención física debe mantener el inventario peligroso.

**Evidencia de cierre.** Concentraciones y presión con incertidumbre, criterios de acceso y campaña PV02/PV04; HEPA no se considera prueba de retención de vapores.

## M5 Control y metrología en desarrollo avanzado

Participante de referencia: Eidan Ajahuana Quiroz.

### ADV-M5-01 Integrar simulación de brazo extrusor y UV

**Resultado y aceptación.** Un único reloj de simulación coordina seis articulaciones, trayectoria, caudal, presión, dosis, temperatura y material añadido. Separar comandos, estimaciones y mediciones. Modelos intercambian datos con unidades, marcos, secuencia, validez y latencia explícitos.

**Evidencia de cierre.** Escena reproducible de la bipirámide con doce aristas y ocho caras cerradas, más una segunda geometría, vídeo y logs temporales; estado de física/calibración declarado.

### ADV-M5-02 Verificar interfaces y recuperación

**Resultado y aceptación.** Ensayos de software en el lazo con emuladores de sensores/actuadores, retardos, jitter, pérdidas/reordenación, CRC/formato incorrecto, calibración inválida, atasco y fallo de energía. Pasar a hardware en el lazo cuando exista equipo. Distinguir emulación ROS del protocolo de vuelo.

**Evidencia de cierre.** Pruebas automáticas de contrato y de fallos con criterio temporal derivado del presupuesto, registro de eventos y trazabilidad a ICD-001/003/005.

### ADV-M5-03 Demostrar calidad y comparación de impresión

**Resultado y aceptación.** Reconstruir geometría simulada o medida sin usar los comandos como verdad de medición. Comparar orientación fija y variable en tareas accesibles a ambas, con registro de lote, exposición, apoyo y velocidad. Propagar incertidumbre y reportar fracasos.

**Evidencia de cierre.** Informe de error, espesor, cobertura, volumen y dosis; contraste de resultados con referencia independiente y conjunto de casos retenidos.

## Sistemas e integración del desarrollo avanzado

Participante de referencia: Eidan Ajahuana Quiroz.

### ADV-SYS-01 Entregar arquitectura de sistema trazable

Responsable de elaboración: Shelton Yauri Huamani. Eidan coordina la integración y la revisión del equipo. En desarrollo desde ahora y utilizable en el PDR.

**Resultado y aceptación.** Modelo en Capella/Arcadia o equivalente con contexto, actores, escenarios nominales y fallos, funciones, cadenas funcionales, componentes físicos/lógicos y asignaciones de requisitos e ICD. El modelo debe concordar con CAD, software, presupuestos y riesgos.

**Evidencia de cierre.** Archivo nativo, vistas exportadas y matriz requisito a función a componente a interfaz a evidencia, revisados por los cinco módulos.

### ADV-SYS-02 Consolidar el expediente avanzado y la demostración final

**Resultado y aceptación.** Reunir CAD dimensionado, modelos matemáticos, tolerancias, simulación integrada de impresión, análisis FEA/lanzamiento, presupuestos y resultados con versiones reproducibles. Indicar qué es cálculo, simulación, ensayo realizado y ensayo futuro; preparar demostración y valor del proyecto para el 19 de diciembre de 2026 si es finalista.

**Evidencia de cierre.** Paquete final con instrucciones de reproducción y límites; las actividades físicas de calificación siguen una hoja de ruta con recursos y criterios propios.

### ADV-SYS-03 Decidir si procede software propio e IA

**Resultado y aceptación.** Evaluar primero las herramientas existentes con el mismo caso 6R. Solo si quedan limitaciones documentadas y hay recursos, aprobar una extensión o software propio con importación geométrica, planificación, simulación y análisis. La IA sería una línea posterior para proponer trayectorias o parámetros, con restricciones deterministas y validación independiente.

**Evidencia de cierre.** Decisión de continuar o descartar con coste y alcance; antes de entrenar: datos trazables, partición de entrenamiento/validación/prueba sin fuga entre geometrías, comparación con planificador convencional, tasa de éxito, violaciones y revisión humana. Nunca autorizar ejecución física directa por salida de IA.

## Cómo simular la impresión con seis ejes

1. **Caso mínimo.** Línea, esquina y pista sobre una cara; después las doce aristas, la formación de caras y el cierre de la bipirámide. M1 y M2 definen soporte y secuencia con M3. Una malla cerrada de la pieza no demuestra que su fabricación sea posible.
2. **De CAD a trayectoria.** Importar la pieza y el robot dimensionado, fijar marcos, TCP y sujeción, generar curvas de deposición y orientaciones completas. Un slicer de capas planas no resuelve automáticamente el acceso no plano, las ocho caras o el giro de herramienta.
3. **Planificación 6R.** M1 y M5 resuelven IK/FK, continuidad, singularidades, límites de velocidad/aceleración/par, colisiones de robot, recinto y material ya construido, y torsión de tubos. Temporizar incluyendo aceleraciones, aproximación, reposicionamiento y pausas.
4. **Proceso sincronizado.** M2 aporta Q(t), presión, retardo y rezume; M3 aporta E(t), dosis, curado y temperatura. M5 intercambia esos datos bajo un reloj de simulación común y realimenta velocidades y estado de fallo. El dosificador es una variable de proceso adicional, no una séptima articulación del brazo.
5. **Material incremental.** Añadir cordones o volúmenes conforme a pose y caudal real estimado; registrar el material depositado para detectar colisiones y cobertura. Para pistas usar Q = ancho × espesor × velocidad y para cordón circular Q = π × diámetro² × velocidad / 4 como primeras aproximaciones; integrar dosis H = ∫E(t)dt. En v = 0, una parada exige tratar presión residual y curado, sin dividir por cero ni seguir extruyendo por defecto.
6. **Fidelidad física.** Empezar con cordones geométricos y modelos reducidos calibrables. Escalar a reología, superficie libre, unión o contracción y curado acoplado solo para preguntas concretas; una animación de cordones no predice estabilidad ni resistencia en microgravedad. Comparar gravedad terrestre, microgravedad y aceleraciones residuales dentro del alcance elegido.
7. **Demostración aceptada.** Publicar entradas, versiones, procedimiento, vídeo y registros sincronizados. Evaluar error TCP y orientación, restricciones, caudal/dosis, espesor, cobertura, volumen, tiempo y fallos. Las tolerancias se fijan y revisan antes de evaluar; declarar qué parte del proceso sigue sin validación física.

## Contratos de simulación de interfaces

El modelo intercambia tiempo monótono en segundos, secuencia, versión de esquema y configuración, marco, unidades, validez e incertidumbre. La pose usa metros y cuaternión normalizado con convención documentada; las articulaciones usan radianes. Mantener campos separados para commanded, estimated y measured. Indicar origen del reloj y transformación de tiempos; no usar hora de pared como sustituto del reloj de simulación.

ICD-001 coordina trayectoria, velocidad, Q, presión, irradiancia y estado; ICD-002 contiene marcos, límites 6R, TCP, masas, montaje y tubos; ICD-003 define adquisición, imágenes, calibración y tiempo; ICD-004 contiene potencia, calor, datos y límites del host; ICD-005 contiene permisos, fallos y recuperación. Las pruebas incluyen retraso, jitter, sensor obsoleto, dato inválido, pérdida de comunicación, puerta abierta, atasco, presión anómala, pérdida de soplador y energía.

Usar software en el lazo primero, luego procesador o hardware en el lazo cuando existan interfaces y equipos. Una red ROS de simulación no acredita por sí misma temporización ni comportamiento del CAN o del hardware de vuelo.


## Software recomendado y criterio de elección

La elección propuesta se debe confirmar con una prueba corta de importación del mismo CAD 6R y el mismo tramo de impresión. Comparar tiempo de preparación, soporte del brazo personalizado, orientación completa, acceso a señales, automatización, exportación y licencias disponibles. Fijar versiones compatibles y dependencias reproducibles; no se incluyen precios ni licencias supuestamente disponibles.

| Necesidad | Opción propuesta | Uso y límite |
|---|---|---|
| CAD y planos | SolidWorks elegido por el equipo el 24 de octubre de 2026 | Mantener una fuente nativa, exportar STEP y propiedades de masa; comprobar que el exportador del robot conserva marcos, ejes y unidades. Elegir por el ensamble real, planos y tolerancias. |
| Primera simulación de impresión robótica | RoboDK más slicer/CAM y modelo personalizado | Su documentación permite G-code y eventos de extrusor. Comprobar integración del brazo propio, postprocesador y orientación 6R; no asumir que un slicer convencional resuelve trayectorias no planas ni que el visor modele resina y curado. |
| Integración abierta y fallos | ROS 2, MoveIt 2, ros2_control y Gazebo mediante gz_ros2_control | MoveIt planifica trayectorias con restricciones y colisiones; Gazebo permite integrar controladores y modelos. Añadir el modelo de dosificación, cordones y UV: no vienen validados para GE680. Empezar en PC; no presupone portabilidad directa a GR740. |
| Dinámica y control con acceso institucional | MATLAB y Simulink con Simscape Multibody y Robotics System Toolbox | Importación URDF/CAD y simulación multicuerpo/control. Requiere toolboxes/licencias y revisión de propiedades importadas; el proceso de resina necesita modelo adicional. |
| Estructuras y lanzamiento | Ansys Mechanical si hay acceso; SimScale para estudiar modalidades disponibles | Modelo estático, modal y respuesta dinámica. Confirmar solver y licencia para PSD aleatoria, excitación de base y choque. No sustituir vibración aleatoria por solo un cálculo modal o armónico. |
| Extrusión y física de material | Modelo reducido propio y calibrado; COMSOL Polymer Flow para preguntas avanzadas | COMSOL ofrece modelos de flujo no newtoniano; la superficie libre, cinética de GE680 y acoplamiento UV requieren configuración, datos y módulos adecuados. Evitar CFD completo como primer entregable. |
| Arquitectura de sistema | Eclipse Capella con Arcadia | Contexto, escenarios, funciones y arquitectura lógica/física. Enlazar IDs de requisitos y contratos de ICD; no es simulador cinemático ni FEA. |

Ruta sugerida: una prueba de RoboDK para obtener pronto una secuencia visible y comprobar el robot personalizado; ROS 2/MoveIt/Gazebo si se necesita integrar señales, control, proceso y fallos con mayor flexibilidad. Si el equipo ya domina MATLAB y tiene acceso, Simulink/Simscape puede cubrir la integración dinámica. Mantener CAD, requisitos y archivos de parámetros comunes cualquiera que sea la elección.

### Software propio e IA como última instancia

Antes de desarrollar una plataforma completa, registrar qué requisito no cubre la solución existente y si basta un complemento o adaptador. La primera versión propia debe importar CAD/URDF, planificar una trayectoria determinista restringida y reproducirla con modelos de proceso y registros. La IA se estudia después como generador de propuestas de orientación, secuencia o parámetros a partir de geometría.

La puerta de entrenamiento exige datos de simulación y/o ensayos con procedencia, límites de validez y métricas. Reservar familias de geometrías para prueba, comparar con un planificador convencional y comprobar colisiones, límites, caudal, dosis y construcción antes de aceptar una propuesta. La recuperación y ejecución física mantienen autorización humana y controles independientes. Esta línea no es condición para el PDR ni compromiso de entrenar un modelo para diciembre.

### Fuentes técnicas de las recomendaciones

- [RoboDK y eventos del extrusor](https://robodk.com/doc/en/Robot-Machining-Robot-3D-Printing-Project.html).
- [MoveIt y planificación con restricciones](https://moveit.picknik.ai/main/doc/concepts/motion_planning.html).
- [Integración Gazebo y ros2_control](https://control.ros.org/rolling/doc/gz_ros2_control/doc/index.html). Esta página corresponde a desarrollo; seleccionar una combinación estable soportada para el proyecto.
- [MathWorks e importación CAD y URDF](https://www.mathworks.com/help/sm/ref/smimport.html).
- [Ansys Mechanical](https://ansys.synopsys.com/products/structures/ansys-mechanical) y [análisis de vibraciones de SimScale](https://www.simscale.com/simulations/vibration-analysis/).
- [COMSOL Polymer Flow](https://www.comsol.com/polymer-flow-module).
- [Capella y Arcadia](https://mbse-capella.org/).
- [NASA GEVS GSFC-STD-7000B](https://standards.nasa.gov/node/791): referencia metodológica de verificación ambiental; aplicar el perfil y criterios acordados con el proveedor y host reales.


## Condiciones para evaluar aptitud de lanzamiento

La configuración de lanzamiento debe incluir las seis articulaciones retenidas, cabezal, cartucho, fluidos, filtros, electrónica y cableado, con la base de montaje real. Separar cargas de ensayo terrestre de la operación en microgravedad. La ecuación estructural de excitación de base es M ẍ + C ẋ + K x = −M r a_base; evaluar condiciones de contorno, contactos y amortiguamiento con sus incertidumbres.

Los criterios de evaluación son tensiones y deformaciones admisibles, resistencia de uniones y fijaciones, márgenes de fluencia/rotura/pandeo/fatiga cuando corresponda, pérdida de precarga, desplazamientos relativos, modos y respuesta de componentes sensibles. Los factores de seguridad, PSD, niveles de seno, choque, duración y ejes deben proceder del proveedor o de una hipótesis de estudio declarada. Sin esos datos, la salida es sensibilidad paramétrica, no compatibilidad de lanzamiento.

La verificación exige convergencia de malla, comprobación de masas/reacciones, sensibilidad a contactos y correlación mediante inspección modal y campaña ambiental cuando exista hardware. Planificar comprobaciones funcionales y de calibración antes y después, instrumentación, útiles y criterios de interrupción. Además de vibración se requieren revisiones de materiales, incendio, contaminación, UV, radiación, EMC y host. Ningún resultado FEA aislado acredita lanzamiento o vuelo.


## Puertas de cierre y orden de integración

| Puerta | Condición de cierre | Integración |
|---|---|---|
| P0 Definición | Requisitos y métricas asignados, referencias seleccionadas, ICD y supuestos con revisión | Eidan con los cinco módulos |
| P1 Modelos de módulo | CAD y marcos compatibles, modelos individuales con entradas y unidades comprobadas | Cada módulo; M4 concilia recursos |
| P2 Impresión acoplada | Caso mínimo y bipirámide con reloj común, límites, fallos y registros | M1/M2/M3 aportan modelos; M5 integra; M4 entorno |
| P3 PDR | Paquete completo congelado y revisado para entregar el 28 de noviembre | Eidan coordina aceptación; todos revisan interfaces |
| P4 Final avanzada | Segunda geometría, tolerancias y análisis ampliados con evidencia reproducible | Todos según objetivos ADV; presentación si finalista |
| P5 Validación física y espacial | Ensayos financiados, correlación, interfaces y aceptación formal del host y proveedor | Campaña futura coordinada por sistemas y M4 |

El avance de modelos puede comenzar desde ahora. La profundidad avanzada se acuerda según recursos y riesgos, manteniendo una ruta mínima de demostración y una lista explícita de limitaciones. Cada cambio de geometría, hardware, material o criterio actualiza sus dependencias y evidencias.
## Base documental

El report inglés SRR, revisión 5 con archivo actualizado el 17 de octubre de 2026, fija las referencias de diseño y los presupuestos de estudio. Este plan incorpora la decisión de Eidan del 18 de octubre de 2026 de trabajar por requisitos y adoptar exclusivamente el brazo 6R. Los criterios nuevos del plan son propuestas de aceptación, pendientes de revisión de los módulos; las selecciones de referencia ya constan en el SRR.

- [Report inglés de referencia](https://docs.google.com/document/d/1sF6ue6xzVTxw11Q5jYj6G-STlRtV-LT6/edit).
- [Report español actualizado](https://docs.google.com/document/d/1tMreuYGo6GXU7-P4isbVbHghdLBRkpSi/edit).
- [Agenda SGAC](https://drive.google.com/file/d/15wp7T_g8LAdjV__cyXzAkniWXYBsE00b/view). Eidan confirmó el 18 de octubre que el año correcto es 2026; el 2027 impreso es un error de tipeo.
