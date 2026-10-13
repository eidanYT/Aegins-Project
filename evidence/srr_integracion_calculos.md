# EV-SRR-INT-01 — Cálculos y modelo conceptual

**Tipo:** análisis y pruebas de software; sin ensayo físico. **Estado:** resultados matemáticos bajo hipótesis declaradas, pendientes de revisión independiente del equipo. Autor: Codex, 12 de octubre de 2026.

## Procedencia y alcance

- Caso didáctico: [DEMO-001](../config/caso_demo.json), sin cambios.
- Ejercicio histórico: [trazabilidad](../system/ejemplo_trazabilidad.md), sin adoptar sus objetivos como requisitos.
- Geometría actual: [SRR-GEO-001](../system/caso_srr.json).
- Código y pruebas: [modelos de integración](../models/srr_integracion/README.md).
- Requisitos afectados: CTL-001, MET-001, INT-001/002 y MOT-001 de forma condicionada. No se declara ninguno verificado en hardware.
- Versión reproducible: commit que introduce este archivo y su conjunto de modelos; identificarlo en el PR. No cambiar un resultado sin regenerar/revisar entradas.

## Resultados

| Cálculo | Entradas / procedencia | Resultado SI | Interpretación |
|---|---|---|---|
| Desplazamiento temporal de ejemplo | v=0,005 m/s y Δt=0,05 s, DEMO-001 | 0,00025 m | Sensibilidad, no error total físico |
| Límite temporal didáctico | asignación 0,0001 m del ejemplo histórico y v=0,005 m/s | 0,02 s | No es requisito de misión aprobado |
| Escala de imagen ideal | ancho 0,1 m y 1920 píxeles, ejemplo histórico | 5,2083333×10⁻⁵ m/píxel | No demuestra incertidumbre de reconstrucción |
| Altura de bipirámide nominal | base cuadrada y aristas a=0,05 m | √2·a=0,0707106781 m | Solo pieza, no cámara/mecanismo |
| Aristas y caras | conectividad de la geometría elegida | 12 aristas únicas, 8 caras | Cierre de malla; no cierre físico |

La cámara no recibe valores inventados de generación de gases, volumen, material o exposición. Los modelos de masa/energía/RSS están preparados para recibir datos; no hay totales de recursos ni incertidumbre real calculados.

## Doble comprobación realizada

Las conversiones temporales y de imagen se contrastan con aritmética racional en mm/ms frente a cálculos SI. Las pruebas de geometría evalúan distancias y uso opuesto de cada arista por las dos caras adyacentes. El balance ideal se comprueba contra conservación de masa y condición inicial; las entradas no finitas o incompatibles se rechazan.

El modelo lógico comprueba que no se salta de reposo a impresión, que condiciones inválidas bloquean inicio y que un fallo no permite reanudación automática. El evento power_lost es solo una representación; la reacción de hardware sin energía sigue por diseñar.

Estas comprobaciones usan métodos distintos dentro del mismo trabajo de Codex. **No constituyen una revisión de otra persona ni validación experimental independiente.**

## Reproducción y revisión pendiente

Ejecutar las pruebas y los generadores desde la raíz usando los comandos del README de modelos. Revisar entradas e hipótesis con Eidan/M1/M2/M3/M4. Para comprobar desempeño, hacen falta calibración, medición de tiempos, emisiones/contención y ensayos físicos con criterios aprobados.
