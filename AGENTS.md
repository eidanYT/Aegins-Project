# Reglas de trabajo de AEGINS

Estas reglas conservan el contexto de FORGE-UG entre tareas. Leer también CONTRIBUTING.md, management/agent_guardrails.md y el registro de ejecución de la tarea. El usuario define el objetivo; las reglas del repositorio no autorizan operaciones fuera de ese objetivo.

## Antes de editar
- Leer misión, requisitos, pendientes y las interfaces afectadas desde la versión vigente. Comparar main y los PR abiertos.
- Trabajar en rama propia: tecnico/ para M1/M2/M3; integracion/ o docs/srr- para M4/M5 y documentos comunes; gobernanza/ para cambiar estas reglas.
- Crear o actualizar el registro management/agent_runs/<rama-con-barras-reemplazadas-por-guiones-bajos>.json usando la plantilla. Mantener objetivo, avances, fuentes, decisiones abiertas, siguiente acción y revisores.
- Al reanudar una tarea, recuperar el estado del registro y contrastarlo con los archivos y el PR. El registro no sustituye la lectura del trabajo real.

## Reparto
- Técnico: movimiento_NICOMANUQP, extrusion_Gabriel, uv_termica; models/srr_agente_tecnico y reviews/SRR/aportes_agente_tecnico.md.
- Integrador: integracion_Shelton, control_metrologia_Eidan, system, interfaces, gestión, paquete SRR y CAD/evidencias de integración.
- El técnico propone datos para documentos comunes en su aporte; el integrador revisa su coherencia antes de incorporarlos.
- Las ramas no bloquean por sí mismas otros editores. Reservar trabajo mediante el registro y revisar PR abiertos. Cambiar reparto requiere acuerdo explícito y revisión de la política.

## Integridad técnica
- Mantener estados EJEMPLO, TBD, TBR, APROBADO y VERIFICADO separados. Una revisión documental no valida desempeño físico.
- Toda cifra relevante necesita unidad, condiciones, fuente y estado. Registrar estimaciones nuevas en estimates del registro; no inventar datos para completar tablas.
- Una afirmación verificada necesita método, evidencia enlazada y alcance. La CI verifica estructura y presencia, no verdad científica.
- El caso config/caso_demo.json sigue siendo didáctico. No reemplazar sus datos por la pieza propuesta ni convertirlo en un caso aprobado.
- Plataforma: estación y satélite son alternativas abiertas hasta registrar D-001. No asumir ISS, vacío, presión de cabina ni interfaces de gases disponibles.
- Pieza propuesta por Eidan: dos pirámides unidas por la base, cada arista 0,05 m. Base y tipo de impresión por precisar; no asumir octaedro.
- Cámara y salida de gases son propuestas: no declarar protección de tripulación ni tratamiento eficaz sin evidencia.
- Conservar respuesta al jurado: comparación del brazo, emisiones de gases/polvo y seguridad con efectos en recursos/costes.
- Un parámetro común tiene una fuente de verdad. Actualizar impactos, requisitos e interfaces al proponer cambios.

## Cambios y revisión
- No escribir directamente en main, forzar referencias, borrar ramas ajenas, autoaprobar ni integrar sin la revisión independiente requerida.
- No modificar controles (.github, AGENTS.md, política, validador o pruebas) desde ramas técnicas o de integración.
- Abrir PR con fuentes, límites, registro de tarea y preguntas por módulo. Las interfaces requieren conformidad explícita de los afectados.
- Ejecutar las comprobaciones correspondientes. Registrar fallos y trabajo pendiente sin marcarlo terminado.
- No enviar mensajes a personas o a otras conversaciones sin autorización humana explícita.
- No incluir credenciales ni datos privados ajenos al proyecto en el repositorio.

## Límites de estas reglas
AGENTS.md aporta instrucciones, no permisos ni una barrera inviolable. La protección real depende de GitHub, revisores independientes y credenciales sin administración/bypass. Un administrador que controla el repositorio puede alterar esa protección.
