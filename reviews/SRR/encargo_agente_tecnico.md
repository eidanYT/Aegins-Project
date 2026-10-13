# Encargo para el otro agente — Aportes técnicos al SRR de AEGINS

Este documento es un prompt para que Eidan lo entregue al otro agente. **No indica que el encargo ya se haya enviado.**

## Objetivo y autorización

Eidan quiere avanzar hoy en el borrador del System Requirements Review (SRR) de AEGINS / FORGE-UG, proyecto de impresión 3D en microgravedad. El repositorio es https://github.com/eidanYT/Aegins-Project y su rama compartida es main. Tienes acceso a GitHub. Tu encargo es producir propuestas técnicas revisables de **M1 movimiento, M2 material y extrusión y M3 UV y térmica**, con fuentes, cálculos preliminares y una síntesis para integrar con los otros módulos.

El agente del chat de Eidan tiene asignados M4 cámara/integración, M5 control/metrología y los documentos comunes del SRR. No presupongas que esos trabajos ya estén terminados. El objetivo de hoy es un paquete documental coherente; no fabricar ni demostrar aptitud de vuelo.

## Estado del proyecto y decisiones del usuario

El repositorio está en fase de concepto. Sus cinco propuesta.md eran borradores sin completar, los requisitos eran propuestas, los presupuestos estaban TBD y los ICD eran borradores. No había ensayos ni simulaciones validadas incluidos en el kit. Actualiza este estado leyendo GitHub antes de editar; otro agente puede haber avanzado.

Eidan mantiene dos plataformas candidatas: estación espacial y satélite, como payload. **Todavía no eligió una línea base.** No asumas que estación significa ISS, una presión concreta ni una interfaz al soporte vital; satélite no significa resina expuesta al vacío. Condiciona cualquier análisis a un ambiente declarado.

La pieza propuesta por Eidan consiste en **dos pirámides unidas por su base, con cada arista de 5 cm = 0,05 m**. Es una bipirámide; el usuario la llamó prisma. El polígono de la base, número de aristas y si se imprimirán caras o únicamente aristas no están definidos. No asumas octaedro de base cuadrada ni alteres el caso didáctico para hacerlo pasar por un caso elegido. Puedes analizar una geometría condicional, claramente marcada EJEMPLO/TBR.

Eidan propuso que la impresora trabaje dentro de una cámara, con una salida de gases cuya conexión y destino todavía desconoce. El jurado señaló posible daño a la tripulación por gases o polvo y la necesidad de considerar seguridad más allá de temperatura. Cámara y tratamiento son propuestas; no son protección validada. No inventes salida directa a cabina, conexión disponible al soporte vital, escape al exterior ni eficacia universal de filtros.

La otra observación del jurado fue que el brazo parece complejo y podría no ser adecuado para microgravedad. La respuesta exige comparar alternativas y explicar qué necesidad científica justifica orientación, así como sus cargas, montaje y limitaciones; no basta afirmar que funciona.

Eidan pidió una prórroga que no está confirmada. No dediques esta tarea a perseguir plazos ni contactar organizadores.

## Documentos del programa ya leídos por el agente de Eidan

Los lineamientos oficiales piden 10 minutos de exposición y 15 de preguntas. Se debe mostrar progreso desde Review 1 y respuesta a observaciones. Se evalúan claridad, viabilidad, cronograma, innovación, sostenibilidad, resiliencia/durabilidad, eficiencia de costes y modularidad.

La plantilla del informe tiene máximo 30 páginas y cubre introducción, contexto/objetivos, viabilidad técnica/económica/ambiental, diseño detallado con requisitos de misión y sistema y métodos A/T/I/D, mercado/costes de ciclo de vida, riesgos y gestión/cronograma, conclusiones y pasos hacia PDR. También contempla autonomía/fiabilidad y contribución logística. No se encontró una plantilla oficial de diapositivas.

Fuentes, si tienes acceso:
- https://docs.google.com/document/d/12ZDWNiUHeyCW8tckpVIAnYeAPqpNIW_J/edit — lineamientos de Review 2.
- https://docs.google.com/document/d/1VEZzT6vw134w6CKLxHCs_u7poRDYHhSM/edit — plantilla del informe.
- https://drive.google.com/file/d/1fCPoGXb0Y6MstuKdieDDerOqg5v8OnwV/view — evaluación de AEGINS de Review 1.

Esta síntesis permite trabajar aunque no tengas Drive. No uses la lista antigua de entregables del repositorio como única especificación oficial.

## Archivos que puedes editar

- modules/movimiento_NICOMANUQP/
- modules/extrusion_Gabriel/
- modules/uv_termica/
- models/srr_agente_tecnico/ para cálculos/estudios nuevos.
- reviews/SRR/aportes_agente_tecnico.md para el resumen de integración.

No edites system/, interfaces/, config/, management/, cad/, módulos M4/M5 ni los documentos generales del SRR: los integra el otro agente. Propón allí las filas o cambios necesarios mediante tu resumen, con identificadores existentes y sin declarar acuerdos que no existan. Lee CONTRIBUTING.md y cualquier AGENTS.md aplicable. Conserva el contenido técnico anterior y su contexto.

Antes de crear una rama comprueba las ramas y PR abiertos para evitar duplicar un trabajo propio existente. Trabaja en una rama propia desde main y abre un PR en borrador; no integres a main ni modifiques la rama del otro agente. Adjunta el PR a tu tarea si la herramienta está disponible. No contactes a miembros u organizadores: entrega el encargo y las preguntas en el PR y tu respuesta a Eidan.

## Entregas concretas

**M1:** completa propuesta.md con dos alternativas, incluida una de menor complejidad, y criterios para elegir. Propón trayectoria/anclaje y estudio de alcance según la geometría disponible. Identifica datos de masa del cabezal, base, tubos e inercias que faltan. Distingue factibilidad geométrica/cinemática de precisión física del material. No declares aptitud para microgravedad por usar un brazo comercial.

**M2:** completa propuesta.md con dos materiales/formulaciones candidatos y dos alternativas de alimentación, documentando compatibilidad, ambiente y limitaciones con fuentes primarias. Añade inventario preliminar y fichas de seguridad cuando estén disponibles. Calcula caudal nominal con diámetro y velocidad explícitos, como supuesto si no están elegidos. Declara límites de un modelo estacionario; presión, transitorios, burbujas, compatibilidad y emisiones requieren datos. No inventes curvas ni resultados de ensayo.

**M3:** completa propuesta.md con combinaciones material–fuente UV candidatas, espectro, geometría de iluminación y exposición, sombras y riesgo de curado en boquilla. Añade balance térmico preliminar con entradas/supuestos y fuentes. La dosis nominal no demuestra conversión o resistencia. El responsable humano de este módulo no está asignado; no inventes su aprobación.

Usa documentación primaria de fabricantes, artículos originales o NASA/ESA para datos especializados y verifica la versión/condiciones aplicables. No atribuyas calificación espacial a componentes terrestres. Si no encuentras evidencia, registra la carencia con una próxima acción concreta en vez de completar cifras.

Para cada módulo incluye recursos preliminares de masa, volumen, potencia normal/pico, energía, calor y coste con unidades, fuentes/fecha, condición y estado. Si no pueden estimarse de forma sustentada, documenta qué dato falta. No sumes picos sin su secuencia ni presentes precios históricos como cotizaciones actuales.

Crea cálculos reproducibles solo donde añadan evidencia útil; verifica conversiones y consistencia, e identifica cualquier análisis condicional o dato sintético. No necesitas ensayos físicos para escribir el borrador.

## Resumen para el agente integrador

En aportes_agente_tecnico.md incluye:
1. Resumen de qué quedó redactado y qué está sustentado.
2. Tabla de entradas/salidas comunes: geometría, velocidad, diámetro, caudal, espectro/exposición, masa del cabezal, montaje/tubos, potencia/calor y señales/latencias, con valor/unidad/fuente/estado o TBD.
3. Filas propuestas para requisitos e ICD-001/002/003/004/005; el otro agente hará la edición de los documentos compartidos.
4. Respuesta a la crítica del brazo, y aportes de material/UV a contención y seguridad.
5. Supuestos, dependencias, decisiones y revisión humana necesaria, con responsable propuesto y fecha por acordar.
6. Vínculos a archivos y evidencia, método de verificación y límites.
7. Texto técnico breve reutilizable en el informe, sin afirmar resultados no obtenidos.

Los responsables humanos registrados son NICOMANUQP para M1, Gabriel Hurtado para M2, Shelton Yauri para M4 y Eidan para M5. M3 y coordinación de sistemas siguen por asignar. La revisión de interfaces necesita conformidad de todos los afectados.

## Ritmo y resultado esperado

Lee el plan reviews/SRR/plan_trabajo_hoy.md si está disponible. Primera síntesis técnica después de unos 80 minutos de trabajo efectivo; después corrige con datos de integración. Prioriza propuestas coherentes y evidencia mínima sustentada sobre amplitud de investigación. Las decisiones sin respuesta permanecen abiertas.

En tu respuesta final a Eidan indica qué publicaste, enlace al PR, resultados establecidos, limitaciones y preguntas que desbloquean la integración. Deja comentarios breves en tu propia tarea al completar una fase. Este encargo no te autoriza a enviar mensajes a otras conversaciones.

## Matriz de seguimiento disponible en GitHub

Consulta reviews/SRR/respuesta_expertos.md en la propuesta SRR si está disponible. Registra las opiniones de los dos expertos del MDR / Review 1: EXP-01 pide justificar el brazo frente a una alternativa más simple; EXP-02 exige evaluar gases/polvo; EXP-03 amplía seguridad e impacto en diseño/costes. En tu síntesis aporta explícitamente la respuesta de M1 a EXP-01 y los datos de M2/M3 para EXP-02/03. No marques estas observaciones resueltas solo por redactar el texto.

## Reglas persistentes y registro de ejecución

Eidan solicitó aplicar controles de agentes. La propuesta [Reglas y controles para coordinar agentes en Aegins](https://github.com/eidanYT/Aegins-Project/pull/2) contiene AGENTS.md, la política de ámbitos, registros y CI; **su integración y la activación administrativa de protección de main siguen pendientes**.

Antes de iniciar o reanudar, comprueba si AGENTS.md y management/agent_policy.json ya están en main y lee su versión vigente. Si aún no se integraron, conserva el reparto de este encargo y lee la propuesta como borrador; no afirmes que la protección esté activa.

Usa una rama con prefijo tecnico/ para este encargo. Además de los archivos técnicos asignados, crea o actualiza únicamente tu propio registro management/agent_runs/<rama-con-barras-reemplazadas-por-guiones-bajos>.json desde templates/agent_run.json cuando la plantilla esté disponible. Conserva objetivo, avances comprobados, fuentes, pendientes con dueño/fecha, siguiente acción y revisores. Incluye estimaciones nuevas con unidad/fuente/estado y evidencias declaradas verificadas con método/alcance/archivo.

No edites AGENTS.md, workflows, política o validador para hacer pasar una comprobación, ni uses otro perfil para ampliar este encargo. Recupera el contexto del registro, los archivos y el PR al reanudar. La CI no sustituye revisión científica ni aprobación de interfaces.

## Decisiones nuevas de Eidan para integrar M1/M2/M3

Eidan eligió estación espacial con tripulación, dentro de cámara. Confirmó base cuadrada y pidió **aristas y caras cerradas**, con todas las aristas de 0,05 m. No hay material ni hardware elegidos.

La primera propuesta de integración recoge las decisiones en system/caso_srr.json y cad/pieza_srr.md. Antes de continuar, revisa main y los PR de integración para localizar la versión de ese caso: puede seguir pendiente de revisión. La geometría nominal tiene ocho caras y doce aristas, pero no hay espesor ni trayectoria aprobados.

M1 debe proponer recorrido de superficies y anclaje, además de aristas; M2, formación/espesor/material y gas/residuo interno; M3, exposición y sombras/curado de caras. No usar la longitud de aristas como tiempo o material total para las caras. Documenta la diferencia con el alcance anterior y los datos que requieres de M4/M5.
