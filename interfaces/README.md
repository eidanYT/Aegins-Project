# Interfaces: acuerdos entre módulos

Una interfaz describe qué necesita un módulo del otro y qué le proporciona: datos, conexiones, montaje, recursos o reacción ante fallos. Escribe aquí el acuerdo compartido y enlázalo desde tu propuesta.

## Abre el documento que necesitas

| Documento | Módulos que revisan | Qué acordar | Qué mostrar para revisarlo |
|---|---|---|---|
| [ICD-001](ICD-001.md) | M1 / M2 / M3 / M5 | Velocidad, caudal, UV y secuencia temporal | Caso nominal, cambio de velocidad y parada; hipótesis y retardos |
| [ICD-002](ICD-002.md) | M1 / M2 / M3 / M4 | Montaje del cabezal, masa, cables/tubos y coordenadas | Envolvente, recorrido y tabla de cargas |
| [ICD-003](ICD-003.md) | M5 / M1 / M2 / M3; M4 para visibilidad y montaje | Señales, unidades, adquisición, tiempo, validez y calibración | Diccionario y registro de ejemplo |
| [ICD-004](ICD-004.md) | M4 / M1 / M2 / M3 / M5 y plataforma | Montaje y recursos: masa, potencia, calor y comunicaciones | Asignaciones, fuentes, presupuestos e incertidumbre |
| [ICD-005](ICD-005.md) | M2 / M3 / M4 / M5; M1 cuando afecta al movimiento | Contención, fallos y estado seguro | Escenarios de fallo y respuesta coordinada |

Los cinco archivos ya están creados. ICD-001 conserva el caso didáctico; los demás son borradores sin valores aprobados.

## Cómo proponer un cambio

1. Abre el ICD en la misma rama que tu propuesta y comprueba si hay una Issue/PR trabajando el punto.
2. Completa el intercambio, unidades, condiciones, rangos, tiempos, fuente y fallo.
3. Añade las preguntas específicas en **Puntos pendientes de revisión**, con el nombre del miembro que las debe resolver.
4. Abre o enlaza una Issue de **Cambio de interfaz** y un PR con los archivos.
5. Solicita revisión; continúa trabajando con los supuestos marcados.
6. Registra respuestas, corrige y enlaza la conformidad de todos los afectados antes de integrar el acuerdo.

Puedes proponer una interfaz completa aunque los demás estén ocupados. Lo propuesto permanece TBR; no equivale a conformidad ni a verificación física.

Para una interfaz nueva, copia [templates/interfaz.md](../templates/interfaz.md) en `interfaces/ICD-006.md`, o usa el siguiente ID libre. Evita mantener versiones paralelas del mismo acuerdo.

## Ejemplo

M1 propone cambiar la velocidad. Gabriel revisa caudal; M3, exposición; Eidan, sincronización; Shelton, recursos si cambian. Registra cada pregunta en la tabla del PR y del ICD-001. El modelo puede analizar ambos casos mientras llega respuesta; el cambio no se aprueba con una contradicción abierta.

[Guía completa de revisión](../management/colaboracion.md) · [Contactos](../management/equipo.md) · [Volver al inicio](../README.md)
