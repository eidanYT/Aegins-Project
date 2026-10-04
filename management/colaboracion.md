# Proponer, pedir revisión y seguir trabajando

Cada integrante puede preparar un modelo completo de su módulo e incluso una propuesta del sistema entero. Esto permite evaluar una solución de principio a fin aunque los demás tengan horarios distintos.

**Distingue lo que propones de lo que los otros módulos ya han confirmado.** Usa TBR para supuestos propuestos y TBD para datos que todavía faltan. La revisión de una interfaz es un acuerdo entre áreas; la verificación técnica necesita un método y evidencia.

## Dónde va la información

| Información | Lugar |
|---|---|
| Tu explicación, alternativas y cálculos | `propuesta.md` y archivos de tu módulo |
| Lo que dos o más módulos intercambian | [Documento de interfaz ICD correspondiente](../interfaces/README.md) |
| Una pregunta pendiente o cambio que necesita seguimiento | Issue: **Cambio de interfaz** o **Tarea técnica** |
| Los archivos que propones incorporar | PR de tu rama hacia `main` |
| Preguntas para cada revisor y su respuesta | Conversación del PR; comentario sobre una línea si corresponde |
| Acuerdo final | Actualización del ICD, con enlaces al PR y a las conformidades |

## Paso a paso para una interfaz

1. **Busca el ICD y la conversación existente.** Mira [interfaces](../interfaces/README.md), Issues y PRs para no duplicar el mismo cambio.
2. **Escribe tu propuesta en tu rama.** Edita el ICD existente. Los ICD-002 a ICD-005 ya tienen un borrador preparado; si aparece una interfaz nueva, copia [templates/interfaz.md](../templates/interfaz.md) a `interfaces/ICD-006.md`, o al siguiente ID libre.
3. **Define el intercambio.** Qué envías, qué necesitas recibir, unidades, rango, tiempos, condiciones, fuente y reacción ante fallos. Marca datos propuestos TBR.
4. **Marca los puntos concretos por revisar.** Añade una fila por pregunta en la tabla de revisión del ICD y en el PR. Identifica el apartado; no basta “revisar todo”.
5. **Abre o enlaza una Issue de Cambio de interfaz.** Explica el cambio y sus efectos, y enlaza los archivos. Si ya existe una Issue, añade tu propuesta a esa.
6. **Abre un PR y pide revisión.** Usa los nombres de [equipo](equipo.md). Selecciona sus usuarios en Reviewers o menciona sus usuarios reales en un comentario; si faltan, comparte el enlace por el canal habitual.
7. **Continúa con lo que puedas resolver.** Elabora el modelo con supuestos visibles y, si procede, compara rangos. No tomes un supuesto pendiente como valor definitivo.
8. **El revisor deja una respuesta concreta.** Indica el punto, si lo acepta o qué debe cambiar, con su justificación. El autor incorpora las correcciones al mismo PR.
9. **Registra la conformidad de todos los afectados.** En el ICD enlaza comentarios/revisiones y la versión revisada. Un cambio posterior que afecte al acuerdo requiere nueva revisión.
10. **Integra cuando esté revisado.** La coordinación comprueba la coherencia y se integra. Actualiza requisitos, parámetros, modelos y evidencia que cambien con ese acuerdo.

## Tabla para copiar al documento y al PR

| Punto / apartado | Propuesta o supuesto | Quién debe revisar | Pregunta concreta | Estado de revisión | Enlace a respuesta |
|---|---|---|---|---|---|
| Ejemplo: caudal de ICD-001 | Valor TBR del caso analizado | Gabriel — M2 | ¿La alimentación propuesta puede entregar este caudal y con qué retardo? | Pendiente | — |

Estados de revisión: **Pendiente**, **Cambios solicitados**, **Conforme**. Solo escribe Conforme con una respuesta explícita y enlazada. Estos estados no equivalen a VERIFICADO por ensayo.

Si propones partes de otros módulos dentro de un modelo completo, marca cada una con el nombre del área que debe revisarla y conserva la información acordada en su documento compartido. No la conviertas en una segunda fuente de verdad dentro de tu propuesta.

## A quién pedir cada revisión

| Tema | Contacto |
|---|---|
| Trayectoria, posición, velocidad, alcance y cargas del brazo | M1 — NICOMANUQP |
| Material, boquilla, presión, caudal y retraso de alimentación | Gabriel — M2 |
| Fuente UV, exposición, sombras y temperatura | M3 — responsable por asignar |
| Recinto, montaje, contención y recursos de la plataforma | Shelton — M4 |
| Señales, sincronización, medición, registro y estados de control | Eidan — M5 |
| Coherencia del conjunto y versión de entrega | Coordinación — por asignar |

Cuando falte un responsable, abre la pregunta igualmente y pide al equipo que designe quién la revisará. Puedes avanzar tu borrador; ese punto sigue pendiente de conformidad.

[Volver al inicio](../README.md) · [Cómo editar y abrir un PR](../CONTRIBUTING.md)
