# M3 UV y térmica

Participante de referencia: **Andres Zelada Solano**. Estado de criterios nuevos: propuesta para revisión del equipo, 18 de octubre de 2026.

El módulo elige cómo alcanzar los resultados y aporta evidencia revisable. Interfaces: ICD-001, ICD-002, ICD-004 e ICD-005.

### PDR-M3-01 Definir óptica y ventana de curado

**Resultado y aceptación.** Nichia NVSU233B U365 a 365 nm, cuatro emisores de referencia; geometría y distancia de iluminación vinculadas a orientación, caudal y velocidad. La irradiancia en resina se calcula o mide; la potencia óptica del LED no la sustituye. Establecer criterios de gel, unión y curado final con GE680.

**Evidencia de cierre.** Mapa de irradiancia/dosis propuesto y plan de caracterización; sensibilidad a sombras e incidencia en las ocho caras.

### PDR-M3-02 Cerrar balance térmico preliminar y medición

**Resultado y aceptación.** Placa conductora y straps, Pt100 y fotodiodo SiC SG01D como referencias. Separar calor de LED, driver, motores, electrónica, absorción y reacción; definir ruta al host. Comprobar responsividad y margen de señal SG01D a 365 nm antes de confirmar variante.

**Evidencia de cierre.** Balance con incertidumbre, temperaturas límite por material y ubicación de sensores; PV03 e ICD-004.

### PDR-M3-03 Especificar protección UV y fallos

**Resultado y aceptación.** Definir inhibición física de UV ante puerta abierta, presión inválida o pérdida de permiso y el tratamiento del calor residual. Evaluar Lexan, Rosco R3114, adhesivo y Acktar a 365 nm, envejecimiento y limpieza.

**Evidencia de cierre.** Esquema de interbloqueo con M4/M5 y plan de transmisión/exposición PV03; límites de seguridad pendientes de fuente aplicable.

## Desarrollo avanzado

### ADV-M3-01 Acoplar exposición y curado al movimiento

**Resultado y aceptación.** Integrar irradiancia sobre cada tramo depositado usando pose, sombras, velocidad y estado temporal del material. Relacionar dosis con gel, conversión, unión y contracción mediante datos de la formulación; identificar resultados solo cualitativos cuando falten datos.

**Evidencia de cierre.** Mapa temporal de dosis y estado de curado con incertidumbre; zonas deficientes y excesivas trazadas al plan de impresión.

### ADV-M3-02 Correlacionar térmica y protección óptica

**Resultado y aceptación.** Modelo térmico transitorio de cabezal, resina, electrónica y recinto con caminos conductivos, radiación y convección interna justificada. Incorporar peor caso y fallos, transmisión real del panel y calibración de sensores.

**Evidencia de cierre.** Temperaturas, flujo al host y exposición exterior frente a límites acordados, convergencia y plan/datos de correlación PV03.

## Registro del resultado

Mantener en [propuesta](propuesta.md) las decisiones, fuentes y evidencias de cada ID. Toda cifra requiere unidades, condiciones y procedencia; los umbrales pendientes se cierran antes de declarar cumplimiento. [Requisitos comunes](../../system/requisitos.md) · [Interfaces](../../interfaces/README.md) · [Equipo](../../management/equipo.md).
