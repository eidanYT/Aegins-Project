# M2 Material y extrusión

Participante de referencia: **Gabriel Hurtado Curi**. Estado de criterios nuevos: propuesta para revisión del equipo, 18 de octubre de 2026.

El módulo elige cómo alcanzar los resultados y aporta evidencia revisable. Interfaces: ICD-001, ICD-002, ICD-004 e ICD-005.

## Desarrollo avanzado

### ADV-M2-01 Cerrar la definición del circuito de resina

**Resultado y aceptación.** Referencia GE680, viproHEAD 5, boquilla de acero inoxidable, línea PTFE protegida de UV y sensor de presión Kulite. Documentar variantes, diámetros interiores, longitudes, volumen muerto, compatibilidad, almacenamiento y limpieza. SDS/TDS e inventario de peligros y emisiones con fuentes; no atribuir ausencia de emisiones sin datos.

**Evidencia de cierre.** Esquema fluídico, BOM y fichas; las variantes pendientes tienen criterio y fecha de selección.

### ADV-M2-02 Dimensionar entrega y transitorios

**Resultado y aceptación.** Derivar caudales de aristas y caras del perfil de velocidad, sección y espesor; estimar pérdidas de presión y límites del dosificador, considerando viscosidad, temperatura, compresibilidad, burbujas, arranque, parada y presión residual.

**Evidencia de cierre.** Modelo Q(t), presión y consumo; ventana de operación propuesta y plan de caracterización PV01.

### ADV-M2-03 Correlacionar un modelo del extrusor

**Resultado y aceptación.** Modelo de entrega con retardo, cumplimiento del caudal, presión, elasticidad y rezume, ajustado a datos de banco cuando estén disponibles. La ley newtoniana solo se usa dentro de su aplicabilidad; calibrar reología dependiente de cizalla y temperatura si se necesita.

**Evidencia de cierre.** Curvas y residuos de ajuste, incertidumbre y casos de velocidad variable, esquina, pausa, reinicio, atasco y cartucho agotado.

### ADV-M2-02 Representar deposición y construcción de la pieza

**Resultado y aceptación.** Construcción incremental del material con caudal real estimado y pose del TCP, diferenciando aristas, pistas de caras, uniones y cierre. Conservar volumen integrado y declarar modelos de sección, contracción y apoyo. Progresar de cordón geométrico a modelo físico solo si una decisión lo requiere.

**Evidencia de cierre.** Mapa de cobertura, espesor, volumen, vacíos/solapes y material desperdiciado; contraste con probetas futuras junto con M3 y M5.

## Registro del resultado

Mantener en [propuesta](propuesta.md) las decisiones, fuentes y evidencias de cada ID. Toda cifra requiere unidades, condiciones y procedencia; los umbrales pendientes se cierran antes de declarar cumplimiento. [Requisitos comunes](../../system/requisitos.md) · [Interfaces](../../interfaces/README.md) · [Equipo](../../management/equipo.md).
