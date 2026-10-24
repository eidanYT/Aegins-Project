# Requisitos de misión sistema PDR y desarrollo avanzado

Reparto operativo actualizado el 24 de octubre: [equipo activo y entregables](reparto_trabajo_2026-10-24.md). Los IDs PDR/ADV conservan su alcance técnico; su cobertura puede proceder de entregas compartidas. Eidan asume M5 y el modelo matemático; Shelton elabora Capella con coordinación de Eidan. Un cambio de responsable no cambia el estado de evidencia.

Fuente de la línea base MIS-SRR y SYS-SRR: report inglés revisión 5, con traducción española. Las selecciones documentadas son referencias de diseño. Los criterios nuevos PDR/ADV son propuestas de aceptación del plan del 18 de octubre de 2026 y requieren revisión técnica. A análisis, I inspección, D demostración, T ensayo. No hay evidencia física nueva.

## Misión

| ID de misión | Requisito | Evidencia de aceptación y relación |
| --- | --- | --- |
| MIS-SRR-01 | Definir misión de fabricación contenida en estación tripulada y límites de alojamiento. | I: misión e interfaz acordadas; se relaciona con SYS-001 e INT-002. Escenario elegido; límites abiertos. |
| MIS-SRR-02 | Evaluar posición y orientación completa del cabezal 6R frente a orientación fija sobre tareas accesibles equivalentes. | A/I: protocolo de tarea equivalente, condiciones y métricas; se relaciona con SCI-001/002 y MOT-001. |
| MIS-SRR-03 | Proteger tripulación y alojamiento en operación, fallos y recuperación. | A/I/T: peligros revisados, material retenido y criterios de acceso/fallo verificados; se relaciona con INT-001, EXT-002 y SAF-001. |

## Sistema y equivalencia de identificadores

| ID SRR e ID previo | Requisito de sistema propuesto | Método y base de aceptación |
| --- | --- | --- |
| SYS-SRR-01<br>(SYS-001) | Mantener una misión de referencia y límites ambientales. | I: registro controlado y límites del alojamiento; Sistemas/M4. |
| SYS-SRR-02<br>(SCI-001) | Comparar orientación fija y variable con condiciones trazables. | I/A: tarea accesible equivalente, controles de exposición/material y réplicas; Sistemas/M5. |
| SYS-SRR-03<br>(SCI-002) | Definir métricas geométricas y de proceso con incertidumbre. | A/T: métricas, efecto científico e incertidumbre adecuada; M5. |
| SYS-SRR-04<br>(MOT-001) | Alcanzar trayectorias de posición y orientación con seis articulaciones actuadas y giro axial definido, dentro de límites articulares y de separación. | Verificación 6R pendiente con CAD, trayectoria continua y pruebas propias. |
| SYS-SRR-05<br>(MOT-002) | Mantener cargas y perturbaciones dentro de asignaciones. | A/T: dinámica y cargas de seis ejes, retención del sexto eje e interfaz con host; M1/M4. |
| SYS-SRR-06<br>(EXT-001) | Suministrar caudal de aristas y caras con transitorios controlados. | A/T: respuesta medida de presión/caudal en el rango derivado; M2. |
| SYS-SRR-07<br>(EXT-002) | Mantener material y presión dentro de límites del circuito. | I/A/T: compatibilidad, presión máxima creíble y ensayo de retención ante fallo; M2/M4. |
| SYS-SRR-08<br>(UV-001) | Entregar espectro e historia de exposición compatibles con el material. | A/T: mapa de irradiancia y criterios de gel, unión y curado final específicos; M3. |
| SYS-SRR-09<br>(THM-001) | Mantener temperatura y transferencia de calor dentro de límites. | A/T: modelo térmico con seis accionamientos, pérdidas de drivers y calor de motores; correlación y medidas de temperatura/calor al host; M3/M4. |
| SYS-SRR-10<br>(INT-001) | Retener líquidos, partículas y pieza en operación y fallos definidos. | A/T: verificación de barreras y acceso según inventario; M4. |
| SYS-SRR-11<br>(INT-002) | Respetar masa, envolvente, potencia, energía, calor y datos asignados. | I/A: presupuestos de seis ejes y siete nodos frente a ICD; pendientes con M4 y revisión antes de PDR. |
| SYS-SRR-12<br>(CTL-001) | Sincronizar seis consignas/lectores articulares, pose completa TCP y sensores de proceso con origen temporal y validez. | A/D/T: presupuesto temporal, relojes y latencia medida; M5. |
| SYS-SRR-13<br>(MET-001) | Resolver diferencias geométricas relevantes con cobertura documentada. | A/T: comprobación de calibración independiente e incertidumbre propagada; M5. |
| SYS-SRR-14<br>(SAF-001) | Alcanzar y mantener la condición física revisada para cada fallo. | A/D/T: pruebas por fallo, pérdida de energía y recuperación autorizada; M4/M5. |
| SYS-SRR-15<br>(DOC-001) | Entregar paquete SRR y visualización trazables. | I: lista de formato/lineamientos, fuentes, modelos versionados y revisión; Sistemas. |
| SYS-SRR-16 | Detectar cierre y bloquear físicamente UV si se pierde permiso. | I/A/T: análisis de fallos e inyección; PV02. M4/M5. |
| SYS-SRR-17 | Vigilar presión diferencial cámara/cabina para verificar la condición de contención tipo MSG elegida y detectar señales inválidas. | A/T: rango, incertidumbre, umbral y respuesta por definir; PV02/PV04. M4. |
| SYS-SRR-18 | Verificar el sellado elegido mediante prueba aislada de mantenimiento de presión tipo MSG antes de operar; definir acceso seguro. | A/T: protocolo, volumen, temperatura, sensibilidad y fuga máxima por definir; PV02. M4. |
| SYS-SRR-19 | Limitar exposición UV y conservar observación útil a través de paneles. | A/T: límite de exposición a acordar; espectro, envejecimiento y unión película panel; PV03. M3/M4. |
| SYS-SRR-20 | Demostrar caudal, retención de emisiones y respuesta a filtro cargado o ventilador perdido. | A/T: emisiones y curvas reales; criterios por definir; PV01/PV04. M4. |

## Objetivos y aceptación por módulo

El texto normativo y la evidencia exigida están en [objetivos PDR y desarrollo avanzado](../system/objetivos_pdr_y_desarrollo.md). Los IDs siguientes amplían los requisitos del SRR; no los renumeran. Registrar por ID evidencia, commit, método, resultado, versión y revisor.

| ID | Resultado | Referencia técnica por módulo | Estado |
| --- | --- | --- | --- |
| PDR-SYS-01 | Entregar el paquete PDR integrado | Eidan Ajahuana Quiroz | Criterio propuesto; evidencia pendiente |
| PDR-SYS-02 | Gestionar decisiones y cierre por evidencia | Eidan Ajahuana Quiroz | Criterio propuesto; evidencia pendiente |
| ADV-SYS-01 | Entregar arquitectura de sistema trazable | Shelton Yauri Huamani; coordinación Eidan | Criterio propuesto; evidencia pendiente |
| ADV-SYS-02 | Consolidar el expediente avanzado y la demostración final | Eidan Ajahuana Quiroz | Criterio propuesto; evidencia pendiente |
| ADV-SYS-03 | Decidir si procede software propio e IA | Eidan Ajahuana Quiroz | Criterio propuesto; evidencia pendiente |
| PDR-M1-01 | Definir el brazo 6R y su geometría | Nicolas Quispe Papuico | Criterio propuesto; evidencia pendiente |
| PDR-M1-02 | Justificar capacidad y cargas | Nicolas Quispe Papuico | Criterio propuesto; evidencia pendiente |
| PDR-M1-03 | Demostrar factibilidad de trayectoria | Nicolas Quispe Papuico | Criterio propuesto; evidencia pendiente |
| ADV-M1-01 | Entregar CAD apto para fabricación y análisis | Nicolas Quispe Papuico | Criterio propuesto; evidencia pendiente |
| ADV-M1-02 | Cerrar dinámica y elementos finitos | Nicolas Quispe Papuico | Criterio propuesto; evidencia pendiente |
| ADV-M1-03 | Ejecutar movimiento de impresión verificable | Nicolas Quispe Papuico | Criterio propuesto; evidencia pendiente |
| PDR-M2-01 | Cerrar la definición del circuito de resina | Gabriel Hurtado Curi | Criterio propuesto; evidencia pendiente |
| PDR-M2-02 | Dimensionar entrega y transitorios | Gabriel Hurtado Curi | Criterio propuesto; evidencia pendiente |
| PDR-M2-03 | Justificar formación de caras y contención del material | Gabriel Hurtado Curi | Criterio propuesto; evidencia pendiente |
| ADV-M2-01 | Correlacionar un modelo del extrusor | Gabriel Hurtado Curi | Criterio propuesto; evidencia pendiente |
| ADV-M2-02 | Representar deposición y construcción de la pieza | Gabriel Hurtado Curi | Criterio propuesto; evidencia pendiente |
| PDR-M3-01 | Definir óptica y ventana de curado | Andres Zelada Solano | Criterio propuesto; evidencia pendiente |
| PDR-M3-02 | Cerrar balance térmico preliminar y medición | Andres Zelada Solano | Criterio propuesto; evidencia pendiente |
| PDR-M3-03 | Especificar protección UV y fallos | Andres Zelada Solano | Criterio propuesto; evidencia pendiente |
| ADV-M3-01 | Acoplar exposición y curado al movimiento | Andres Zelada Solano | Criterio propuesto; evidencia pendiente |
| ADV-M3-02 | Correlacionar térmica y protección óptica | Andres Zelada Solano | Criterio propuesto; evidencia pendiente |
| PDR-M4-01 | Definir contención y acceso | Shelton Yauri Huamani | Criterio propuesto; evidencia pendiente |
| PDR-M4-02 | Cerrar presupuestos e interfaces del host | Shelton Yauri Huamani | Criterio propuesto; evidencia pendiente |
| PDR-M4-03 | Preparar AIV y ambiente de lanzamiento | Shelton Yauri Huamani | Criterio propuesto; evidencia pendiente |
| ADV-M4-01 | Cerrar ensamble e interfaces físicas | Shelton Yauri Huamani | Criterio propuesto; evidencia pendiente |
| ADV-M4-02 | Evaluar respuesta a lanzamiento y elaborar la campaña de ensayo | Shelton Yauri Huamani | Criterio propuesto; evidencia pendiente |
| ADV-M4-03 | Modelar aire, emisiones y fallos de contención | Shelton Yauri Huamani | Criterio propuesto; evidencia pendiente |
| PDR-M5-01 | Definir control, señales y estados | Eidan Ajahuana Quiroz | Criterio propuesto; evidencia pendiente |
| PDR-M5-02 | Cerrar criterio geométrico y presupuesto de error | Eidan Ajahuana Quiroz | Criterio propuesto; evidencia pendiente |
| PDR-M5-03 | Dimensionar cómputo, almacenamiento y energía | Eidan Ajahuana Quiroz | Criterio propuesto; evidencia pendiente |
| ADV-M5-01 | Integrar simulación de brazo extrusor y UV | Eidan Ajahuana Quiroz | Criterio propuesto; evidencia pendiente |
| ADV-M5-02 | Verificar interfaces y recuperación | Eidan Ajahuana Quiroz | Criterio propuesto; evidencia pendiente |
| ADV-M5-03 | Demostrar calidad y comparación de impresión | Eidan Ajahuana Quiroz | Criterio propuesto; evidencia pendiente |

## Asignación de umbrales

Cada umbral de error, orientación, velocidad, par, presión, fuga, UV, temperatura, latencia, vibración y holgura se cierra con fundamento antes de declarar cumplimiento. Registrar dueño y fecha en [pendientes](pendientes.md), transferir valor a ICD y modelos, y conservar sensibilidad e incertidumbre. Un cero o una celda vacía no sustituyen un valor desconocido.
