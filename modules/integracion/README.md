# M4 — Recinto e integración
Responsable y revisor: completar en management/equipo.md.
Estado: borrador para organizar la investigación. Candidatos no seleccionados ni calificados para vuelo.

## Qué medir y relación con la misión
Compatibilidad con plataforma: envolvente, cargas, masa, energía, calor, materiales y contención.
El ambiente de microgravedad y el escenario se definen a nivel de sistema; este paquete declara cómo cambian sus supuestos.

## 1. Prestaciones necesarias
Requisitos padres: SYS-001, INT-001, INT-002.
Presión/temperatura, volumen disponible, montaje, pasamuros, inventario, extracción/almacenamiento, potencia y enlace de datos. Ningún límite ISS se supone universal.
Registrar valor, unidad, condiciones, tolerancia, fuente y estado. Los límites definitivos se derivan del caso común y de la plataforma.

## 2. Componentes o arquitecturas candidatas
Cámara con atmósfera controlada; alternativa recinto ventilado hacia un alojamiento compatible; opción expuesta al vacío solo como escenario completo distinto.
Completar templates/componente.md para cada opción crítica. Lo que no dispone de ficha se marca “concepto”, no “modelo seleccionado”.
Un componente terrestre puede servir para representación o ensayo; no se le atribuye aptitud espacial automáticamente.

## 3. Interfaces y riesgos
ICD-002: montaje; ICD-004: host; ICD-005: fallos, residuos y apertura.
Revisar system/riesgos.md y enlazar los eventos aplicables.
Ningún cambio en una salida compartida se acepta sin comprobar qué ocurre en el receptor.

## 4. Verificación
Inspección del ensamble y presupuestos, análisis de peligros; futura prueba de contención, térmica y estructura según interfaz aplicable.
Distinguir lo que se verificará durante SRR/PDR de las pruebas futuras que exige construir o volar.

## Información faltante
Plataforma de referencia y recursos asignados, ambiente de lanzamiento/operación y concepto de recuperación de muestras.
Crear Issues acotadas con responsable y fecha. No esperar a conocer todo para producir un primer modelo con incertidumbre.

## Primera entrega
Cerrar D-001 con el equipo, CAD de envolvente, presupuesto integrado y riesgos con controles y evidencias pendientes.
Entregar como PR con vínculos a requisitos, interfaces y evidencia.
