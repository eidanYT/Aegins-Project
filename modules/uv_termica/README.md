# M3 — UV y térmica
Responsable y revisor: completar en management/equipo.md.
Estado: borrador para organizar la investigación. Candidatos no seleccionados ni calificados para vuelo.

## Qué medir y relación con la misión
Distribución de irradiancia, historia de exposición, temperatura y criterio de curado.
El ambiente de microgravedad y el escenario se definen a nivel de sistema; este paquete declara cómo cambian sus supuestos.

## 1. Prestaciones necesarias
Requisitos padres: UV-001, THM-001.
Espectro, irradiancia a distancia definida, área iluminada, sombras, emisión/calor, conversión y temperatura admisible.
Registrar valor, unidad, condiciones, tolerancia, fuente y estado. Los límites definitivos se derivan del caso común y de la plataforma.

## 2. Componentes o arquitecturas candidatas
Fuente UV a 365 nm como referencia de P1/P2; otra banda o geometría solo si la formulación tiene evidencia de respuesta. Comparar foco y distribución alrededor del cordón antes de elegir pieza comercial.
Completar templates/componente.md para cada opción crítica. Lo que no dispone de ficha se marca “concepto”, no “modelo seleccionado”.
Un componente terrestre puede servir para representación o ensayo; no se le atribuye aptitud espacial automáticamente.

## 3. Interfaces y riesgos
ICD-001: v/exposición; ICD-002: masa/óptica; ICD-004/005: calor y contención.
Revisar system/riesgos.md y enlazar los eventos aplicables.
Ningún cambio en una salida compartida se acepta sin comprobar qué ocurre en el receptor.

## 4. Verificación
Integración de irradiancia a lo largo de la trayectoria, balance térmico con incertidumbre, futura caracterización de curado.
Distinguir lo que se verificará durante SRR/PDR de las pruebas futuras que exige construir o volar.

## Información faltante
Mapa óptico del fabricante, respuesta de resina, calor de reacción y límites térmicos; separar potencia eléctrica y óptica.
Crear Issues acotadas con responsable y fecha. No esperar a conocer todo para producir un primer modelo con incertidumbre.

## Primera entrega
Comparación resina–fuente junto a M2, mapa aproximado justificado, balance térmico inicial y estrategia para evitar curado en boquilla.
Entregar como PR con vínculos a requisitos, interfaces y evidencia.
