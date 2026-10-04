# M2-Gabriel — Material y extrusión

**Responsable: Gabriel Hurtado.** [Volver al inicio](../../README.md) · [Contactos](../../management/equipo.md)

Gabriel, propón qué material usar y cómo alimentar la boquilla con caudal y presión compatibles con la impresión.

## Get started: empieza ahora

**Primera entrega:** Una comparación de dos materiales y dos formas de alimentación, con un cálculo nominal y preguntas sobre movimiento, UV y control. No necesitas esperar una fecha ni la respuesta de todos para preparar un borrador.

1. En GitHub, abre el selector de rama `main`, escribe `m2/propuesta-extrusion` y selecciona **Create branch … from main**.
2. En esa rama, entra en `modules/extrusion_Gabriel` y abre [propuesta.md](propuesta.md). Ya está creado.
3. Pulsa el lápiz (**Edit this file**), rellena la estructura siguiendo los pasos de abajo y usa **Preview**.
4. Guarda con **Commit changes** en tu rama y un mensaje que explique lo que avanzaste. Para continuar, vuelve a abrir esa misma rama.

La carpeta pertenece al mismo repositorio; no crees otro repositorio para tu módulo.

## Desarrolla tu propuesta

### 1. Caso de impresión

Abre [misión](../../system/mision.md), [caso demostrativo](../../config/caso_demo.json) e [ICD-001](../../interfaces/ICD-001.md). Usa diámetro y velocidad como supuestos identificados, sin tratarlos como valores aprobados.

Escríbelo en el apartado **Geometría y comparación** de tu propuesta.

### 2. Material y alimentación

Compara dos materiales con sus fichas técnicas/de seguridad, y dos arquitecturas de alimentación. Indica viscosidad, compatibilidad, volumen, presión y datos que faltan; una opción sin ficha sigue siendo concepto.

Escríbelo en el apartado **Alternativas** de tu propuesta.

### 3. Caudal y respuesta

Documenta el cálculo de caudal nominal del caso, unidades, supuestos y límites. Explica qué diferencia hay entre caudal comandado, estimado y entregado; identifica presión, retrasos y burbujas.

Escríbelo en el apartado **Modelo y verificación** de tu propuesta.

### 4. Montaje y fallos

Propón depósito, boquilla, tubos y conexiones. Describe qué revisar ante atasco, fuga, pérdida de energía o presión residual.

Escríbelo en el apartado **Interfaces y revisión** de tu propuesta.

Requisitos que debes consultar en [el registro](../../system/requisitos.md): **EXT-001 y EXT-002**. Los valores del caso demostrativo son ejemplos, no límites aprobados.

## Si necesitas más archivos

Mantén la primera entrega en `propuesta.md`. Para ampliarla, desde **esta carpeta y tu rama** usa **Add file → Create new file**:

- `candidatos/CAND-01.md`: copia [templates/componente.md](../../templates/componente.md), rellena modelo/concepto, prestaciones, fuentes y dudas. Repite para la alternativa crítica.
- `analisis/calculo.md`: documenta entradas, unidades, método, resultado y limitaciones. Cambia el nombre por el cálculo concreto.
- Para un archivo existente: **Add file → Upload files** en tu rama.

Escribir `candidatos/CAND-01.md` crea la subcarpeta junto con el archivo. No hace falta crear carpetas vacías. Guarda con **Commit changes** y enlaza cada archivo desde tu propuesta.

Si hace falta, crea `analisis/caudal.md`. Las fichas de candidatos se crean en `candidatos/` como se explica abajo.

## Con quién revisar las interfaces

Una interfaz (ICD) es el acuerdo sobre lo que tu módulo envía, recibe o necesita del otro. Trabaja los acuerdos compartidos en `interfaces/`; tu propuesta explica el razonamiento y enlaza el ICD.

| Habla con | Para resolver | Documento compartido |
|---|---|---|
| M1 — NICOMANUQP | Velocidad, diámetro propuesto, carga del cabezal y recorrido de tubos | [ICD-001](../../interfaces/ICD-001.md) / [ICD-002](../../interfaces/ICD-002.md) |
| M3 — por asignar | Compatibilidad de resina con espectro UV y ventana de curado | [ICD-001](../../interfaces/ICD-001.md) / [ICD-002](../../interfaces/ICD-002.md) |
| Shelton — M4 | Montaje del depósito, retención de líquidos, acceso y residuos | [ICD-002](../../interfaces/ICD-002.md) / [ICD-005](../../interfaces/ICD-005.md) |
| Eidan — M5 | Consigna de caudal, lectura de presión, retrasos y reacción ante fallo | [ICD-001](../../interfaces/ICD-001.md) / [ICD-003](../../interfaces/ICD-003.md) / [ICD-005](../../interfaces/ICD-005.md) |

Cuando M3 no tenga responsable, registra la pregunta y pide al equipo que designe revisor. Los usuarios para solicitar revisión están en [equipo](../../management/equipo.md).

### Paso a paso, sin esperar una reunión

1. Abre en **tu rama** el ICD enlazado en la tabla. Los cinco documentos ya existen; revisa si hay una Issue o PR trabajando el mismo punto.
2. Escribe el intercambio que propones: datos o conexión, unidades, rango, tiempos, condiciones y fallo. Marca tus valores TBR y lo desconocido TBD.
3. En **Puntos pendientes de revisión**, indica el apartado, la propuesta, el miembro que debe revisar y una pregunta concreta. Copia la misma tabla en el PR.
4. Abre o enlaza una Issue de **Cambio de interfaz** y comparte tu PR con esas personas. Registra la respuesta en GitHub y enlázala desde la tabla.
5. Mientras responden, continúa con tus cálculos o alternativas usando supuestos visibles. Incorpora correcciones en la misma rama; integra el acuerdo cuando los afectados hayan dejado conformidad y se haya revisado el conjunto.

**Ejemplo para tu módulo:** Puedes proponer material y caudal completos usando una ventana de curado TBR. Marca “M3 debe confirmar compatibilidad material–UV” y “Eidan debe revisar consigna y retardo”; continúa comparando alternativas mientras recibes respuesta.

Puedes proponer un modelo completo, incluso con partes de otros módulos. Señala quién debe verificar o confirmar cada parte; no la presentes como aceptada por el equipo. La [guía de colaboración](../../management/colaboracion.md) incluye la tabla y explica cómo registrar conformidades.

## Comparte y cierra tu primera entrega

1. Ve a **Pull requests → New pull request**: **base: main**, **compare: m2/propuesta-extrusion**.
2. Escribe un título que describa la entrega y enlaza tu propuesta, requisitos e ICD modificados.
3. Incluye los puntos pendientes y solicita revisión a los contactos de la tabla. Si aún está en desarrollo, abre un PR en borrador; al estar listo, márcalo para revisión.
4. Responde observaciones, guarda correcciones en tu rama y registra la conformidad de los afectados. Otro integrante revisa los cambios técnicos importantes antes de integrarlos.

Tu primera entrega está preparada para revisión cuando:

- [ ] La propuesta responde: **¿Qué alimentación y material cubren el caso propuesto, y qué datos UV, de presión y retardo requieren confirmación?**
- [ ] Las alternativas, fuentes, unidades, supuestos y límites están claros.
- [ ] Los puntos que requieren revisión tienen pregunta, contacto y enlace al ICD.
- [ ] Hay un método o resultado documentado: Cálculo de caudal y modelo de presión/respuesta con fuentes y límites. Una orden al pistón no prueba el caudal real en la boquilla.
- [ ] El PR permite encontrar los archivos y distinguir trabajo propuesto de acuerdos.

[Detalle técnico del módulo](ALCANCE_TECNICO.md) · [Guía de GitHub](../../CONTRIBUTING.md) · [Hitos](../../management/plan.md)
