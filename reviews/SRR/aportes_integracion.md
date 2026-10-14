# Primera entrega de integración — M4 y M5

**TBR — revisión técnica pendiente.** Preparada el 12 de octubre de 2026. Rama integracion/m4-m5-srr. No representa diseño de vuelo aprobado.

## Decisiones de Eidan incorporadas

Referencia: estación espacial con tripulación y cámara interna. Pieza: bipirámide de base cuadrada, todas las aristas de 0,05 m y caras cerradas. Material, espesor, host y hardware no elegidos.

[SRR-GEO-001](../../system/caso_srr.json) es la fuente común del nominal; no sustituye el caso didáctico. [Pieza derivada](../../cad/pieza_srr.md) y OBJ/SVG disponibles.

## Entregas

| Elemento | Archivo | Qué aporta |
|---|---|---|
| M4 | [Propuesta](../../modules/integracion_Shelton/propuesta.md) | Cámara y alternativas de gases; integración, recursos y revisión |
| M5 | [Propuesta](../../modules/control_metrologia_Eidan/propuesta.md) | Arquitectura, instrumentación por función, control y requisitos |
| Medición | [Metrología](../../modules/control_metrologia_Eidan/metrologia.md) | Aristas/exterior/espesor/interior, cobertura, calibración e incertidumbre |
| Interfaces | [Datos](../../interfaces/ICD-003.md), [host](../../interfaces/ICD-004.md), [fallos](../../interfaces/ICD-005.md) | Contratos propuestos sin cifras arbitrarias |
| Modelos | [README](../../models/srr_integracion/README.md) | Geometría, sensibilidad temporal, balances y estados |
| Evidencia | [Cálculos](../../evidence/srr_integracion_calculos.md) | Conversiones y pruebas bajo hipótesis; no ensayos físicos |
| Informe | [Borrador integrado](informe_borrador.md) | Contenido inicial para la plantilla oficial, con dependencias explícitas |
| Seguimiento | [Pendientes](../../system/pendientes.md) | Responsables propuestos y preguntas abiertas |

## Respuesta a los expertos

- Brazo: el otro agente debe comparar alternativas y justificar orientación; M4 solicita volumen barrido/cargas y M5 marco/datos.
- Gases/polvo: M4 propone cámara y rutas condicionadas al material/host; no declara una solución verificada.
- Seguridad/costes: se amplían peligros y partidas de recursos, acceso y pruebas. No se asignan costes sin componentes/fuentes.
- Caras cerradas: se añade formación de superficies, espesor, curado, gas/residuo interno e inspección por etapas a los datos requeridos del equipo técnico.

## Lo que falta para cerrar el diseño

La entrega del otro agente ya fue contrastada e incorporada documentalmente en [consolidación de los cinco módulos](consolidacion_modulos.md). Sus hipótesis no se convierten en selecciones ni conformidades. El informe común y los ICD-001/002 incorporan sus impactos de proceso y montaje; los módulos M1/M2/M3 conservan su propia rama.

M1: trayectoria/anclaje/recorrido/cargas. M2: material, formación de caras, espesor, inventario/emisiones y transitorios. M3: espectro, exposición, sombras, curado y calor. Host: asignaciones, gases, seguridad y operación. M5: métodos/criterios e instrumentación y calibración. M4: dimensionamiento y ruta aceptada.

Las pruebas de código no demuestran seguridad de tripulación, fabricabilidad, exactitud real ni aptitud de vuelo. Conformidades y pruebas siguen pendientes.
