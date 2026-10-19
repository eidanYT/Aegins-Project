# M1 Movimiento y estructura del brazo

Participante de referencia: **Nicolas Quispe Papuico**. Estado de criterios nuevos: propuesta para revisión del equipo, 18 de octubre de 2026.

El módulo elige cómo alcanzar los resultados y aporta evidencia revisable. Interfaces: ICD-001, ICD-002, ICD-003 e ICD-004.

### PDR-M1-01 Definir el brazo 6R y su geometría

**Resultado y aceptación.** Ensamble preliminar con seis articulaciones revolutas, marcos base, pieza, brida y TCP, longitudes, offsets, límites de posición, velocidad y aceleración, y masas e inercias con procedencia. Cada dimensión crítica tiene valor y unidad o pendiente con fecha de cierre. La orientación incluye giro axial.

**Evidencia de cierre.** CAD preliminar, tabla cinemática y memoria FK/IK; revisión de M2, M3, M4 y M5.

### PDR-M1-02 Justificar capacidad y cargas

**Resultado y aceptación.** Comparación 6R frente a movimiento cartesiano para la misma tarea accesible; dimensionamiento de par continuo y pico por articulación, rigidez, holgura y cargas de base/cabezal, incluyendo gravedad de ensayo terrestre y condición orbital por separado.

**Evidencia de cierre.** Memoria de cálculo y selección por eje; hipótesis de fricción, reductora y ciclo declaradas.

### PDR-M1-03 Demostrar factibilidad de trayectoria

**Resultado y aceptación.** Trayectoria preliminar continua con posición y orientación completas, traslados sin extrusión, aproximaciones y salida. Identificar singularidades, colisiones y torsión finita de tubos; cualquier tramo no resuelto queda identificado, con impacto en la probeta.

**Evidencia de cierre.** Simulación 6R versionada, cobertura y lista de tramos factibles y pendientes; un vídeo aislado no cierra el criterio.

## Desarrollo avanzado

### ADV-M1-01 Entregar CAD apto para fabricación y análisis

**Resultado y aceptación.** Todas las piezas y uniones del brazo y cabezal están dimensionadas; planos con datums, ajustes, tolerancias geométricas y dimensionales funcionales, materiales y acabados, BOM, masas, centros de gravedad e inercias. El presupuesto de tolerancias se propaga al TCP. Exportar nativos y STEP, además de URDF/Xacro o formato equivalente, sin perder unidades ni marcos.

**Evidencia de cierre.** Planos y ensamble revisados; comparación entre CAD y modelo cinemático; cadena de tolerancias y procedimiento de calibración.

### ADV-M1-02 Cerrar dinámica y elementos finitos

**Resultado y aceptación.** Modelo dinámico 6R con masas e inercias del CAD, cargas de tubos y proceso; FEA estático, modal y respuesta al ambiente de lanzamiento aplicable en configuración bloqueada. Incluir contactos, tornillos, precarga, rodamientos y retención de articulaciones; demostrar convergencia y sensibilidad a rigidez y amortiguamiento.

**Evidencia de cierre.** Casos reproducibles, reacciones, deformación TCP, tensiones, modos y márgenes frente a criterios acordados. Revisión con M4 y correlación física futura.

### ADV-M1-03 Ejecutar movimiento de impresión verificable

**Resultado y aceptación.** Toda la secuencia aprobada de la bipirámide y una geometría adicional se ejecutan con límites articulares y de actuadores respetados, sin colisiones dentro de la resolución declarada y con holgura mínima aprobada. Se evalúan orientaciones completas, cambios de rama IK, singularidades y envolvente de tubos.

**Evidencia de cierre.** Trayectoria temporizada, q1 a q6, velocidades, aceleraciones, pares, error TCP/orientación y distancia mínima; M5 integra con extrusor y UV.

## Registro del resultado

Mantener en [propuesta](propuesta.md) las decisiones, fuentes y evidencias de cada ID. Toda cifra requiere unidades, condiciones y procedencia; los umbrales pendientes se cierran antes de declarar cumplimiento. [Requisitos comunes](../../system/requisitos.md) · [Interfaces](../../interfaces/README.md) · [Equipo](../../management/equipo.md).
