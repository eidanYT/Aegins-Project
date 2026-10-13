# Registro inicial de riesgos y peligros
No es una evaluación de seguridad aprobada. La severidad/controles dependen del escenario.
| ID | Evento | Consecuencia | Responsable | Control a estudiar | Evidencia faltante |
|---|---|---|---|---|---|
| R01 | Pérdida de coordinación v/Q/UV | Diámetro irregular, ruptura, curado desigual | M1/M2/M3/M5 | Secuencia temporal y respuesta ante pausa | Latencias y modelo de proceso |
| R02 | Curado dentro de boquilla | Atasco y aumento de presión | M2/M3 | Pantalla óptica, distancia y limitación de presión | Geometría/mapa óptico |
| R03 | Calor de reacción excesivo | Deformación, degradación, peligro térmico | M3/M4 | Límite de proceso y disipación | Propiedades/cinética térmica |
| R04 | Fuga o desprendimiento | Contaminación de equipo; posible exposición humana | M2/M4 | Contención y retención | Compatibilidad y análisis de fallo |
| R05 | Manguera limita movimiento | Colisión, cargas o tracción no previstas | M1/M2/M4 | Enrutamiento y radios de curvatura | Modelo de recorrido/cargas |
| R06 | Reacción del brazo en satélite | Perturbación de actitud y geometría | M1/M4 | Perfil suave y compatibilidad con control de nave | Inercias, base y límites host |
| R07 | Emisiones incompatibles | Daño/contaminación, posible riesgo a tripulación | M2/M4 | Inventario, materiales y gestión de emisiones | Evaluación específica del ambiente |
| R08 | Pérdida de energía/datos | Proceso interrumpido con material residual | M5/M2/M3 | Estado seguro por fallo | Simulación de transición y ensayo futuro |
| R09 | Modelo o cifra sin validar | Diseño aparentemente correcto pero no sustentado | Todos | Trazabilidad y sensibilidad | Fuentes y revisión |
Priorizar peligros de alta consecuencia aunque una probabilidad supuesta produzca un número bajo.
No asumir que “no tripulado” elimina contaminación, incendio o pérdida del vehículo.

## Ampliación por cámara, medición y caras cerradas

Estas son hipótesis de peligro para evaluación; severidad/probabilidad no se asignan sin escenario e inventario. No son una evaluación aprobada.

| ID | Evento | Impacto a evaluar | Trabajo y responsable propuestos | Evidencia pendiente |
|---|---|---|---|---|
| R10 | Acumulación, obstrucción o capacidad agotada en la gestión de gases | Presión, contaminación y posible exposición | M2/M4/host: inventario, ruta y balance por especie | Emisiones, capacidad y ensayos de contención/apertura |
| R11 | Vista óptica inválida por sombras, brillo, transparencia o ventana | Conclusión geométrica sin cobertura/incertidumbre fiable | M5 con M3/M4: calibración, cobertura y validez | Patrón independiente y material/óptica reales |
| R12 | Formación de caras y cierre de volumen con gas o residuo interno | Defectos, deformación o recuperación no prevista | M1/M2/M3 con M4/M5: estrategia de cierre e inspección por etapas | Fabricabilidad, espesor, uniones y gas interno |
| R13 | Confundir HOLD lógico con seguridad física | Continuación o acceso sin contención aceptada | M4/M5/host: condiciones físicas y respuesta sin energía | Análisis y prueba por escenario de fallo |

La selección de estación tripulada aumenta la relevancia de exposición y acceso, pero no determina sustancias ni límites. La pieza nominal cerrada no demuestra estanqueidad ni eliminación de gases.
