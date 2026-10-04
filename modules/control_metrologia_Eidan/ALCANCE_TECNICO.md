# M5 — Control y metrología
Responsable: Eidan. Revisión según los módulos afectados; consultar management/equipo.md.
Estado: borrador para organizar la investigación. Candidatos no seleccionados ni calificados para vuelo.

## Qué medir y relación con la misión
Sincronización y calidad del dato; geometría del material, temperatura, presión y respuesta ante fallo.
El ambiente de microgravedad y el escenario se definen a nivel de sistema; este paquete declara cómo cambian sus supuestos.

## 1. Prestaciones necesarias
Requisitos padres: CTL-001, MET-001, SAF-001.
Latencia/jitter, frecuencia de adquisición, resolución/incertidumbre, rango, calibración, campo de visión, reloj, almacenamiento y interfaces eléctricas.
Registrar valor, unidad, condiciones, tolerancia, fuente y estado. Los límites definitivos se derivan del caso común y de la plataforma.

## 2. Componentes o arquitecturas candidatas
Controlador del robot + MCU para proceso + ordenador para visión/registro como arquitectura candidata terrestre. Comparar MCU STM32-class o Teensy-class por interfaces/timing; modelo exacto TBD. Cámaras calibradas, sensor de presión y temperatura; acelerómetro solo con banda/ruido justificados.
Completar templates/componente.md para cada opción crítica. Lo que no dispone de ficha se marca “concepto”, no “modelo seleccionado”.
Un componente terrestre puede servir para representación o ensayo; no se le atribuye aptitud espacial automáticamente.

## 3. Interfaces y riesgos
ICD-001: consignas; ICD-003: datos; ICD-004: potencia/comunicaciones; ICD-005: estado seguro.
Revisar system/riesgos.md y enlazar los eventos aplicables.
Ningún cambio en una salida compartida se acepta sin comprobar qué ocurre en el receptor.

## 4. Verificación
Trazas temporales sintéticas y presupuesto de errores ahora; futuras pruebas de sincronización/calibración. Elegir muestreo desde banda y antialias.
Distinguir lo que se verificará durante SRR/PDR de las pruebas futuras que exige construir o volar.

## Información faltante
Errores científicamente relevantes, protocolos del hardware candidato, ruido/cadencia de sensores y condiciones ambientales.
Registrar preguntas concretas en Issues enlazadas a la propuesta. No esperar a conocer todo para producir un primer modelo con incertidumbre.

## Primera entrega
Diagrama de estados, diccionario de señales, presupuesto de medida y ejemplo de log. No confundir resolución de píxel con exactitud.
Entregar como PR con vínculos a requisitos, interfaces y evidencia.


[Volver al Get started](README.md) · [Propuesta de trabajo](propuesta.md)
