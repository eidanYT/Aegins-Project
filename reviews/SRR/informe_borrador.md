# FORGE-UG — Borrador integrado SRR / Review 2

**Estado: TBR, primera entrega de M4/M5.** Equipo: AEGINS. Preparado por Codex a solicitud de Eidan, 12 de octubre de 2026. Revisión/autoría final del equipo: pendiente. Este texto es fuente para la plantilla oficial; no sustituye aún el informe maquetado ni garantiza su límite de 30 páginas.

## 1. Introducción

FORGE-UG estudia una propuesta de impresión 3D de material curable mediante UV en microgravedad. El experimento compara orientación fija y variable de la boquilla con condiciones y mediciones registradas; la hipótesis puede confirmarse, limitarse o rechazarse.

El escenario de referencia elegido por Eidan es un payload dentro de una cámara en una estación espacial con tripulación. La estación/alojamiento y recursos todavía no están elegidos. La seguridad frente a emisiones, residuos y fallos debe formar parte del diseño y de su evaluación de viabilidad.

## 2. Contexto, objetivos e innovación

La pregunta científica propuesta es cómo cambia el error geométrico al coordinar orientación, trayectoria, alimentación y UV. Debe justificarse el observable específico y el valor de estudiarlo en microgravedad con fuentes y un protocolo; no se afirma beneficio real antes de evidencia.

La pieza nominal será una bipirámide de base cuadrada, aristas de 0,05 m y caras cerradas. [Misión](../../system/mision.md), [caso](../../system/caso_srr.json) y [modelo nominal](../../cad/pieza_srr.md) definen el contexto. Espesor, material y criterios de calidad requieren propuestas revisadas.

## 3. Viabilidad

### Técnica

M4 compara cámara con retención/tratamiento interno y transferencia condicionada a un receptor del host. M5 compara control distribuido y un controlador integrado compatible, y desarrolla alternativas de medición exterior y por etapas.

Datos necesarios de M1/M2/M3: comparación del mecanismo, trayectoria de superficies, material y deposición de caras, exposición/curado, datos de presión/calor y requisitos de interfaces. Estas entradas todavía no se han integrado en esta primera entrega.

Hay geometría nominal y cálculos reproducibles de sensibilidad, no ensayos físicos ni simulación validada del proceso. Faltan datos que permitan demostrar fabricabilidad, seguridad y prestaciones.

### Económica y ambiental

La estructura de coste incluye desarrollo, fabricación, componentes, instrumentación, pruebas, integración, operación y recuperación/gestión de residuos. No hay presupuesto monetario sustentado todavía.

Inventariar material, consumibles, electricidad, residuos y emisiones. La propuesta de pieza cerrada no elimina contaminación ni obliga a ventear. Identificar rutas de gestión aceptadas por el host antes de afirmar sostenibilidad o ahorro.

### Resiliencia, modularidad y autonomía

El reparto modular permite revisar interfaces y alternativas. El modelo de estados incluye detección lógica de datos inválidos y recuperación autorizada propuesta. La respuesta real ante pérdida de energía, fallos o residuos requiere hardware y evidencia; no se declara autonomía o durabilidad verificadas.

## 4. Diseño y justificación

### Arquitectura preliminar

M1 movimiento; M2 material/extrusión; M3 UV/térmica; M4 cámara/integración; M5 control/metrología. M4 recibe datos de los módulos y del alojamiento; M5 coordina señales y conserva trazabilidad temporal.

[Propuesta M4](../../modules/integracion_Shelton/propuesta.md) y [propuesta M5](../../modules/control_metrologia_Eidan/propuesta.md) contienen alternativas, decisiones abiertas, recursos y preguntas de revisión. Son propuestas, no conformidades.

Los [candidatos de componentes M5](../../modules/control_metrologia_Eidan/candidatos_prototipo.md) se limitan a un demostrador terrestre y requieren comparación y pruebas antes de seleccionar. No se presenta esa lista como equipo de vuelo.

### Requisitos de misión y sistema

El [registro de requisitos](../../system/requisitos.md) conserva IDs y métodos A/T/I/D. Su refinamiento M4/M5 identifica criterios todavía abiertos. Para la exportación a la plantilla oficial se debe separar nivel de misión y sistema y mantener trazabilidad, sin renombrar IDs silenciosamente.

La selección de escenario no define límites de host; los ejemplos de metrología/tiempo no son requisitos de misión. Cada umbral futuro necesita fuente/razón, unidad, condiciones, método y criterio revisado.

### Geometría, interfaces y recursos

La pieza nominal tiene doce aristas únicas y ocho caras. El OBJ es una superficie nominal sin espesor ni trayectoria; la cámara debe incluir mecanismo, soporte, alimentación, UV, observación y acceso.

[ICD-003](../../interfaces/ICD-003.md): datos y tiempo. [ICD-004](../../interfaces/ICD-004.md): host/recursos. [ICD-005](../../interfaces/ICD-005.md): fallos/contención. Montaje/proceso en ICD-001/002 requiere aportes M1/M2/M3.

[Presupuestos](../../system/presupuestos.md) reúne partidas y métodos. No se publican masas/potencias/costes de equipos desconocidos ni totales que oculten datos faltantes.

### Medición y verificación

[Plan de metrología](../../modules/control_metrologia_Eidan/metrologia.md): exterior, aristas, espesor/interior, cobertura y calibración. [Evidencia](../../evidence/srr_integracion_calculos.md): geometría y conversiones con límites explícitos. Las verificaciones de hardware y seguridad quedan en un plan futuro con criterios por acordar.

## 5. Mercado y costes

Hipótesis de valor inicial: una capacidad experimental de fabricación en microgravedad y datos que permitan evaluar estrategias de proceso. Usuarios/interesados, competencia, necesidad concreta y modelo de servicio deben validarse; no se afirma tamaño de mercado ni retorno económico.

El equipo debe completar esta sección con antecedentes y comparaciones sustentadas. Los costes de contención, instrumentación y calificación deben incluirse junto a los del mecanismo/material; no publicar un coste de vuelo como suma de piezas terrestres.

## 6. Riesgos y respuesta a Review 1

La [matriz de expertos](respuesta_expertos.md) registra complejidad/adecuación del brazo, gases/polvo y ampliación de seguridad/costes. La respuesta se presenta como observación → propuesta → evidencia disponible → pendiente.

[Riesgos](../../system/riesgos.md) incluye coordinación, presión/material, calor, contaminación, tubos/cargas, energía/datos, metrología inválida y cierre de caras. Probabilidad/severidad y criterios de seguridad dependen del inventario y host; no se inventan valoraciones ni se declara mitigación validada.

## 7. Equipo, gestión y cronograma

El [equipo](../../management/equipo.md) mantiene responsables existentes. M3 y sistemas siguen por asignar. Las fechas oficiales y la prórroga no se confirman con este documento.

Ruta propuesta: completar datos M1/M2/M3 y host; revisar interfaces y presupuestos; preparar ensamble/CAD y métodos de medida; desarrollar prototipo y calibración; realizar ensayos y revisiones; evaluar integración/operación en estación con el host. Son fases condicionadas, no promesas de despliegue.

El [plan de hoy](plan_trabajo_hoy.md) organiza el borrador y exposición. Las reglas de agentes separan ámbito, contexto y CI; la configuración de main exige revisión/comprobación según la regla activa consultada. Eso no aprueba el diseño físico.

## 8. Conclusiones y próximos pasos

Esta primera entrega define el escenario, nominal de pieza y propuestas M4/M5, con modelos y contratos de integración revisables. El paso siguiente es incorporar datos técnicos de M1/M2/M3, cerrar decisiones y conformidades y completar la evidencia/viabilidad del conjunto.

Todavía no se demuestra impresión de caras, control físico, medida válida ni protección de tripulación. La decisión de avance a PDR debe considerar las incertidumbres y verificaciones pendientes, no solo la cantidad de documentos.

## Fuentes

Lineamientos y plantilla oficiales de Review 2 consultados en Drive; evaluación de AEGINS de Review 1; decisiones de Eidan; referencias NASA/NIST/OpenCV enlazadas en los documentos técnicos. La versión definitiva debe mantener citas y vínculos a cada dato/modelo utilizado.
