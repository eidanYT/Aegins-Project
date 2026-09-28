# Modelo mínimo para coordinar paquetes
Entrada única del ejemplo: config/caso_demo.json.
No incluye un controlador ni un simulador físico validado.

## Cálculos nominales
A = πd²/4; Q = A v; t_exp = L/v; H = E t_exp; desplazamiento_por_desfase = v Δt.
Q se obtiene en m³/s; H en J/m².
Conversiones: 1 m³/s = 10^9 mm³/s = 6×10^7 mL/min.
1 W/m² = 0,1 mW/cm²; 1 J/m² = 0,1 mJ/cm².

Salida esperada con el ejemplo:
- Q ≈ 5,655×10^-9 m³/s = 5,655 mm³/s = 0,3393 mL/min.
- t_exp = 0,4 s.
- H = 1000 J/m² = 100 mJ/cm².
- Desplazamiento por desfase = 0,00025 m = 0,25 mm.

Aplicabilidad: cordón nominal circular, flujo estacionario incompresible sin pérdidas/acumulación y velocidad de formación aproximada por la de trayectoria.
Para el equipo real deben considerarse expansión, contracción, deformación, burbujas, transitorios y velocidad efectiva del material.
La exposición requiere integrar E a lo largo del movimiento real; no predice por sí sola conversión o resistencia.
Si cambian config, recalcular y registrar la evidencia con el commit correspondiente.

## Próximos modelos
M1: cinemática y cargas; incluir acoplamiento a nave si aplica.
M2: presión/caudal y respuesta temporal.
M3: distribución óptica, cinética y balance térmico según datos disponibles.
M4: presupuestos y escenarios de contención.
M5: latencias, incertidumbre metrológica y estados.
No introducir multiphysics complejo antes de identificar entradas confiables y la pregunta que resolverá.
