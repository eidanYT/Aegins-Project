# Presupuestos
Separar: entrega CAD/análisis; demostrador terrestre; futuro equipo de vuelo.
Moneda y fecha de referencia por partida. No declarar un precio histórico como cotización actual.

| Paquete | Masa kg | Potencia normal W | Pico W y duración s | Energía por ciclo Wh | Calor a host W | Volumen m³ | Coste y moneda | Fuente/estado |
|---|---|---|---|---|---|---|---|---|
| M1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| M2 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| M3 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| M4 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| M5 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

No sumar picos como si fueran simultáneos sin secuencia; no equiparar electricidad consumida y calor instantáneo en cada interfaz.
Registrar masas de cables, mangueras, fijaciones y material; evitar contarlas dos veces.
M4 integra recursos; cada paquete responde por sus datos.
Reservas: indicar cantidad, razón y madurez. Ningún porcentaje genérico sustituye el análisis.
Coste de vuelo: además de BOM, ingeniería, fabricación, instrumentación, pruebas, documentación, integración y operación; si no hay cotización, dejar estimación con base o TBD.

## Entradas de M4/M5 para la primera integración

Estado TBR; no hay material, cámara, controlador ni sensores elegidos. Se publican métodos y fuentes requeridas, no cifras de hardware.

| Módulo / partida | Qué falta | Fuente y método |
|---|---|---|
| M4 cámara/base/cierre | Dimensiones, material, espesor, masas y cargas | Propuesta M1/host; modelo de paneles y masa por componentes |
| M4 ventanas/pasamuros/tubos/retención | Compatibilidad, recorrido, inventario y conexiones | Fichas M2/M3/M5 y diseño revisado |
| M4 gases/térmica | Generación por especie, capacidad/ruta, calor y potencia por estado | M2/M3/host; balances condicionados |
| M5 control y adquisición | Modelos, interfaces, potencia/pico y duración | Fichas/modelos elegidos y secuencia |
| M5 cámaras/datos | Píxeles, profundidad, frecuencia, cámaras y duración | Requisitos de medida y fichas; tasa bruta = píxeles·bits/píxel·frecuencia·cámaras |
| M5 calibración/ensayos/operación | Patrones, montaje, verificación, trabajo e integración | Plan de ensayo y coste de ciclo de vida, con fecha/moneda |

Calcular energía internamente en J desde la línea de tiempo; 1 Wh = 3600 J para presentación. No publicar un total como cero cuando faltan partidas.

Vínculos: [M4](../modules/integracion_Shelton/propuesta.md), [M5](../modules/control_metrologia_Eidan/propuesta.md) y [modelos paramétricos](../models/srr_integracion/README.md).
