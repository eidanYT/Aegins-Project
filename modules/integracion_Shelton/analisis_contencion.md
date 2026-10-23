# M4 — Modelos paramétricos de contención y recursos

**TBR; derivaciones analíticas, sin entradas de emisión ni diseño de vuelo seleccionados.** Implementación: [calculos.py](../../models/srr_integracion/calculos.py).

## Balance de una especie

Para masa de contaminante m en un volumen libre V, C=m/V en kg/m³. Bajo mezcla homogénea, volumen constante, fuente constante G en kg/s y ausencia de eliminación/fugas: C(t)=C₀+Gt/V.

La ecuación muestra qué entradas faltan: especie, generación, concentración inicial, tiempo y volumen libre. No se han asignado valores a esas entradas. La mezcla homogénea y fuente constante requieren justificación; no se extrapola a aerosoles, superficies, adsorción, procesos reactivos o transitorios sin modelo adicional.

Para una ruta con eliminación, el balance debe incluir entrada/salida, retención por especie y capacidad variable. La elección y eficacia de tratamiento siguen pendientes de material/host. Un sensor genérico o una cámara cerrada no demuestran que una especie peligrosa esté dentro del límite aceptable.

No convertir este modelo en un límite de exposición: faltan criterio del host, evaluación toxicológica y verificación experimental específica.

## Masa inicial de paneles

Para un recinto rectangular de dimensiones L,W,H, pared delgada t y densidad ρ: m_paneles≈2(LW+LH+WH)tρ. Todas las longitudes se introducen en m y la densidad en kg/m³.

Es un modelo geométrico ideal de pared delgada, no un cálculo de resistencia. Añadir puerta, marcos, sellos, ventanas, pasamuros, fijaciones, instrumentos y soportes, y corregir aperturas. No se han seleccionado dimensiones/material/espesor, ni se ha dimensionado un recipiente a presión.

## Potencia, energía y calor

Usar una línea de tiempo común. Para tramos no superpuestos: E=ΣP_promedio,i·Δt_i en J. Para mostrar Wh, dividir J entre 3600; los valores internos permanecen SI.

La potencia eléctrica simultánea se suma por estado, no como suma indiscriminada de máximos independientes. La transferencia de calor al host depende de almacenamiento térmico, proceso y ruta de disipación; no se iguala automáticamente a la potencia instantánea.

## Verificación y siguiente paso

Las pruebas del código comprueban conservación de masa, condiciones iniciales, entradas inválidas y sumas de energía. Esas comprobaciones prueban las relaciones programadas bajo sus hipótesis, no el comportamiento de una cámara real.

M2 aporta inventario/emisiones; M1 recorrido/cargas; M3 calor/UV; M5 instrumentos y registro; el host establece sus asignaciones. Hasta recibirlos, no se publica un total numérico de cámara ni un criterio de exposición.
