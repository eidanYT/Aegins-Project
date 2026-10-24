# Registro CAD del brazo 6R y ensamble

Herramienta elegida: SolidWorks. Nicolas y Gabriel preparan el CAD preliminar con apoyo de Eidan; Andres aporta dimensiones y espacios de instalación. Eidan utiliza la geometría para los modelos matemáticos y la simulación. La primera versión incluye medidas principales, seis ejes y ubicaciones de componentes; los planos de fabricación y tolerancias se profundizan después. [Reparto vigente](../system/reparto_trabajo_2026-10-24.md).

Meta: una fuente paramétrica controlada para brazo, muñeca, cabezal, tubos, cámara, montaje y retención de lanzamiento. No se ha creado CAD de fabricación en esta actualización de objetivos.

| Conjunto | Datos exigidos | Módulos que aceptan | Estado |
|---|---|---|---|
| Brazo 6R y muñeca | Piezas, ejes, ceros, offsets, límites, tolerancias, ajustes, masa/CG/inercia | M1 con M2/M3/M4/M5 | Pendiente |
| Extrusor y alimentación | Brida, TCP, volumen muerto, conexiones y tubos móviles | M2 con M1/M3/M4 | Pendiente |
| Óptica y térmica | Volumen UV, sombras, sensores y ruta conductiva | M3 con M1/M2/M4/M5 | Pendiente |
| Cámara y transporte | Base, paneles, puertas, filtros, arnés, fijación y bloqueos | M4 con todos | Pendiente |
| Metrología | Posiciones, campos de visión, calibración y ventanas | M5 con M4/M1 | Pendiente |

Cada versión enlaza archivos nativos, STEP, planos, BOM y exportación cinemática. Registrar unidades, marcos, fecha, revisión y commit. Comprobar que masas/inercias del robot y la malla FEA corresponden al mismo CAD. [Criterios avanzados](../system/objetivos_pdr_y_desarrollo.md).
