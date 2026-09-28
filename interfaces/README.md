# Interfaces: contratos entre paquetes
Una interfaz define lo que un paquete necesita del otro y lo que garantiza, con unidades, rangos, tolerancias, tiempos, marcos y reacción ante fallos.
Cada lado identifica un responsable real en management/equipo.md.

| ID | Paquetes | Qué acordar | Evidencia de aceptación |
|---|---|---|---|
| ICD-001 | M1/M2/M3/M5 | Velocidad–caudal–exposición y secuencia temporal | Caso nominal, desaceleración y parada; modelos y retrasos declarados |
| ICD-002 | M1/M2/M3/M4 | Brida, TCP, masa/CG/inercia del cabezal, tubos y cables | CAD de envolvente, recorrido y tabla de cargas |
| ICD-003 | M5 con M1/M2/M3 | Señales, unidades, adquisición, relojes, validez y calibración | Diccionario de datos y registro de ejemplo |
| ICD-004 | M4 con plataforma y M1/M3/M5 | Montaje, masa, cargas, potencia, calor y comunicaciones | Asignación host/hipótesis y presupuesto |
| ICD-005 | M2/M3/M4/M5 | Contención, fallos, acceso y estado seguro | Análisis de peligros y diagrama de estados |

ICD-001 tiene un ejemplo desarrollado. Para los demás copiar templates/interfaz.md.
Antes de cambiar una interfaz: crear Issue → identificar afectados → PR con cálculo de impacto → conformidad de cada lado → coordinación integra.
Un comentario informal en chat no actualiza una interfaz aceptada.

## Ejemplo
M1 quiere pasar de 5 a 8 mm/s. M2 calcula el nuevo caudal; M3 revisa tiempo de exposición; M5 actualiza secuencia; M4 verifica potencia/calor si cambian.
Si M3 no puede alcanzar el proceso necesario, el cambio vuelve a decisión: reducir velocidad, modificar óptica o cambiar geometría/material. No se integra una contradicción.
