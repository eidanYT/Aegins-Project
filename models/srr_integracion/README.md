# Modelos de integración para SRR

**TBR; análisis/ejemplos sin validación física.** Solo se escriben salidas en cad/ cuando se ejecuta el generador de geometría. No hay conexión a equipos.

| Archivo | Función | Alcance |
|---|---|---|
| [calculos.py](calculos.py) | Cotas de sincronización, escala de imagen, RSS, balance ideal de contaminante, masa de paneles y energía | Hipótesis y entradas explícitas; no predice seguridad ni curado |
| [control_conceptual.py](control_conceptual.py) | Estados, eventos y condiciones de inicio/recuperación | Modelo lógico; no implementación de control ni respuesta física |
| [geometria.py](geometria.py) | Bipirámide nominal con base cuadrada y caras | No trayectoria, espesor, anclaje ni prueba de impresión |
| [test_calculos.py](test_calculos.py) | Condiciones iniciales, conservación, conversiones y estados | Comprobación de modelos programados |
| [test_geometria.py](test_geometria.py) | Longitudes y cierre de malla | Comprobación de geometría nominal |

Desde la raíz: python -m unittest discover -s models/srr_integracion -p "test_*.py" -v.

Los números de calculos.py provienen de config/caso_demo.json y system/ejemplo_trazabilidad.md, y siguen siendo EJEMPLO_NO_APROBADO. La geometría usa system/caso_srr.json, que recoge la decisión actual de Eidan sin reemplazar el caso didáctico.

La [evidencia](../../evidence/srr_integracion_calculos.md) distingue resultados de cálculo, entradas didácticas y pruebas futuras. Ningún test equivale a verificación de equipo de vuelo.
