# Modelo preliminar M1–M3 del SRR

Versión 0.1, 2026-10-12. **Análisis sintético EJEMPLO/TBR; revisión independiente pendiente.** No contiene ensayos, curvas de material ni un ensamble CAD. Los resultados son candidatos para revisión del integrador, con [fuentes y acceso](fuentes.md).

## Reproducir y revisar

Requiere Python 3 y biblioteca estándar. Desde la raíz del repositorio:

```text
python models/srr_agente_tecnico/calculos.py
```

Lee [entradas.json](entradas.json); genera [resultados.json](resultados.json), [raster.csv](raster.csv), [poses.csv](poses.csv) y [bipiramide.obj](bipiramide.obj). El hash de las entradas queda en resultados: JSON canónico UTF-8, claves ordenadas y separadores compactos, independiente de los saltos de línea de Windows/Linux. Todos los archivos geométricos usan **metros**; CSV de articulaciones usa radianes. El OBJ es una superficie externa ideal cerrada, sin espesor, fijación, tolerancia ni máquina: sirve de referencia para el CAD de integración.

El programa termina con error si falla una comprobación. Se contrastan área por productos vectoriales con ocho triángulos equiláteros, volumen por tetraedros orientados con dos pirámides, cierre/Euler y longitudes. La cinemática inversa se contrasta con la directa. Son comprobaciones internas del mismo autor; **no una segunda revisión independiente**. Otro revisor debe contrastar fuentes, reconstruir fórmulas/dimensiones y revisar hipótesis antes de incorporar los valores.

## Entradas, unidades y modelo

Cada entrada numérica declara valor SI, unidad, condición, fuente y estado en el JSON. La bipirámide cuadrada de arista a tiene vértices (±a/2, ±a/2, 0) y ápices (0,0,±a/√2). No se adopta globalmente esta geometría ni una plataforma: es el caso condicional permitido por el prompt original, coincidente con aclaraciones posteriores de Eidan que aún deben registrarse en documentos comunes.

| Magnitud | Fórmula y comprobación dimensional | Límite |
|---|---|---|
| Área / volumen exterior / aristas | A=2√3 a² [m²]; V=√2 a³/3 [m³]; L=12a [m] | V es volumen **encerrado**, no consumo de resina. |
| Aristas circulares | Ac=πd²/4 [m²]; Q=Ac v [m³/s]; Vc=Ac L | Diámetro depositado no necesariamente coincide con boquilla. Sin deformación, intersecciones ni contracción. |
| Caras por raster | Ac=w t [m²]; Q=wtv. N=ceil(h/w), h=√3 a/2. Pistas al centro de N bandas; Lr=8aN/2 | Se necesita proceso que permita depositar cada pista. No simula mojado, autoapoyo, uniones ni hermeticidad. |
| Pared delgada | Vpared≈A t [m³] | Primera aproximación; no suma aristas y no corrige esquinas. El raster tiene solape. |
| Presión de sensibilidad | ΔP=8ηLQ/(πr⁴): [Pa·s][m][m³/s]/[m⁴]=[Pa] | Flujo newtoniano, laminar, estacionario y tubo circular. GE680 no queda caracterizado así; no es presión de diseño. |
| Pistón | u=Q/Ap [m/s], F=ΔP Ap [N], Ph=ΔP Q [W] | Excluye sellos, fricción, cumplimiento, gas/burbujas, motor y transitorios. |
| Exposición | tex=Luv/v [s]; H=Etex [J/m²] | Irradiancia uniforme hipotética, sin cinética ni sombras. |
| LED / calor | Pel=nIV [W]; Popt=nΦ [W]; Pj=Pel−Popt [W]; energía=Pel t [J] | Valores típicos de referencia, driver y reacción no incluidos. No predice temperatura de unión. |

Conversiones: 1 mm=10⁻³ m; 1 mL=10⁻⁶ m³; 1 g/cm³=1000 kg/m³; 1 mPa·s=1 cP=10⁻³ Pa·s; 1 mW/cm²=10 W/m²; 1 mJ/cm²=10 J/m²; 1 bar=10⁵ Pa; grados=radianes·180/π.

## Resultados del caso 0.1

Todas las cifras siguientes son **resultados de análisis condicional, TBR**, salvo la dosis didáctica EJEMPLO. Redondeo para lectura; JSON conserva precisión numérica.

| Resultado | Valor / unidad / condición |
|---|---|
| Geometría | 6 vértices, 12 aristas, 8 caras; envolvente 50×50×70,71 mm; A=0,00866025 m²; volumen encerrado 58,9256 mL |
| Aristas | L=0,600 m; Q=5,65487×10⁻⁹ m³/s=0,339292 mL/min; volumen 0,678584 mL; tiempo ideal 120 s |
| Caras, w=1,2 mm, t=0,5 mm | 37 pistas/cara, paso 1,17030 mm; L=7,400 m; Q=3,00×10⁻⁹ m³/s=0,180 mL/min; volumen 4,440 mL; tiempo ideal 1480 s |
| Inventario ilustrativo | Aristas+caras sin descontar cruces: 5,11858 mL; +20%: 6,14230 mL, masa GE680 condicional 0,0108104 kg. Añadir cebado/volumen muerto. |
| Tubo remoto supuesto | Radio interior 2 mm, L=0,5 m: retiene 6,28319 mL, mayor que la reserva anterior. Total parte+reserva+tubo=12,4255 mL, sin otros volúmenes muertos. |
| Depósito hipotético | 20 mL de resina: 0,0352 kg. Pistón Ø20 mm: carrera útil ideal 63,662 mm; carcasa/actuador no incluidos. |
| ΔP aristas / caras | 84300 / 44722,5 Pa; fuerza ideal 26,4836 / 14,0500 N. Es sensibilidad con η=54 Pa·s constante, **no** límite operativo. |
| Poses del brazo ideal | 888 muestras en raster: todas dentro de límites propuestos; residuo directo/inverso <10⁻¹² m y <10⁻¹² en vector dirección. Sin comprobación de colisiones ni continuidad. |
| UV didáctico | 0,4 s; H=1000 J/m²=100 mJ/cm². No ventana material acreditada. |
| 4 LED equivalentes, típicos | Pel=15,4 W; Popt=5,16 W; calor local LED=10,24 W. Encendidos durante 1600 s: 24640 J=6,8444 Wh, sin driver/otros tiempos. |

**No sumar una sección circular de 1,2 mm como si fuera una pared de 0,5 mm.** El modelo distingue modos arista y cara. Ni el archivo de raster ni el OBJ prueban superficies imprimibles, cerradas o estancas. El tiempo 1600 s=26,667 min excluye traslados, aceleración, pausas, postcurado, inspección y recuperación.

## Cinemática y alcance

Brazo matemático de 5 articulaciones: Rz(q1), Ry(q2), Ry(q3), Rz(q4), Ry(q5), con enlaces +x de 0,12/0,10 m y herramienta +z de 0,03 m. Base en (−0,12,0,0) m. Cada pista se evalúa en sus dos extremos y centro; punta a 1 mm de la cara y eje dirigido hacia ella. Se resuelve centro de muñeca pW=pTCP−ltool d, yaw, hombro/codo por ley de cosenos y dos giros de muñeca para d. Límites **supuestos**: codo hasta 150°, demás ±180°.

Tres coordenadas de posición y dos de dirección justifican **cinco variables de tarea** para herramienta axialmente simétrica. No prueban que cualquier brazo comercial de cinco ejes satisfaga todas las poses. El sexto giro solo se justifica con orientación alrededor de la boquilla: óptica asimétrica, mangueras, cámara o necesidad de evitar obstáculos.

El q4 calculado toca ±π: hay que desenvolver ángulos y revisar pasos entre caras, topes/cables y reinicio sin extruir. Indicador mínimo |sin(q5)|≈0,300 en muestras; no es un análisis completo de singularidades/Jacobiano. El brazo carece de cuerpos, rigidez, actuadores y holguras. No garantiza trayectorias continuas, margen de colisión, precisión ni reacciones compatibles con el host.

## Iluminación y térmica

Mapa angular **sintético**: luz paralela desde +z, Eface=E0·max(0,nz). Las cuatro caras superiores tienen factor 1/√3≈0,577; las inferiores 0. No incluye reflexión ni oclusión por brazo/anclajes, que pueden reducir más la exposición. Orientar el cabezal normal a cada cara elimina esta pérdida angular ideal, no las sombras reales. Se debe medir E(x,y,z,λ) y usar H=∫E(t)dt; no deducirlo de vatios ópticos totales.

Balance preliminar C dT/dt=Pj+Pdriver+Preacción−G(T−Tbase)−εσA(T⁴−Tenv⁴). Preacción=caudal másico·entalpía efectiva solo si se conoce conversión/cinética. No se ha medido C, G, ε, reacción ni límites. Si toda la luz queda absorbida dentro del recinto, también termina como calor; carga del conjunto ≈Pel más pérdidas de driver y reacción, mientras Pj es únicamente calor local LED. No asumir convección natural terrestre en microgravedad; ventilación forzada sería una interfaz por acordar.

Sensibilidad EJEMPLO: con 10,24 W locales y G=0,1/0,5/1 W/K, ΔT estacionaria simplificada=102,4/20,48/10,24 K. Excluye radiación/reacción/driver y no predice temperatura real. El integrador debe asignar ruta conductiva, capacidad térmica, disipación y límites antes de declarar THM-001 satisfecho.

## Próxima verificación y entregas

M1: CAD con cuerpos, colisiones, anclaje y tubos, continuidad y dinámica. M2: SDS/TDS actuales, reología, respuesta presión/caudal, compatibilidad y emisiones. M3: espectro/mapa óptico y criterio de gel/resistencia del material; calor y protección. Revisor independiente por acordar con NICOMANUQP/Gabriel/M3 y coordinación. La conformidad de interfaces sigue pendiente.

[Síntesis para integración](../../reviews/SRR/aportes_agente_tecnico.md) · [M1](../../modules/movimiento_NICOMANUQP/propuesta.md) · [M2](../../modules/extrusion_Gabriel/propuesta.md) · [M3](../../modules/uv_termica/propuesta.md)
