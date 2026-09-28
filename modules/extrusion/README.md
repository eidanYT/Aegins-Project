# M2 — Material y extrusión
Responsable y revisor: completar en management/equipo.md.
Estado: borrador para organizar la investigación. Candidatos no seleccionados ni calificados para vuelo.

## Qué medir y relación con la misión
Caudal real/estimado, estabilidad temporal, presión y comportamiento del material.
El ambiente de microgravedad y el escenario se definen a nivel de sistema; este paquete declara cómo cambian sus supuestos.

## 1. Prestaciones necesarias
Requisitos padres: EXT-001, EXT-002.
Viscosidad según temperatura/cizalla, compatibilidad de sellos, volumen, rango Q, presión, respuesta y burbujas. La formulación exacta y la seguridad están abiertas.
Registrar valor, unidad, condiciones, tolerancia, fuente y estado. Los límites definitivos se derivan del caso común y de la plataforma.

## 2. Componentes o arquitecturas candidatas
Cartucho/jeringa con pistón motorizado; alternativa depósito con expulsión positiva y regulación de presión. GE680 es candidata por P1; añadir otra formulación con ficha y justificación.
Completar templates/componente.md para cada opción crítica. Lo que no dispone de ficha se marca “concepto”, no “modelo seleccionado”.
Un componente terrestre puede servir para representación o ensayo; no se le atribuye aptitud espacial automáticamente.

## 3. Interfaces y riesgos
ICD-001: v/Q; ICD-002: cabezal/manguera; ICD-005: fugas y presión.
Revisar system/riesgos.md y enlazar los eventos aplicables.
Ningún cambio en una salida compartida se acepta sin comprobar qué ocurre en el receptor.

## 4. Verificación
Balance de masa y modelo de presión/transitorios; después ensayo de alimentación con material real.
Distinguir lo que se verificará durante SRR/PDR de las pruebas futuras que exige construir o volar.

## Información faltante
Fichas TDS/SDS, reología, cinética compartida con M3, elasticidad del circuito, precio/cotización y disponibilidad.
Crear Issues acotadas con responsable y fecha. No esperar a conocer todo para producir un primer modelo con incertidumbre.

## Primera entrega
Comparación de alimentación y dos materiales, cálculo nominal con sensibilidad y definición de qué significa Q comandado frente a Q entregado.
Entregar como PR con vínculos a requisitos, interfaces y evidencia.
