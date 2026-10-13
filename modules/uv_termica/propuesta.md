# Propuesta — M3: UV y térmica

**Estado: TBR, propuesta para revisión; versión 0.1, 2026-10-12.** Autor: agente técnico por encargo de Eidan. Responsable/revisor humano M3: por asignar, sin conformidad. Rama `tecnico/m1-m3-srr`, [PR #6](https://github.com/eidanYT/Aegins-Project/pull/6).

[Alcance](ALCANCE_TECNICO.md) · [Requisitos](../../system/requisitos.md) · [Ficha óptica](candidatos.md) · [Modelo](../../models/srr_agente_tecnico/README.md)

## Combinaciones y elección preliminar

| Combinación / geometría | Sustento y ventaja | Qué sigue pendiente |
|---|---|---|
| A — GE680 + iluminación localizada a 365 nm alrededor del cordón | F01 documenta esa banda; F02 aporta una condición de ficha. Anillo/múltiples sectores reduce dependencia azimutal para aristas. | TBR preferida para estudiar aristas. Óptica/cantidad de emisores, distancia y mapa de irradiancia TBD; no garantiza curar caras ni ausencia de sombras. |
| B — GE680 + foco 365 nm orientable y postexposición de caras | Mantiene banda respaldada y permite dirigir luz normal a cada cara. Puede separar deposición/gel de postcurado. | TBR; sombra de boquilla/otras caras, tiempo/energía de barrido, acceso inferior y anclaje. No hay evidencia de unión/resistencia para esta geometría. |
| C — Dymax 4-20806 + fuente UV/visible de banda a confirmar | Alternativa conjunta con M2 basada en F03; útil para contrastar recubrimiento apoyado. | No seleccionar 405 nm ni copiar dosis GE680 sin respuesta espectral/material. Fuente concreta y ventana: TBD. |

Referencia de emisor: Thorlabs M365L3, terrestre/histórica, F04. Se usa para separar potencia eléctrica/óptica en un presupuesto ilustrativo; **no se ha seleccionado** como cabezal ni validado suministro/calificación. Cuatro emisores equivalentes son una hipótesis, no la reproducción de la óptica publicada en F01.

## Exposición, sombras y caras cerradas

Caso didáctico de ICD-001: E=2500 W/m²=250 mW/cm², Luv=0,002 m y v=0,005 m/s ⇒ tex=0,4 s; H=1000 J/m²=100 mJ/cm². Es EJEMPLO: no se deriva del catálogo LED ni demuestra conversión. La condición F02 de capa máxima incluye **24 horas de evolución posterior**; no autoriza afirmar que el cordón tiene resistencia final al abandonar la boquilla. Distinguir gel/autoapoyo para formar la pieza de conversión y resistencia final.

Mapa angular sintético para luz paralela desde +z: Eface=E0 max(0,nz). En la geometría condicional, cuatro caras reciben factor 0,577 y cuatro inferiores 0; ver normales en resultados. Es análisis ideal de incidencia, sin reflexión ni sombras por brazo/recinto. Orientación normal restituye factor 1 solo en el modelo, no uniformidad ni acceso real. El integrador debe incluir rutas de boquilla/luz, fijación y última cara.

Mapa requerido para PDR: E(x,y,z,λ) calibrado y trazable, incluida boquilla y carcasa; H=∫E(t)dt en cada pista/nodo, con espectro, distancia, ángulo, velocidad y temperatura registrados. No aplicar ley de inverso del cuadrado a una óptica cercana sin justificarla. Derivar ventana mínima/máxima de gel, curado, unión y daño a partir de datos del material; una irradiancia nominal sola no satisface UV-001.

Propuesta contra curado en boquilla: pantallas opacas cerca de salida, ventana de iluminación desplazada al cordón, obturador/sectorización y verificación de luz parásita; materiales de pantalla/reflector y distancia TBD. Revisar que no bloqueen caras ni cámaras. Sensor de presión y observación pueden ayudar a detectar obstrucción, sin presumir cobertura de todos los fallos.

## Balance y recursos preliminares

Para cuatro M365L3 equivalentes a condición típica de F04: Pel=nIV=15,4 W; Popt=5,16 W; calor local en LED Pj=10,24 W. Drivers, óptica y enfriamiento no incluidos. **Típico no es límite máximo ni asignación de pico.** La potencia radiante no indica irradiancia depositada en la zona de 2 mm.

Balance del nodo: C dT/dt=Pj+Pdriver+Preacción−G(T−Tbase)−εσA(T⁴−Tenv⁴), C [J/K], G [W/K]. Reacción, contacto, emisividad, área, temperaturas y capacidades son TBD. Toda luz absorbida en el recinto también calienta al conjunto: para M4 presupuestar Pel más driver/reacción y demás módulos, evitando contar Pj+Popt y luego volver a añadir Pel.

Sensibilidad EJEMPLO con G=0,1/0,5/1 W/K y solo 10,24 W locales: elevación simplificada 102,4/20,48/10,24 K. No es predicción de temperatura LED/resina, ni cálculo de unión ni demostración de disipación. No tomar convección natural de laboratorio como ruta de enfriamiento en microgravedad. Si se propone ventilación, incluir medio, caudal, filtración/contención, vibración y fallos con M4.

| Recurso | Valor / unidad / condición / fuente | Estado / dato faltante |
|---|---|---|
| Masa/envolvente | TBD kg/m³ de emisores, soporte, driver, obturador y disipador | TBD; BOM, CAD y CG/inercia para M1. |
| Potencia de operación | 15,4 W típica, cuatro emisores a 1 A cada uno, F04/cálculo | TBR; driver y disipación adicionales. Máximo normal/pico TBD W con tolerancias/secuencia. |
| Energía | 24640 J=6,8444 Wh si encendidos solo 1600 s de deposición del caso | TBR; postexposición, transitorios y standby TBD. No equivale a misión. |
| Calor | 10,24 W locales típicos; ≈15,4 W en recinto si toda óptica absorbida | TBR; driver/reacción desconocidos y ruta térmica TBD. |
| Temperaturas/límites | TBD K, por componente, material y host | SDS/TDS, datasheet LED/driver y asignación M4. No umbral inventado. |
| Coste | TBD USD, consulta 2026-10-12 sin cotización actual | Óptica, drivers, seguridad, sensor/radiómetro y validación. No usar precio histórico. |

## Seguridad y coordinación

UV accesible, sobretemperatura, luz parásita, bloqueo y proceso incompletamente curado se tratan en ICD-005. Propuestas TBR: recinto opaco/ventanas con atenuación demostrable, enclavamiento de acceso independiente de software, supervisión térmica localizada, inhibición UV ante acceso/fallo eléctrico y retención de material. No se ha demostrado atenuación ni efectividad del interlock. UV apagado no elimina presión/resina residual: M2/M4/M5 deben definir estado seguro por fallo y condiciones de apertura.

| ICD / requisito | Propuesta / pregunta concreta | Revisor / estado |
|---|---|---|
| ICD-001 / UV-001 | Registrar espectro/E medido/H calculado, separado de consigna; ¿qué gel/resistencia permite el material en pistas y nodos? | Gabriel/M2, NICOMANUQP y M3 por asignar; pendiente. |
| ICD-002 / MOT-001 | ¿Cabezal simétrico o necesita sexto giro? Distancias, sombra, masa/CG y boquilla. | M1/M2/M4; pendiente. |
| ICD-003 / CTL-001 / MET-001 | Tiempo común, sensor/ubicación/calibración, saturación de cámaras y filtros compatibles. | Eidan/M5 y Shelton/M4; pendiente. |
| ICD-004 / THM-001 | Ruta de calor, temperaturas, energía por fases y límite de pico; ¿qué ofrece el alojamiento? | Shelton/M4, sistemas/host por designar; pendiente. |
| ICD-005 / SAF-001 | Secuencia para acceso, atasco, pérdida de energía y sobretemperatura; no parada universal sin analizar. | M2/M4/M5 y M1; pendiente. |

Método A realizado: exposición nominal, mapa angular ideal y balance/sensibilidad; comprobaciones del autor. Revisión independiente y ensayos físicos pendientes. Para PDR: confirmar emisor/driver, mapa óptico, cinética y calor; construir CAD del cabezal con M1/M4. Este programa entrega diseño/CAD: los ensayos aquí descritos son un plan futuro, sin resultado ni financiación comprometida. Fecha y revisor M3 por acordar.

[Fuentes F01–F04/F06/F07](../../models/srr_agente_tecnico/fuentes.md) · [Resultados](../../models/srr_agente_tecnico/resultados.json) · [Síntesis](../../reviews/SRR/aportes_agente_tecnico.md) · [Seguimiento técnico #5](https://github.com/eidanYT/Aegins-Project/issues/5)
