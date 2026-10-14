# Candidatos M5 para demostrador terrestre

**TBR; selección pendiente.** Consultados el 12 de octubre de 2026. Estas opciones concretan la arquitectura para comparar prestaciones y costes. No son una lista de compras ni componentes calificados para estación espacial.

| Función | Candidato | Razón para evaluarlo | Condiciones antes de seleccionar |
|---|---|---|---|
| Control/adquisición de proceso | Teensy 4.1 | El fabricante documenta temporizadores, interfaces serie y watchdogs | Compatibilidad eléctrica, interfaces de M1/M2/M3, comportamiento al reiniciar, temporización medida y respuesta física externa |
| Visión y registro | Raspberry Pi 5; alternativa: ordenador disponible del equipo | La ficha documenta interfaces de cámara y periféricos; permite evaluar una plataforma separada para visión | Medir carga, calor, consumo, pérdidas de datos y retrasos con la configuración real; no atribuir tiempo real garantizado a una placa |
| Imagen | Raspberry Pi Global Shutter Camera | Obturador global y óptica intercambiable como opciones frente a distorsión temporal y campo de visión | Lente, enfoque, iluminación, montaje, cable adecuado, acceso óptico, calibración y sincronización; comprobar zonas ocultas y reflejos |

Fuentes primarias: [PJRC Teensy 4.1](https://www.pjrc.com/store/teensy41.html), [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/), [Global Shutter Camera](https://www.raspberrypi.com/products/raspberry-pi-global-shutter-camera/). Las funciones propuestas son interpretación de integración; las fichas no demuestran cumplimiento del experimento.

El obturador global no sincroniza por sí mismo dos cámaras ni determina precisión tridimensional. Una cámara candidata tampoco resuelve la inspección del interior o del espesor de las caras cerradas.

Comparar primero una prueba con patrón independiente y pieza representativa: cobertura visible, incertidumbre, pérdida de imágenes, alineación temporal y datos de recursos. El mecanismo/controlador de movimiento se coordina con M1; no se elige desde M5.

Mantener sensores de presión, temperatura y contaminantes sin modelo seleccionado hasta recibir rangos, material y peligros de M2/M3/M4. La potencia de una fuente recomendada no es el consumo medido del sistema. Costes necesitan cotización local, accesorios y fecha; no hay coste total sustentado todavía.
