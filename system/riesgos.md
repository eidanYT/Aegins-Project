# Riesgos y verificación pendiente

Registro del SRR revisión 5; ningún control se considera físicamente verificado por esta actualización.

| Riesgo y prioridad | Consecuencia | Evidencia de respuesta y responsable propuesto |
| --- | --- | --- |
| R04/R07/R10 Alta — fuga o acumulación de gases | Exposición de tripulación, contaminación o presión. | Inventario, emisiones por especie, barreras compatibles y apertura; ensayos de fuga/retención. M2/M4 y alojamiento. |
| R01/R02/R03 Alta — desajuste de caudal UV o temperatura | Rotura, atasco, exceso de presión o calor. | Ventana medida, protección óptica, transitorios y ensayos térmicos/de fallo. M1/M2/M3/M5. |
| R05/MOT-002 Alta — interferencia o cargas de montaje | Colisión, daño de tubo o perturbación excesiva. | Trayectoria 6R y volumen barrido, giro finito de tubos/cables, cargas del sexto eje y montaje; verificación M1/M4. |
| R08/R13 Alta — pérdida de energía o falsa seguridad | Caudal o exposición residual con controlador parado. | Energía almacenada, retención física e inyección coordinada de fallos. M4/M5. |
| R12 Alta — cara sin apoyo o cierre final | Desprendimiento, unión débil, gas atrapado o defectos inaccesibles. | Deposición, curado e inspección por etapas y pruebas de cierre. M1/M2/M3/M5. |
| R11 Media — reconstrucción óptica inválida | Conclusión incorrecta de precisión o superficie. | Calibración con ventanas reales, cobertura y referencia independiente. M5. |
| R09 Alta — modelo sin trazabilidad o mal aplicado | Decisiones incorrectas a partir de cifras plausibles. | Entradas versionadas, unidades, recálculo y contraste físico. Todos. |
| R14 Alta — falta de acceso a alojamiento o lanzamiento | Demora o rediseño de demostración orbital. | Revisión temprana de interfaces; conservar desarrollo terrestre/gravedad reducida. Sistemas/M4. |
| R15 Media — incertidumbre de coste plazo o suministro | Falta de financiación o retrasos. | Estimación por paquetes, cotizaciones, ruta crítica y alternativas. Coordinación. |
| R16 Media — propiedad intelectual regulación o mercado | Uso restringido, demora o demanda insuficiente. | Revisión de antecedentes/derechos, exportación y reglas del alojamiento, validación de cliente. Coordinación. |
| R17 Alta — degradación de panel óptico | Exposición UV o pérdida de visión. | Ensayar panel, película, adhesivo y limpieza; PV03. M3/M4. |
| R18 Alta — filtro cargado o rama averiada | Pérdida de caudal o depresión y liberación. | Curvas, aislamiento, sensores y estado seguro; PV04. M4. |
| R19 Alta — CPU o placa inadecuada | Pérdida de sincronía, datos o control. | Presupuesto de CPU e interfaces, fallos y revisión de placa; PV05/PV06. M5. |

## Riesgos del desarrollo avanzado

- CAD, robot y proceso incoherentes: usar marcos y parámetros comunes y comprobar propiedades importadas.
- Simular una animación sin formación de caras: exigir material incremental, secuencia de apoyo/unión y criterio de curado, con límites físicos declarados.
- Confundir modos propios con supervivencia a lanzamiento: evaluar respuesta a cargas aplicables, uniones, márgenes y correlación física.
- Sobredimensionar software o IA antes de disponer de datos: prueba corta con herramientas existentes y decisión de alcance antes de desarrollar o entrenar.
- No tener modelos calibrados: identificar sensibilidad y resultado inconcluso; planificar ensayos PV01 a PV06 sin inventar capacidad disponible.

[Objetivos y puertas de cierre](../system/objetivos_pdr_y_desarrollo.md) · [Plan de simulación](software_simulacion.md).
