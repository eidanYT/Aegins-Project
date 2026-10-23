# Presupuestos de referencia del brazo 6R

Fuente: SRR revisión 5, base de precios del 15 de octubre de 2026. Son estimaciones de planificación y sensibilidades, sin cotización actual ni unidad de vuelo. Falta cerrar partidas; lo desconocido no equivale a cero. P precio publicado, R referencia/oferta condicional, F conversión EUR/USD del report, E provisión interna. El report fija 1 EUR = 1,1195 USD como supuesto, no tipo de cambio actual.

## Resumen

- Hardware y consumibles iniciales: USD 157 086,91; USD 41 961,91 en P/R/F y USD 115 125,00 en E. Excluye personal, licencias, impuestos, transporte, lanzamiento, hosting, calificación y servicios no cotizados.
- Masa contabilizada parcial: 9,838498 kg más piezas y equipos pendientes; M1 parcial 2,472 kg. No es masa total de diseño.
- Potencia DC parcial S1/S2: 156,02 / 229,62 W. S1 usa un punto de soplador a cierre sin caudal y es sensibilidad, no operación de misión aceptada.
- A 28 V supuestos y eficiencia 85%: 183,55 / 270,14 W de entrada y 6,56 / 9,65 A. Un 20% ilustrativo sobre S2 da 324,17 W / 11,58 A, más cargas y transitorios pendientes.
- El ejemplo de 1600 s solo de deposición da 81,58 Wh en S1; reevaluar tiempo de trayectorias 6R, preparación, pausas, curado, inspección y misión completa.
- Cuatro Nichia U365: 15,4 W eléctricos, 5,8 W ópticos y 9,6 W de calor local LED a los valores típicos declarados; driver, reacción y luz absorbida se contabilizan sin duplicar calor.

## Inventario por componente

| Componente | Cant. | Masa total g | Tensión / corriente | W S1 / S2 | Base / dato pendiente |
| --- | --- | --- | --- | --- | --- |
| M1 Brazo 6061 | 1 | CAD | Pasivo | 0 | Falta geometría del brazo |
| M1 EC32 flat 267121 | 6 | 342 | 24 V; 0.5 A/motor | 43.20 / 72 | 57 g/u; ficha + factor S1 [P01] |
| M1 CSG-14-50-2UH-LW | 6 | 1920 | Pasivo | 0 | 320 g/u; variante de referencia [J01] |
| M1 RESOLUTE BiSS C | 6 | 108 | 5 V ±10%; ≤0.25 A/lector | 7.50 / 7.50 | 18 g/u; sin anillos/cables [J02] |
| M1 EPOS4 Module 534130 | 6 | 102 | 10–50 V; diseño 24 V | 12 / 12 | 17 g/u; pérdidas supuestas 2 W/u [P02] |
| M2 Resina GE680 | 2 × 50 g | 100 | Pasivo | 0 | Provisión de stock; faltan envases |
| M2 vipro-HEAD 5 | 1 | ≈750 | 24 V; ≤1.4 A/fase | 7.2 / 12 | Cabezal de ficha; W supuestos [J03] |
| M2 Boquilla inoxidable | 2 | CAD | Pasivo | 0 | Faltan largo y diámetros interior/exterior |
| M2 PTFE protegido | 0.5 m ref. | CAD | Pasivo | 0 | Faltan diámetros y protección |
| M2 Presión Kulite | 1 | Falta PN | Falta PN | ND | No consta modelo/rango Kulite |
| M3 NVSU233B U365 | 4 | 0.148* | 3.85 V típ.; 1 A/LED | 15.4 / 15.4 | 0.037 g/u sin placa [P16] |
| M3 Placa + correas | 1 | CAD | Pasivo | 0 | Faltan dimensiones placa/correas |
| M3 Pt100 + MAX31865 (banco) | 1 | 22.0 ref. | 3–5 V lector; RTD pasivo | ND | 3290: 19.3 g + 3328: 2.7 g [J06] |
| M3 SG01D + amplificador | 1 | No publicada | 0 V polarización posible; falta amplificador | ND | SG01D-18; ficha sin masa [J07] |
| M4 Base Al6061 | 1 | 2160 calc. | Pasivo | 0 | Base ilustrativa; CAD no final |
| M4 Lexan paredes + techo | 5 | 3840 calc. | Pasivo | 0 | 5 paneles ilustrativos; CAD no final |
| M4 Rosco R3114 | 2 | Área | Pasivo | 0 | Faltan área instalada/masa por área |
| M4 Recubrimiento Acktar | 1 | 16–32 × S | Pasivo | 0 | g/m² × área recubierta S [C5] |
| M4 Honeywell 1HM1 | 1 | ≤6.35 | Contacto seco; sin alimentación | ND | 1HM1 máximo; falta circuito lector [J08] |
| M4 Presión diferencial | 1 | Falta PN | Falta PN | ND | Piezorresistivo Δp: falta modelo |
| M4 U51DL-024KK-4 | 3; 2 activos | 360 | 12–28 V; nominal 24 V | 46 / 86 | 120 g/u; dos activos + reserva [J04] |
| M4 HEPA + carbón | 2 | Falta PN | Pasivo | 0 | Falta modelo filtro/cartucho |
| M5 Computador GR740 | 1 | Placa | 5 V; <1.4 A referencia | 7 / 7 | Referencia GR-SBC; masa placa sin publicar [J05] |
| M5 SAMRH71 | 1 | Placa | 12 V EK; chip 1.8/3.3 V | ND | Masa EK no publicada; salidas ≠ entrada [J09] |
| M5 RTG4 | 1 | Placa | Chip 1.2/3.3 V; E/S variable | ND | Faltan masa/entrada placa; ver nota [J10] |
| M5 CASPEX 4 Mp | 2 | 128 | 5–9 V; diseño 5 V | 10 / 10 | 64 g/u presupuesto; folleto 62 g [J11] |
| M5 SDRAM 3D PLUS | 1 | Falta PN | Depende del PN | ND | Solo familia; RAM integrada no se suma |
| M5 MRAM UT8MR2M8 | 1 | Encapsulado | 3.3 V nominal (3.0–3.6 V) | ND | Faltan encapsulado/cantidad y carga [J12] |
| M5 VPT SVR + PDU | 1 | ≤55 ref. + PDU | 18–40 V entrada; 5 V salida ref. | Pérdidas ND | Solo referencia SVRTR2805S; ver nota [J13] |
| M5 Interfaces CAN | 7 sup. | PN/PCB | Falta PN transceptor | ND | 6 ejes + supervisor; falta PN/PCB |
| M3 Driver LED B33 | 1 | PN/PCB | 24 V supuesto; 0.755 A total | 2.72 / 2.72 | Falta PN driver; η=85% supuesta |
| Auxiliares comunes | 1 | Inventario | Falta asignar salidas | 5 / 5 | Provisión parcial de 5 W |
| Uniones, anillos, sellos, válvulas, cables, óptica | B31–B37 | Inventario | Según pieza instalada | ND | Faltan dimensiones/PN y cantidades |

## Totales por módulo

| Módulo | Masa kg | S1 W | S2 W | Fracción S2* |
| --- | --- | --- | --- | --- |
| M1 | 2.472000 + pend. | 62.70 | 91.50 | 39.8% |
| M2 | 0.850000 + pend. | 7.20 | 12.00 | 5.2% |
| M3 | 0.022148 + pend. | 18.12 | 18.12 | 7.9% |
| M4 | 6.366350 + pend. | 46.00 | 86.00 | 37.5% |
| M5 | 0.128000 + pend. | 17.00 | 17.00 | 7.4% |
| Auxiliares comunes | pend. | 5.00 | 5.00 | 2.2% |
| Subtotal parcial | 9.838498 + pend. | 156.02 | 229.62 | 100%* |

## Coste detallado de hardware

| Componente | Cant. | USD unidad | USD partida | Base del precio |
| --- | --- | --- | --- | --- |
| B01 M1 6061 del brazo y mecanizado | 1 | 800.00 | 800.00 | E: Lote según CAD; estimación interna |
| B02 M1 maxon EC 32 flat 267121 | 6 | 109.89 | 659.34 | P: Tramo 5–19 [P01]; catálogo, adaptación excluida |
| B03 M1 Harmonic Drive CSF/CSG | 6 | 1,500.00 | 9,000.00 | E: Provisión por reductora; dimensionar tamaño/relación |
| B04 M1 Lectores RESOLUTE | 6 | 1,652.00 | 9,912.00 | R: Referencia RA26BTA052B10F [P03]; anillos B32 |
| B05 M1 EPOS4 Module 50/5 534130 | 6 | 371.30 | 2,227.80 | F: 331.67 EUR × 1.1195; unidad redondeada [P02,P12] |
| B06 M2 Cartuchos GE680 de 50 g | 2 | 200.00 | 400.00 | E: Provisión por envase de 50 g; no es precio publicado |
| B07 M2 Paquete dosificador viproHEAD 5 | 1 | 8,000.00 | 8,000.00 | E: Provisión cabezal/accionamiento; requiere oferta |
| B08 M2 Boquillas de acero inoxidable | 2 | 50.00 | 100.00 | E: Una operativa y una de reserva; dimensionar diámetro |
| B09 M2 Línea PTFE protegida de UV | 1 | 25.00 | 25.00 | E: Una línea de estudio de 0.5 m; racores en B36 |
| B10 M2 Sensor de presión Kulite | 1 | 1,500.00 | 1,500.00 | E: Provisión de familia espacial; verificar rango/cara húmeda |
| B11 M3 Nichia NVSU233B 365 nm en PCB | 4 | 39.93 | 159.72 | P: Lumistrips SKU 31715 [P04]; drivers/óptica B33 |
| B12 M3 Placa conductora y correas | 1 | 400.00 | 400.00 | E: Provisión de conjunto térmico a medida |
| B13 M3 Pt100 con lectura de banco | 1 | 26.90 | 26.90 | R: Adafruit 3290 + MAX31865: 11.95 + 14.95 [P11] |
| B14 M3 Fotodiodo SiC SG01D-18 | 1 | 65.75 | 65.75 | P: sglux en DigiKey [P05]; calibrar a 365 nm |
| B15 M4 Base y marco de 6061 | 1 | 600.00 | 600.00 | E: Lote de material/mecanizado; separado del brazo |
| B16 M4 Paneles Lexan y corte | 1 | 600.00 | 600.00 | E: Lote para un recinto; dimensionar área/grado/espesor |
| B17 M4 Hojas Rosco R3114 | 2 | 11.50 | 23.00 | P: Hoja de referencia 20 × 24 pulgadas [P08]; adhesivo B36 |
| B18 M4 Lote inicial Acktar Fractal Black | 1 | 810.00 | 810.00 |  |
| B19 M4 Honeywell HM, referencia 1HM1 | 1 | 829.34 | 829.34 | P: Listado DigiKey/Powell [P07]; verificar montaje |
| B20 M4 Sensor diferencial piezorresistivo | 1 | 200.00 | 200.00 | E: Provisión de bajo diferencial; distinto de Kulite |
| B21 M4 Micronel U51DL-024KK-4 | 3 | 398.00 | 1,194.00 | P: Dos activos y uno de reserva [P06]; aislamiento B36 |
| B22 M4 Cartuchos HEPA y carbón | 2 | 500.00 | 1,000.00 | E: Un conjunto operativo y otro de reserva; dimensionar capacidad |
| B23 M5 Plataforma de evaluación GR740 | 1 | 15,000.00 | 15,000.00 | E: Provisión de placa [P13]; no se supone préstamo concedido |
| B24 M5 Plataforma de evaluación SAMRH71 | 1 | 4,500.00 | 4,500.00 | E: Provisión de placa; SAMRH71F20-EK bajo consulta [P14] |
| B25 M5 RTG4-DEV-KIT-CG-1 | 1 | 26,054.06 | 26,054.06 | P: Kit de ingeniería Mouser [P10]; no es precio de unidad de vuelo |
| B26 M5 Cabezales de cámara CASPEX 4 Mp | 2 | 25,000.00 | 50,000.00 | E: Provisión de estudio para dos cámaras; sin precio público [P15] |
| B27 M5 Artículo de ensayo SDRAM espacial 3D PLUS | 1 | 4,000.00 | 4,000.00 | E: Provisión de memoria objetivo; distinta de RAM del kit |
| B28 M5 Artículo de ensayo MRAM UT8MR2M8 | 1 | 2,500.00 | 2,500.00 | E: Almacenamiento de estados; no de imágenes masivas |
| B29 M5 Conjunto de potencia VPT SVR | 1 | 6,000.00 | 6,000.00 | E: Provisión de conversión/salidas; dimensionar variantes |
| B30 M5 Nodos de interfaz CAN | 7 | 100.00 | 700.00 | E: Seis ejes y supervisor; provisión transceptores/PCB |
| B31 Uniones mecánicas y cojinetes | 6 | 250.00 | 1,500.00 | E: Hardware articular sin motores/reductoras; estimación interna |
| B32 Anillos RESOLUTE y montaje | 6 | 250.00 | 1,500.00 | E: Provisión anillo/fijación; no incluida en lector |
| B33 Drivers UV y óptica del haz | 1 | 800.00 | 800.00 | E: Lote de hardware driver/óptica para cuatro LED |
| B34 Interbloqueos acondicionamiento y PCB adaptadoras | 1 | 1,000.00 | 1,000.00 | E: Bloqueo UV físico, lectura de sensores e interfaces de realimentación |
| B35 Objetivos de cámara e iluminación visible | 1 | 2,000.00 | 2,000.00 | E: Lote óptico/iluminación para dos cámaras; sin duplicar cámaras |
| B36 Sellos válvulas cableado anclajes y conectores | 1 | 1,500.00 | 1,500.00 | E: Lote de interfaces, protección opaca y contención |
| B37 Repuestos iniciales y consumibles de proceso | 1 | 1,500.00 | 1,500.00 | E: Otras partidas iniciales; sin repetir repuestos ya contados |
| Total de compra Hg |  |  | 157,086.91 | Referencias P/R/F + provisiones E |

## Cierre necesario

M4 integra aportes de cada módulo: masa y centro/inercia del CAD, arnés, sellos, tubos, tornillos, anillos, sexta carcasa, fuentes y electrónica completas; potencia normal/pico con duración y simultaneidad; energía por modo; flujo térmico y rechazo; capacidad de almacenamiento y enlace. Presupuestar también ensayo, instrumentación, útiles, software, ingeniería, integración y operación. Verificar por separado 5 V de RESOLUTE y capacidad EPOS4, buses/encoders y capacidad MRAM para estados frente a imágenes.

Las referencias abreviadas se resuelven en el [report completo](../reviews/SRR/report_referencia.md). No se han actualizado precios a la fecha de esta sincronización.
