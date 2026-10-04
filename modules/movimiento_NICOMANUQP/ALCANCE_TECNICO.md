# M1 — Movimiento
Responsable: Responsable por asignar. Revisión según los módulos afectados; consultar management/equipo.md.
Estado: borrador para organizar la investigación. Candidatos no seleccionados ni calificados para vuelo.

## Qué medir y relación con la misión
Posición/orientación del TCP y alcance de una probeta común; cargas e interacción con la base.
El ambiente de microgravedad y el escenario se definen a nivel de sistema; este paquete declara cómo cambian sus supuestos.

## 1. Prestaciones necesarias
Requisitos padres: MOT-001, MOT-002.
Workspace útil, límites articulares, orientación, velocidad/aceleración, masa/CG/inercia del cabezal, rigidez y cargas. Repetibilidad de catálogo no es exactitud del cordón.
Registrar valor, unidad, condiciones, tolerancia, fuente y estado. Los límites definitivos se derivan del caso común y de la plataforma.

## 2. Componentes o arquitecturas candidatas
Brazo serial 6-DOF de referencia (UR5e documentado en P2); alternativa cartesiana con cabezal orientable. Comparar, no asumir que seis ejes son imprescindibles.
Completar templates/componente.md para cada opción crítica. Lo que no dispone de ficha se marca “concepto”, no “modelo seleccionado”.
Un componente terrestre puede servir para representación o ensayo; no se le atribuye aptitud espacial automáticamente.

## 3. Interfaces y riesgos
ICD-001: tiempo de trayectoria; ICD-002: cabezal/tubos; ICD-004: reacción sobre plataforma.
Revisar system/riesgos.md y enlazar los eventos aplicables.
Ningún cambio en una salida compartida se acepta sin comprobar qué ocurre en el receptor.

## 4. Verificación
Cinemática, límites y colisiones de los objetos modelados. Base fija solo si justificada; en satélite revisar reacción y control de actitud.
Distinguir lo que se verificará durante SRR/PDR de las pruebas futuras que exige construir o volar.

## Información faltante
Modelo CAD/kinemático del brazo, datos de carga y plataforma; recorrido realista de mangueras.
Registrar preguntas concretas en Issues enlazadas a la propuesta. No esperar a conocer todo para producir un primer modelo con incertidumbre.

## Primera entrega
Una tabla de dos arquitecturas, trayectoria representativa con límites, envolvente y lista de restricciones. No basta un video bonito.
Entregar como PR con vínculos a requisitos, interfaces y evidencia.


[Volver al Get started](README.md) · [Propuesta de trabajo](propuesta.md)
