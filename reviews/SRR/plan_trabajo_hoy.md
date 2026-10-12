# Plan de trabajo de hoy — Paquete SRR de AEGINS / FORGE-UG

Fecha: 12 de octubre de 2026. **Plan propuesto, pendiente de confirmar disponibilidad del equipo.** Eidan ha solicitado una prórroga; su aprobación no está confirmada. El trabajo técnico puede avanzar mientras se responde.

## Resultado que buscamos

En unas cuatro horas de trabajo coordinado, producir un **borrador integrado del SRR** con aportes de los cinco módulos, requisitos trazables, recursos estimados, riesgos, visualización conceptual y guion de exposición. La revisión técnica y las decisiones críticas determinan si puede declararse listo para entregar. No se promete terminar fabricación, ensayos ni calificación de vuelo hoy.

La plantilla oficial pide un informe de hasta 30 páginas. La exposición dura 10 minutos y las preguntas 15 minutos. Debe mostrarse progreso frente a la primera revisión, especialmente adecuación/complejidad del brazo y seguridad de emisiones. También cubre viabilidad económica y ambiental, mercado, costes de ciclo de vida, autonomía, resiliencia, modularidad y cronograma.

## Contexto común que no se debe perder

- Payload para estación espacial o satélite: dos alternativas abiertas, no dos compatibilidades demostradas. Elegir una línea base o mantener las conclusiones expresamente condicionadas.
- Pieza propuesta: dos pirámides unidas por su base; cada arista mide 5 cm (0,05 m). Base común y número de aristas por precisar. No asumir un octaedro automáticamente.
- Cámara de impresión propuesta por Eidan. Conexión y destino de gases pendientes; no se asume descarga a cabina, al exterior ni conexión disponible al soporte vital.
- Las propuestas de módulos, interfaces, requisitos y presupuestos del repositorio estaban en borrador. El caso de configuración es didáctico.
- No hay ensayos ni simulaciones validadas publicados en el kit. Una cifra estimada, un esquema o una propuesta aprobada no constituye validación física.

## Reparto propuesto entre los dos agentes

**No se ha enviado todavía una tarea a otro agente.** Eidan puede entregarle el [encargo completo](encargo_agente_tecnico.md).

| Actor | Trabajo | Archivos propios | Resultado |
|---|---|---|---|
| Otro agente técnico | M1 movimiento, M2 material/extrusión, M3 UV/térmica; fuentes y cálculos preliminares | Los tres módulos; models/srr_agente_tecnico/; aportes_agente_tecnico.md en esta carpeta | Propuestas técnicas y tabla de datos, requisitos e interfaces a integrar |
| Agente de este chat — asignación para continuar | M4 cámara/integración, M5 control/metrología; síntesis y paquete SRR | M4/M5; system/; interfaces/; gestión; informe, guion y registro CAD | Integración coherente sin editar archivos del otro agente |
| Eidan y equipo humano | Decisiones y revisión de los módulos afectados | Comentarios/revisiones, con acuerdos enlazados | Decisiones explícitas; conformidades técnicas |

Los cálculos nominales compartidos se guardan con entradas, unidades, fuentes y estado. El otro agente propone cambios de parámetros en su aporte; este chat integra los documentos comunes tras revisar coherencia.

## Ruta de cuatro horas desde el inicio efectivo

| Ventana | Trabajo simultáneo | Salida mínima y condición |
|---|---|---|
| 0–20 min | Eidan/equipo decide plataforma provisional, base de la pieza, aristas o caras, material candidato y responsable provisional de UV. Ambos agentes inspeccionan el estado de GitHub. | Hoja de decisiones. Si algo no se decide, supuesto TBR identificado y resultados condicionados; no se declara cierre. |
| 20–100 min | Otro agente redacta M1/M2/M3 y cálculos con fuentes. Este chat desarrolla M4/M5, respuesta al jurado, requisitos e integración. | Un aporte concreto por módulo y primera tabla de masa/potencia/volumen/calor/coste, sin cifras fabricadas. |
| 100–160 min | Intercambio de datos y revisión con los responsables humanos; integración del caso común, interfaces y riesgos. | Velocidad–caudal–UV coherentes bajo supuestos; montaje, señales, fallos y recursos identificados. Contradicciones registradas y corregidas. |
| 160–210 min | Consolidación del informe oficial, guion de 10 minutos y visualización conceptual de la geometría disponible. | Borrador único, imágenes a escala cuando la geometría esté definida, fuentes y trazabilidad. |
| 210–240 min | Revisión independiente, ensayo de exposición y comprobación de accesos/versiones. | Correcciones, decisiones residuales con propietario/fecha y propuesta de versión de entrega. Solo congelar después de revisión. |

Las ventanas son asignaciones de trabajo, no garantía de cierre. Si faltan respuestas o fuentes, entregar un borrador con pendientes visibles y actualizar el plan; no convertir supuestos en acuerdos.

## Qué debe entregar cada módulo

| Módulo | Revisión humana existente | Entrega mínima para hoy |
|---|---|---|
| M1 — Movimiento | NICOMANUQP | Comparación de mecanismo orientable y alternativa más simple; justificación de orientación; geometría/poses, alcance, anclaje y cargas; distinguir estudio geométrico de precisión real. |
| M2 — Material y extrusión | Gabriel Hurtado | Candidatos documentados de material y alimentación; inventario/SDS disponible; caudal nominal con entradas explícitas; presión y transitorios estimados o pendientes justificados. |
| M3 — UV y térmica | Por asignar | Compatibilidad material–espectro, esquema de exposición, balance térmico preliminar y sombras/atasco; dosis no equivale a curado demostrado. |
| M4 — Recinto e integración | Shelton Yauri | Cámara y rutas de gestión de emisiones alternativas; montaje, accesos y recursos; límites de host pendientes; análisis de contaminación y fallos. |
| M5 — Control y metrología | Eidan | Secuencia nominal y de fallos, señales/unidades/tiempo, medida de geometría/continuidad, instrumentación candidata y presupuesto de error preliminar. |

## Acuerdos entre módulos

1. M1/M2/M3/M5: velocidad, caudal, exposición y sincronización; caso nominal, pausa y fallo.
2. M1/M2/M3/M4: masa del cabezal, envolvente, montaje, tubos y coordenadas.
3. M5 con todos: datos, tiempos, calibración, validez y visibilidad.
4. M4 con todos y host: masa, potencia, energía, calor, volumen y comunicaciones.
5. M2/M3/M4/M5 y M1 cuando aplique: contención, emisión, apertura, pérdida de energía y estado seguro.

Una propuesta puede avanzar con supuestos visibles. Las interfaces requieren revisión de todos los afectados según la guía del repositorio.

## Orden del informe

Introducción y contexto; objetivos e innovación; viabilidad técnica/económica/ambiental; diseño y requisitos de misión/sistema con verificación; mercado y costes; riesgos y mitigaciones; equipo y cronograma; conclusiones y pasos hacia PDR. Añadir una tabla «observación del jurado → respuesta propuesta → evidencia → pendiente».

Para el guion: 1 min problema/experimento; 2 min observaciones y respuesta; 3 min arquitectura y módulos; 2 min viabilidad/recursos/riesgos; 1 min mercado/valor; 1 min cronograma y próximos pasos. Es una propuesta editorial que se ajustará al contenido disponible.

## Criterio de cierre del borrador

- Aportes de todos los módulos, decisiones y supuestos claramente identificados.
- Requisitos con criterio, fuente/razón y método de verificación; sin cumplimiento inventado.
- Recursos integrados con trazabilidad y sin duplicar masa o sumar picos sin secuencia.
- Riesgos, controles propuestos y evidencias pendientes enlazados.
- Respuesta explícita a críticas del brazo y de emisiones.
- Informe, visualización y guion coherentes; mercado/costes y cronograma incluidos.
- Pendientes críticos con responsable y fecha acordada. Una casilla vacía no se sustituye por una aprobación ficticia.
- Revisión de otra persona antes de integrar cambios técnicos importantes y congelar la versión.

## Fuentes de planificación

[Plantilla oficial del informe SRR](https://docs.google.com/document/d/1VEZzT6vw134w6CKLxHCs_u7poRDYHhSM/edit), [lineamientos de Review 2](https://docs.google.com/document/d/12ZDWNiUHeyCW8tckpVIAnYeAPqpNIW_J/edit), evaluación de AEGINS de Review 1 consultada en Drive, y documentos de este repositorio. Los documentos del programa determinan el alcance de entrega; el índice previo del repo no sustituye la plantilla oficial.

## Seguimiento de la evaluación de expertos

La [matriz de respuesta a Review 1](respuesta_expertos.md) desarrolla las dos opiniones del documento Evaluation Grid localizado en AEGINS. Prioriza comparación del mecanismo, inventario de emisiones y controles de seguridad con su impacto en costes. Su fuente es MDR / Review 1, no un SRR ya evaluado. Integrar esta matriz en el informe y en el guion sin presentar trabajo pendiente como avance verificado.

## Controles persistentes propuestos

La [propuesta de reglas y controles](https://github.com/eidanYT/Aegins-Project/pull/2) añade AGENTS.md, ámbitos, registros de ejecución y CI. Su comprobación inicial en GitHub Actions pasó, pero todavía requiere revisión independiente e integración; la conexión actual no permite configurar protección de main. El prompt técnico incorpora el prefijo tecnico/ y recuperación de contexto. No se declara bloqueo administrativo activo.
