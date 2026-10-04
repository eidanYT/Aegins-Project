# Cómo trabajar en GitHub, paso a paso

Puedes hacer el primer documento desde el navegador. Necesitas permiso de escritura; si no puedes editar o crear una rama, pide acceso a Eidan (`eidanYT`).

## 1. Abre tu módulo

Desde el [README principal](README.md), entra en tu módulo y lee su primera entrega. Su archivo `propuesta.md` ya está creado: no hace falta preparar una carpeta vacía ni esperar al cronograma.

Una Issue registra una tarea; un archivo contiene el trabajo; un PR propone incorporar tus cambios; `main` reúne la versión compartida.

## 2. Crea una rama para tu tarea

1. En la página del repositorio, abre el selector que dice `main`.
2. Escribe un nombre breve, por ejemplo `m5/propuesta-medicion`.
3. Selecciona **Create branch … from main**.
4. Comprueba que el selector muestra tu rama.

Usa una rama por tarea. Para continuar una propuesta existente, abre su rama o PR; no crees otra copia de la misma tarea.

## 3. Escribe y guarda

1. En tu rama, abre `propuesta.md` dentro de tu módulo.
2. Pulsa el lápiz (**Edit this file**).
3. Sustituye los campos pendientes por tu propuesta, fuentes y cálculos. Mantén lo desconocido como TBD y lo propuesto como TBR.
4. Usa **Preview** para ver cómo queda.
5. Pulsa **Commit changes**, escribe qué avanzaste y guarda en **tu rama**.

Puedes guardar varias veces. Un commit es una versión registrada de tus cambios.

## 4. Crea archivos o carpetas solo cuando hagan falta

Desde la carpeta de tu módulo y dentro de tu rama: **Add file → Create new file**.

- Para un documento nuevo escribe `medicion.md`.
- Para una ficha escribe `candidatos/CAND-01.md` y copia la [plantilla de componente](templates/componente.md).
- Para un cálculo escribe `analisis/calculo.md`; incluye datos de entrada, unidades, método, resultado y límites.
- Para subir un archivo existente usa **Add file → Upload files**, manteniendo seleccionada tu rama.

La barra `/` del nombre crea la subcarpeta. Git guarda archivos, no carpetas vacías. Los documentos `.md` son texto que GitHub muestra con títulos, tablas y enlaces.

Usa el [registro CAD](cad/registro.md) para identificar archivos o versiones CAD externas. En [evidence/](evidence/README.md) guarda resultados con la [plantilla de evidencia](templates/evidencia.md). Etiqueta las simulaciones y los datos sintéticos; no los presentes como ensayos reales.

## 5. Comparte un pull request

1. Abre **Pull requests → New pull request**.
2. Elige **base: main** y **compare: tu rama**.
3. Pulsa **Create pull request**, escribe un título concreto y completa la plantilla.
4. Indica los archivos, el resultado y la tabla de puntos que requieren revisión.
5. Si estás desarrollándolo, usa **Create draft pull request**. Cuando esté listo para recibir revisión técnica, márcalo listo para revisión.
6. Solicita revisión a los usuarios indicados en [equipo](management/equipo.md). Si falta un usuario, comparte el enlace y registra a quién necesitas.

Al editar y guardar de nuevo en la misma rama, el PR se actualiza. Los demás pueden comentar cuando tengan tiempo.

## 6. Registra tareas y acuerdos sin duplicar documentos

Si necesitas una decisión o seguimiento: **Issues → New issue → Get started** en la plantilla **Tarea técnica** o **Cambio de interfaz**. Comprueba antes si ya existe una Issue sobre ese asunto.

Enlaza los archivos y el PR; no copies todo el informe en la Issue. Usa `Closes #N` en el PR solo si su integración resuelve por completo esa Issue. El número lo asigna GitHub.

Para cambios que afectan a otro módulo, sigue la [guía de colaboración](management/colaboracion.md). No hace falta tener configurado un Project para empezar.

## 7. Revisa e integra

Ningún cambio técnico importante se integra sin revisión de otra persona. Las interfaces requieren conformidad explícita de todos los módulos afectados y coordinación de sistemas; el autor puede registrar la de su propio lado. Si cubre ambos lados, incluir un revisor independiente.

Cuando se resuelvan las observaciones, quien tenga permisos integra (**Merge**) y se registra el acuerdo. Una propuesta disponible para comentar no está automáticamente aprobada.

Si usas GitHub Desktop: actualiza `main` con **Fetch origin / Pull origin**, crea una rama, edita, haz **Commit**, **Publish branch / Push origin** y abre un PR.

## Reglas técnicas que conservamos

- Unidades SI internamente; conversiones explícitas cuando se muestren otras unidades.
- Fuente, versión, condiciones e incertidumbre para cada dato relevante.
- Estados de datos: EJEMPLO, TBD, TBR, APROBADO o VERIFICADO. Aprobar una propuesta no valida físicamente el sistema.
- Un parámetro compartido tiene una única fuente de verdad. El caso didáctico vive en [config/caso_demo.json](config/caso_demo.json).
- Quien cambia un parámetro revisa los modelos y documentos afectados.
- Para editar simultáneamente el mismo documento, repartir secciones y elegir quién integra. Para CAD binario, reservar un editor por pieza/ensamble en la Issue.
- Conservar las versiones anteriores con su contexto, sin presentarlas como resultados vigentes.

[Volver al inicio](README.md) · [Fuentes y documentación de GitHub](references/fuentes.md)
