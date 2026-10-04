# M5-Eidan — Control y metrología

**Responsable: Eidan.** [Volver al inicio](../../README.md) · [Contactos](../../management/equipo.md)

Eidan, propón cómo coordinar la operación del sistema, registrar datos y medir si la pieza impresa cumple las métricas elegidas.

## Get started: empieza ahora

**Primera entrega:** Una propuesta con métricas de la pieza, estados de operación, señales, instrumentación candidata y presupuesto inicial de errores. No necesitas esperar una fecha ni la respuesta de todos para preparar un borrador.

1. En GitHub, abre el selector de rama `main`, escribe `m5/propuesta-medicion` y selecciona **Create branch … from main**.
2. En esa rama, entra en `modules/control_metrologia_Eidan` y abre [propuesta.md](propuesta.md). Ya está creado.
3. Pulsa el lápiz (**Edit this file**), rellena la estructura siguiendo los pasos de abajo y usa **Preview**.
4. Guarda con **Commit changes** en tu rama y un mensaje que explique lo que avanzaste. Para continuar, vuelve a abrir esa misma rama.

La carpeta pertenece al mismo repositorio; no crees otro repositorio para tu módulo.

## Desarrolla tu propuesta

### 1. Qué medir

Abre [misión](../../system/mision.md) y [ejemplo de trazabilidad](../../system/ejemplo_trazabilidad.md). Propón cómo medir trayectoria del material, diámetro y continuidad, y cómo comparar orientación fija/variable. Usa supuestos TBR si la pieza todavía no está acordada con M1.

Escríbelo en el apartado **Geometría y comparación** de tu propuesta.

### 2. Cómo operar

Dibuja los estados: comprobación, preparación, impresión, finalización, inspección y fallo. Explica qué permite pasar de uno a otro y qué datos requieren. La parada depende también de presión/material y UV.

Escríbelo en el apartado **Alternativas** de tu propuesta.

### 3. Señales e instrumentación

Define comandos y lecturas con unidad, emisor/receptor, tiempo, validez y fuente. Propón cámaras, sensores y arquitectura de control por sus necesidades; diferencia comando, estimación y medida.

Escríbelo en el apartado **Modelo y verificación** de tu propuesta.

### 4. Error y registro

Identifica contribuciones de calibración, perspectiva, ruido y desfase temporal. Propón un ejemplo de registro claramente sintético y señala qué se comprobará ahora por análisis y qué exige ensayo futuro.

Escríbelo en el apartado **Interfaces y revisión** de tu propuesta.

Requisitos que debes consultar en [el registro](../../system/requisitos.md): **SCI-001, SCI-002, CTL-001, MET-001 y SAF-001**. Los valores del caso demostrativo son ejemplos, no límites aprobados.

## Si necesitas más archivos

Mantén la primera entrega en `propuesta.md`. Para ampliarla, desde **esta carpeta y tu rama** usa **Add file → Create new file**:

- `candidatos/CAND-01.md`: copia [templates/componente.md](../../templates/componente.md), rellena modelo/concepto, prestaciones, fuentes y dudas. Repite para la alternativa crítica.
- `analisis/calculo.md`: documenta entradas, unidades, método, resultado y limitaciones. Cambia el nombre por el cálculo concreto.
- Para un archivo existente: **Add file → Upload files** en tu rama.

Escribir `candidatos/CAND-01.md` crea la subcarpeta junto con el archivo. No hace falta crear carpetas vacías. Guarda con **Commit changes** y enlaza cada archivo desde tu propuesta.

Si hace falta, crea `analisis/error_medida.md` y `ejemplo_log.csv`. El registro puede tener tiempo, estado, velocidad comandada/estimada, caudal comandado/estimado, presión, temperatura, validez y fallo; incluye unidades y procedencia en su diccionario.

## Con quién revisar las interfaces

Una interfaz (ICD) es el acuerdo sobre lo que tu módulo envía, recibe o necesita del otro. Trabaja los acuerdos compartidos en `interfaces/`; tu propuesta explica el razonamiento y enlaza el ICD.

| Habla con | Para resolver | Documento compartido |
|---|---|---|
| M1 — NICOMANUQP | Pieza, trayectoria nominal, coordenadas y datos de movimiento | [ICD-001](../../interfaces/ICD-001.md) / [ICD-003](../../interfaces/ICD-003.md) |
| Gabriel — M2 | Caudal/presión, punto de medida, retraso y parada de alimentación | [ICD-001](../../interfaces/ICD-001.md) / [ICD-003](../../interfaces/ICD-003.md) / [ICD-005](../../interfaces/ICD-005.md) |
| M3 — por asignar | Consigna UV, temperatura, tiempos e interferencias de iluminación | [ICD-001](../../interfaces/ICD-001.md) / [ICD-003](../../interfaces/ICD-003.md) / [ICD-005](../../interfaces/ICD-005.md) |
| Shelton — M4 | Campo de visión/montaje, recursos eléctricos y respuesta segura | [ICD-004](../../interfaces/ICD-004.md) / [ICD-005](../../interfaces/ICD-005.md) |

Cuando M3 no tenga responsable, registra la pregunta y pide al equipo que designe revisor. Los usuarios para solicitar revisión están en [equipo](../../management/equipo.md).

### Paso a paso, sin esperar una reunión

1. Abre en **tu rama** el ICD enlazado en la tabla. Los cinco documentos ya existen; revisa si hay una Issue o PR trabajando el mismo punto.
2. Escribe el intercambio que propones: datos o conexión, unidades, rango, tiempos, condiciones y fallo. Marca tus valores TBR y lo desconocido TBD.
3. En **Puntos pendientes de revisión**, indica el apartado, la propuesta, el miembro que debe revisar y una pregunta concreta. Copia la misma tabla en el PR.
4. Abre o enlaza una Issue de **Cambio de interfaz** y comparte tu PR con esas personas. Registra la respuesta en GitHub y enlázala desde la tabla.
5. Mientras responden, continúa con tus cálculos o alternativas usando supuestos visibles. Incorpora correcciones en la misma rama; integra el acuerdo cuando los afectados hayan dejado conformidad y se haya revisado el conjunto.

**Ejemplo para tu módulo:** Puedes proponer un sistema completo de control usando supuestos TBR. Marca el retardo de alimentación para Gabriel, el control UV para M3, el marco de coordenadas para M1 y la posición de cámaras/estado seguro para Shelton.

Puedes proponer un modelo completo, incluso con partes de otros módulos. Señala quién debe verificar o confirmar cada parte; no la presentes como aceptada por el equipo. La [guía de colaboración](../../management/colaboracion.md) incluye la tabla y explica cómo registrar conformidades.

## Comparte y cierra tu primera entrega

1. Ve a **Pull requests → New pull request**: **base: main**, **compare: m5/propuesta-medicion**.
2. Escribe un título que describa la entrega y enlaza tu propuesta, requisitos e ICD modificados.
3. Incluye los puntos pendientes y solicita revisión a los contactos de la tabla. Si aún está en desarrollo, abre un PR en borrador; al estar listo, márcalo para revisión.
4. Responde observaciones, guarda correcciones en tu rama y registra la conformidad de los afectados. Otro integrante revisa los cambios técnicos importantes antes de integrarlos.

Tu primera entrega está preparada para revisión cuando:

- [ ] La propuesta responde: **¿Cómo mediremos diferencias entre piezas y qué señales, tiempos y montajes deben confirmar los otros módulos?**
- [ ] Las alternativas, fuentes, unidades, supuestos y límites están claros.
- [ ] Los puntos que requieren revisión tienen pregunta, contacto y enlace al ICD.
- [ ] Hay un método o resultado documentado: Método de medida, presupuesto inicial de errores y registro sintético. El tamaño de píxel no demuestra exactitud; el encoder del brazo no mide por sí solo la geometría del material.
- [ ] El PR permite encontrar los archivos y distinguir trabajo propuesto de acuerdos.

[Detalle técnico del módulo](ALCANCE_TECNICO.md) · [Guía de GitHub](../../CONTRIBUTING.md) · [Hitos](../../management/plan.md)
