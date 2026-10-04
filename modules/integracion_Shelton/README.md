# M4-Shelton — Recinto e integración

**Responsable: Shelton Yauri.** [Volver al inicio](../../README.md) · [Contactos](../../management/equipo.md)

Shelton, propón dónde se aloja el sistema y cómo integrar brazo, material, UV, electrónica y medición dentro de sus recursos y límites.

## Get started: empieza ahora

**Primera entrega:** Una propuesta de escenario de referencia, esquema de recinto, presupuesto inicial y preguntas de montaje, recursos y contención. No necesitas esperar una fecha ni la respuesta de todos para preparar un borrador.

1. En GitHub, abre el selector de rama `main`, escribe `m4/propuesta-integracion` y selecciona **Create branch … from main**.
2. En esa rama, entra en `modules/integracion_Shelton` y abre [propuesta.md](propuesta.md). Ya está creado.
3. Pulsa el lápiz (**Edit this file**), rellena la estructura siguiendo los pasos de abajo y usa **Preview**.
4. Guarda con **Commit changes** en tu rama y un mensaje que explique lo que avanzaste. Para continuar, vuelve a abrir esa misma rama.

La carpeta pertenece al mismo repositorio; no crees otro repositorio para tu módulo.

## Desarrolla tu propuesta

### 1. Escenario de referencia

Abre [misión](../../system/mision.md) y compara las tres opciones de D-001. Propón una para desarrollar el concepto y explica presión, temperatura, acceso y recursos asumidos. Marca la elección TBR hasta que el equipo la acuerde.

Escríbelo en el apartado **Geometría y comparación** de tu propuesta.

### 2. Recinto y alternativas

Dibuja el recinto y la disposición preliminar del brazo, depósito, óptica y sensores. Explica montaje, ventanas, pasamuros, acceso y retención de líquidos/pieza. Compara una alternativa pertinente.

Escríbelo en el apartado **Alternativas** de tu propuesta.

### 3. Recursos del conjunto

Reúne masa, volumen, potencia, calor y coste de las propuestas disponibles. Si faltan, usa asignaciones provisionales explícitas y preguntas. Registra el presupuesto compartido en [system/presupuestos.md](../../system/presupuestos.md).

Escríbelo en el apartado **Modelo y verificación** de tu propuesta.

### 4. Integración y riesgos

Comprueba envolvente y posibles incompatibilidades. Documenta peligros y controles en [system/riesgos.md](../../system/riesgos.md), y referencia los acuerdos de montaje, recursos y fallos.

Escríbelo en el apartado **Interfaces y revisión** de tu propuesta.

Requisitos que debes consultar en [el registro](../../system/requisitos.md): **SYS-001, INT-001 e INT-002**. Los valores del caso demostrativo son ejemplos, no límites aprobados.

## Si necesitas más archivos

Mantén la primera entrega en `propuesta.md`. Para ampliarla, desde **esta carpeta y tu rama** usa **Add file → Create new file**:

- `candidatos/CAND-01.md`: copia [templates/componente.md](../../templates/componente.md), rellena modelo/concepto, prestaciones, fuentes y dudas. Repite para la alternativa crítica.
- `analisis/calculo.md`: documenta entradas, unidades, método, resultado y limitaciones. Cambia el nombre por el cálculo concreto.
- Para un archivo existente: **Add file → Upload files** en tu rama.

Escribir `candidatos/CAND-01.md` crea la subcarpeta junto con el archivo. No hace falta crear carpetas vacías. Guarda con **Commit changes** y enlaza cada archivo desde tu propuesta.

Para ampliar, crea `analisis/envolvente.md`; registra las versiones CAD en [cad/registro.md](../../cad/registro.md).

## Con quién revisar las interfaces

Una interfaz (ICD) es el acuerdo sobre lo que tu módulo envía, recibe o necesita del otro. Trabaja los acuerdos compartidos en `interfaces/`; tu propuesta explica el razonamiento y enlaza el ICD.

| Habla con | Para resolver | Documento compartido |
|---|---|---|
| M1 — NICOMANUQP | Envolvente del movimiento, base, cargas y recorrido de cables/tubos | [ICD-002](../../interfaces/ICD-002.md) / [ICD-004](../../interfaces/ICD-004.md) |
| Gabriel — M2 | Depósito, tubos, fugas, residuos, presión y contención | [ICD-002](../../interfaces/ICD-002.md) / [ICD-005](../../interfaces/ICD-005.md) |
| M3 — por asignar | Óptica, calor, protección UV y temperatura del recinto | [ICD-002](../../interfaces/ICD-002.md) / [ICD-004](../../interfaces/ICD-004.md) / [ICD-005](../../interfaces/ICD-005.md) |
| Eidan — M5 | Montaje/visibilidad de cámaras, potencia/comunicaciones y estado seguro | [ICD-003](../../interfaces/ICD-003.md) / [ICD-004](../../interfaces/ICD-004.md) / [ICD-005](../../interfaces/ICD-005.md) |

Cuando M3 no tenga responsable, registra la pregunta y pide al equipo que designe revisor. Los usuarios para solicitar revisión están en [equipo](../../management/equipo.md).

### Paso a paso, sin esperar una reunión

1. Abre en **tu rama** el ICD enlazado en la tabla. Los cinco documentos ya existen; revisa si hay una Issue o PR trabajando el mismo punto.
2. Escribe el intercambio que propones: datos o conexión, unidades, rango, tiempos, condiciones y fallo. Marca tus valores TBR y lo desconocido TBD.
3. En **Puntos pendientes de revisión**, indica el apartado, la propuesta, el miembro que debe revisar y una pregunta concreta. Copia la misma tabla en el PR.
4. Abre o enlaza una Issue de **Cambio de interfaz** y comparte tu PR con esas personas. Registra la respuesta en GitHub y enlázala desde la tabla.
5. Mientras responden, continúa con tus cálculos o alternativas usando supuestos visibles. Incorpora correcciones en la misma rama; integra el acuerdo cuando los afectados hayan dejado conformidad y se haya revisado el conjunto.

**Ejemplo para tu módulo:** Puedes dibujar un recinto completo con reservas de espacio TBR. Marca la envolvente del brazo para M1, el depósito para Gabriel, la evacuación térmica para M3 y el campo de visión para Eidan; no presentes esas reservas como compatibilidad demostrada.

Puedes proponer un modelo completo, incluso con partes de otros módulos. Señala quién debe verificar o confirmar cada parte; no la presentes como aceptada por el equipo. La [guía de colaboración](../../management/colaboracion.md) incluye la tabla y explica cómo registrar conformidades.

## Comparte y cierra tu primera entrega

1. Ve a **Pull requests → New pull request**: **base: main**, **compare: m4/propuesta-integracion**.
2. Escribe un título que describa la entrega y enlaza tu propuesta, requisitos e ICD modificados.
3. Incluye los puntos pendientes y solicita revisión a los contactos de la tabla. Si aún está en desarrollo, abre un PR en borrador; al estar listo, márcalo para revisión.
4. Responde observaciones, guarda correcciones en tu rama y registra la conformidad de los afectados. Otro integrante revisa los cambios técnicos importantes antes de integrarlos.

Tu primera entrega está preparada para revisión cuando:

- [ ] La propuesta responde: **¿Cómo cabe y se conecta el conjunto, y qué asignaciones o medidas deben confirmar los otros módulos?**
- [ ] Las alternativas, fuentes, unidades, supuestos y límites están claros.
- [ ] Los puntos que requieren revisión tienen pregunta, contacto y enlace al ICD.
- [ ] Hay un método o resultado documentado: Esquema/CAD con revisión de envolvente y presupuesto con incertidumbre. No asumir límites de una plataforma real sin fuente.
- [ ] El PR permite encontrar los archivos y distinguir trabajo propuesto de acuerdos.

[Detalle técnico del módulo](ALCANCE_TECNICO.md) · [Guía de GitHub](../../CONTRIBUTING.md) · [Hitos](../../management/plan.md)
