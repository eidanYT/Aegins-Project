# Ejemplo completo de trazabilidad: metrología y sincronización

**Estado: ejercicio de trabajo TBR, no especificación aprobada de FORGE-UG.** Los números sirven para aprender a derivar requisitos; el equipo debe justificar o reemplazarlos.

## Necesidad científica
Supongamos que el equipo decide que una diferencia de 0,5 mm en el error de trayectoria sería científicamente relevante. Esa cifra necesita una razón vinculada al tamaño y función de la pieza; no se toma de una norma.

## Requisito de medida propuesto
MET-DEMO-01: el método de reconstrucción deberá tener una incertidumbre expandida de posición no superior a 0,10 mm, con factor de cobertura k = 2 declarado, en el volumen de medida de la probeta.

La asignación de 0,10 mm equivale a una quinta parte de la diferencia relevante supuesta. Es una elección para discusión, no una regla estadística universal; no garantiza potencia suficiente para detectar diferencias entre grupos.

Responsable: M5. Padre: SCI-002. Afectados: M1/M3/M4. Estado: TBR.

## Candidatos y selección
Opción A: dos cámaras calibradas con reconstrucción estéreo.
Opción B: una cámara calibrada con vistas sucesivas, solo si la geometría, visibilidad y estabilidad permiten reconstruir lo necesario.
Son arquitecturas candidatas; faltan modelo, óptica, iluminación, calibración y coste.

En una vista ortogonal ideal de 100 mm de ancho y 1920 píxeles, la escala nominal es 100/1920 = 0,0521 mm/píxel. Esto NO demuestra incertidumbre de 0,10 mm: profundidad, distorsión, calibración, enfoque, movimiento y segmentación también aportan error.

## Interfaces condicionantes
- M1 entrega trayectoria nominal y transformaciones de coordenadas, sin asumir que su encoder mide el cordón.
- M3 especifica luz UV y posibles interferencias con la adquisición.
- M4 proporciona campo de visión, ventanas, montaje y estabilidad.
- M5 define sincronización, formato de imagen, calibración y reconstrucción.

## Verificación y evidencia
Para SRR: presupuesto de incertidumbre que identifique contribuciones y datos faltantes. Para PDR: simulación geométrica de cobertura y sensibilidad de calibración. Para un prototipo futuro: medir un patrón de dimensiones conocidas en varias posiciones y orientaciones, cuantificar sesgo/repetibilidad y contrastar con un patrón independiente.

EV-MET-01 debe registrar calibración, trazabilidad del patrón, condiciones, método, resultados, incertidumbre y limitaciones. El cálculo de tamaño de píxel aislado no permite cerrar MET-DEMO-01.

## Trabajo en GitHub
Issue: “Definir presupuesto de incertidumbre para SCI-002”.
Rama: m5/presupuesto-metrologia.
Archivos: ficha de candidato, ICD-003, presupuesto de error y evidencia.
Revisores: M1 para coordenadas; M3/M4 para luz, visibilidad y montaje.
Terminado para SRR: arquitectura preliminar y presupuesto revisados, con TBD asignados. El ensayo sigue pendiente; se registra como tal.

## Ejemplo paralelo de sincronización
Si el equipo asignara 0,10 mm del error a un desfase temporal durante un tramo a 5 mm/s, el límite nominal sería Δt ≤ 0,10/5 = 0,020 s, es decir 20 ms.
El límite corresponde a ese supuesto y velocidad. La regla general usa la velocidad máxima aplicable y considera aceleraciones; tampoco corrige automáticamente el retraso hidráulico ni errores de reloj.
Esta derivación ayuda a M5 a seleccionar adquisición/control y a M2 a evaluar compensación del retardo. Debe quedar vinculada a ICD-001.
