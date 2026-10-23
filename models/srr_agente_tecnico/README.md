# Modelos técnicos del brazo 6R

La referencia actual exige seis articulaciones revolutas, posición TCP y orientación completa, incluyendo giro axial. No existe todavía en este directorio un simulador 6R integrado ni evidencia de trayectoria ejecutable.

El nuevo modelo debe derivarse del CAD dimensionado y publicar marcos, límites, masas e inercias, FK/IK, trayectoria continua y temporizada, colisiones, singularidades, cargas y recorrido de tubos. El extrusor y UV se integran con un reloj común, sin confundir caudal con una articulación del brazo.

[Objetivos M1](../../modules/movimiento_NICOMANUQP/README.md) · [Objetivos M2](../../modules/extrusion_Gabriel/README.md) · [Objetivos M3](../../modules/uv_termica/README.md) · [Fuentes técnicas](fuentes.md).

Los valores de geometría, caudal y exposición del SRR son referencias condicionales de proceso y se recalculan con las entradas del caso actual. No se transfieren resultados cinemáticos anteriores al brazo adoptado.
