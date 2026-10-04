# M1-NICOMANUQP — Movimiento

**Responsable: NICOMANUQP.** [Volver al inicio](../../README.md) · [Contactos](../../management/equipo.md)

Propón cómo el mecanismo moverá y orientará la boquilla para imprimir la pieza de referencia, y qué límites tendrá.

## Get started: empieza ahora

**Primera entrega:** Una propuesta de movimiento con dos alternativas, trayectoria representativa, límites y preguntas para los otros módulos. No necesitas esperar una fecha ni la respuesta de todos para preparar un borrador.

1. En GitHub, abre el selector de rama `main`, escribe `m1/propuesta-movimiento` y selecciona **Create branch … from main**.
2. En esa rama, entra en `modules/movimiento_NICOMANUQP` y abre [propuesta.md](propuesta.md). Ya está creado.
3. Pulsa el lápiz (**Edit this file**), rellena la estructura siguiendo los pasos de abajo y usa **Preview**.
4. Guarda con **Commit changes** en tu rama y un mensaje que explique lo que avanzaste. Para continuar, vuelve a abrir esa misma rama.

La carpeta pertenece al mismo repositorio; no crees otro repositorio para tu módulo.

## Desarrolla tu propuesta

### 1. Pieza y trayectoria

Abre [misión](../../system/mision.md) y [caso demostrativo](../../config/caso_demo.json). Propón la geometría de prueba, posición y orientación de la boquilla. Si usas el caso demostrativo, identifícalo como EJEMPLO; si faltan datos, marca tus supuestos TBR.

Escríbelo en el apartado **Geometría y comparación** de tu propuesta.

### 2. Alternativas

Compara dos arquitecturas de movimiento. Justifica alcance, orientación, espacio disponible y capacidad de cargar el cabezal; registra fuentes y restricciones.

Escríbelo en el apartado **Alternativas** de tu propuesta.

### 3. Modelo preliminar

Esboza la trayectoria y cómo comprobarás límites, colisiones y cargas. Indica qué sistema de coordenadas usas. Puedes entregar un esquema o análisis antes de tener CAD completo.

Escríbelo en el apartado **Modelo y verificación** de tu propuesta.

### 4. Aportes al conjunto

Propón velocidad, montaje, envolvente y cargas. Marca masa del cabezal, mangueras o límites de plataforma que otros deban confirmar.

Escríbelo en el apartado **Interfaces y revisión** de tu propuesta.

Requisitos que debes consultar en [el registro](../../system/requisitos.md): **MOT-001 y MOT-002**. Los valores del caso demostrativo son ejemplos, no límites aprobados.

## Si necesitas más archivos

Mantén la primera entrega en `propuesta.md`. Para ampliarla, desde **esta carpeta y tu rama** usa **Add file → Create new file**:

- `candidatos/CAND-01.md`: copia [templates/componente.md](../../templates/componente.md), rellena modelo/concepto, prestaciones, fuentes y dudas. Repite para la alternativa crítica.
- `analisis/calculo.md`: documenta entradas, unidades, método, resultado y limitaciones. Cambia el nombre por el cálculo concreto.
- Para un archivo existente: **Add file → Upload files** en tu rama.

Escribir `candidatos/CAND-01.md` crea la subcarpeta junto con el archivo. No hace falta crear carpetas vacías. Guarda con **Commit changes** y enlaza cada archivo desde tu propuesta.

Si lo necesitas, crea `analisis/trayectoria.md`. El CAD puede enlazarse desde `propuesta.md` e identificarse en [cad/registro.md](../../cad/registro.md).

## Con quién revisar las interfaces

Una interfaz (ICD) es el acuerdo sobre lo que tu módulo envía, recibe o necesita del otro. Trabaja los acuerdos compartidos en `interfaces/`; tu propuesta explica el razonamiento y enlaza el ICD.

| Habla con | Para resolver | Documento compartido |
|---|---|---|
| Gabriel — M2 | Masa de depósito/boquilla, tubos y caudal compatible con la velocidad | [ICD-001](../../interfaces/ICD-001.md) / [ICD-002](../../interfaces/ICD-002.md) |
| M3 — por asignar | Masa y geometría UV, exposición compatible con la trayectoria | [ICD-001](../../interfaces/ICD-001.md) / [ICD-002](../../interfaces/ICD-002.md) |
| Shelton — M4 | Montaje, espacio y cargas que recibirá la plataforma | [ICD-002](../../interfaces/ICD-002.md) / [ICD-004](../../interfaces/ICD-004.md) |
| Eidan — M5 | Trayectoria nominal, coordenadas, tiempos y métricas para comparar piezas | [ICD-001](../../interfaces/ICD-001.md) / [ICD-003](../../interfaces/ICD-003.md) |

Cuando M3 no tenga responsable, registra la pregunta y pide al equipo que designe revisor. Los usuarios para solicitar revisión están en [equipo](../../management/equipo.md).

### Paso a paso, sin esperar una reunión

1. Abre en **tu rama** el ICD enlazado en la tabla. Los cinco documentos ya existen; revisa si hay una Issue o PR trabajando el mismo punto.
2. Escribe el intercambio que propones: datos o conexión, unidades, rango, tiempos, condiciones y fallo. Marca tus valores TBR y lo desconocido TBD.
3. En **Puntos pendientes de revisión**, indica el apartado, la propuesta, el miembro que debe revisar y una pregunta concreta. Copia la misma tabla en el PR.
4. Abre o enlaza una Issue de **Cambio de interfaz** y comparte tu PR con esas personas. Registra la respuesta en GitHub y enlázala desde la tabla.
5. Mientras responden, continúa con tus cálculos o alternativas usando supuestos visibles. Incorpora correcciones en la misma rama; integra el acuerdo cuando los afectados hayan dejado conformidad y se haya revisado el conjunto.

**Ejemplo para tu módulo:** Si propones aumentar la velocidad, registra el valor TBR y pregunta a Gabriel si puede mantener el caudal, a M3 si mantiene la exposición y a Eidan qué cambia en la sincronización. No cambies solo la velocidad del brazo.

Puedes proponer un modelo completo, incluso con partes de otros módulos. Señala quién debe verificar o confirmar cada parte; no la presentes como aceptada por el equipo. La [guía de colaboración](../../management/colaboracion.md) incluye la tabla y explica cómo registrar conformidades.

## Comparte y cierra tu primera entrega

1. Ve a **Pull requests → New pull request**: **base: main**, **compare: m1/propuesta-movimiento**.
2. Escribe un título que describa la entrega y enlaza tu propuesta, requisitos e ICD modificados.
3. Incluye los puntos pendientes y solicita revisión a los contactos de la tabla. Si aún está en desarrollo, abre un PR en borrador; al estar listo, márcalo para revisión.
4. Responde observaciones, guarda correcciones en tu rama y registra la conformidad de los afectados. Otro integrante revisa los cambios técnicos importantes antes de integrarlos.

Tu primera entrega está preparada para revisión cuando:

- [ ] La propuesta responde: **¿Qué trayectoria y límites permite esta alternativa, y qué datos del cabezal y la plataforma faltan?**
- [ ] Las alternativas, fuentes, unidades, supuestos y límites están claros.
- [ ] Los puntos que requieren revisión tienen pregunta, contacto y enlace al ICD.
- [ ] Hay un método o resultado documentado: Esquema o trayectoria con método de comprobación, límites e incertidumbres. Distingue alcance simulado de precisión real de la pieza.
- [ ] El PR permite encontrar los archivos y distinguir trabajo propuesto de acuerdos.

[Detalle técnico del módulo](ALCANCE_TECNICO.md) · [Guía de GitHub](../../CONTRIBUTING.md) · [Hitos](../../management/plan.md)
