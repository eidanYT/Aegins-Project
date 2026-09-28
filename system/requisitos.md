# Registro inicial de requisitos
Todos los requisitos siguientes son BORRADORES. Aceptarlos exige justificación y aprobación del equipo.
Los valores de config/caso_demo.json son EJEMPLOS, no límites aprobados.
Métodos: A análisis; I inspección documental; D demostración; T ensayo físico futuro.

| ID | Padre | Requisito propuesto | Valor/criterio pendiente | Responsable | Interfaz | Verificación y evidencia prevista |
|---|---|---|---|---|---|---|
| SYS-001 | Necesidad programa | Definir un escenario único de referencia y sus límites ambientales | D-001 cerrado | Sistemas/M4 | ICD-004 | I: decisión y fuentes |
| SCI-001 | Pregunta científica | Permitir comparar orientación fija y variable con condiciones registradas | Protocolo aprobado, métricas y réplicas justificadas | Sistemas/M5 | ICD-001/003 | I/A: protocolo y sensibilidad |
| SCI-002 | SCI-001 | Definir métricas de trayectoria y diámetro e incertidumbre | Umbral científico TBD | M5 | ICD-003 | A/T: presupuesto de errores y calibración |
| MOT-001 | SCI-001 | Alcanzar poses de la probeta de referencia dentro de límites del mecanismo | Geometría final y orientación TBR | M1 | ICD-002 | A: trayectoria, límites y resultado cinemático |
| MOT-002 | SYS-001 | Mantener reacciones y movimiento dentro de asignación de plataforma | Cargas/par/perturbación TBD | M1/M4 | ICD-004 | A: modelo de base fija o dinámica acoplada según plataforma |
| EXT-001 | SCI-001 | Entregar el caudal requerido con transitorios compatibles con el error permitido | Rango y tiempo de respuesta TBD | M2 | ICD-001 | A/T: alimentación, tolerancias y curva Q(t) |
| EXT-002 | SYS-001 | Mantener material y presión dentro de límites del circuito | Presión/líquido/compatibilidad TBD | M2/M4 | ICD-005 | A/I/T: materiales y plan de prueba |
| UV-001 | SCI-001 | Entregar exposición y espectro compatibles con formulación y geometría | Ventana de curado TBD | M3 | ICD-001 | A/T: mapa de irradiancia y evidencia de material |
| THM-001 | SYS-001 | Mantener temperaturas y disipación dentro de asignaciones | Límites material/equipo/host TBD | M3/M4 | ICD-004/005 | A/T: balance con incertidumbre |
| INT-001 | SYS-001 | Retener líquidos, fragmentos y pieza durante operación y fallos definidos | Criterios según peligro y host TBD | M4/M2 | ICD-005 | A/T: peligros y plan de verificación |
| INT-002 | SYS-001 | Respetar volumen, masa, energía, potencia y comunicaciones asignadas | Asignación host TBD | M4 | ICD-004 | I/A: presupuestos y comparación con ICD host |
| CTL-001 | SCI-001 | Registrar comandos y mediciones con identificación temporal común | Desfase/latencia permitidos TBD | M5 | ICD-001/003 | A/D/T: secuencia simulada y prueba de sincronía |
| MET-001 | SCI-002 | Resolver la diferencia científicamente relevante sin confundirla con error de medida | Resolución/incertidumbre TBD | M5 | ICD-003 | A/T: calibración, cobertura y error |
| SAF-001 | SYS-001 | Alcanzar estado seguro ante fallos seleccionados | Estado y tiempo por fallo TBD | M5/M4 | ICD-005 | A/D/T: escenarios y transición coordinada |
| DOC-001 | Programa | Entregar concepto, especificaciones y visualización trazables | Lista SRR completa | Sistemas | Todas | I: reviews/SRR/README.md |

## Qué cerrar antes del SRR
Plataforma conceptual elegida, probeta, rangos preliminares de proceso, métricas y objetivos justificados.
Si el alojamiento sigue sin conocerse, fijar una asignación provisional explícita con su fuente/razón y riesgo; no afirmar compatibilidad real.
Cada TBD se vincula a una Issue, un propietario y fecha en system/pendientes.md.
No confundir “tenemos plan de ensayo” con “requisito verificado por ensayo”.
