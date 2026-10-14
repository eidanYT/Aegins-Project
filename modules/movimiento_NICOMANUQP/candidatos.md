# Fichas de arquitecturas — M1

Versión 0.1, 2026-10-12. Campos de la plantilla de componente; **conceptos/candidatos TBR, ninguno seleccionado o calificado**. Revisión propuesta NICOMANUQP, pendiente.

| Campo | M1-A: serial compacto 5R, sexto giro opcional | M1-B: XYZ con cabezal orientable | M1-R: UR5e terrestre |
|---|---|---|---|
| Requisitos / comparación | MOT-001/002; compara con B/R | MOT-001/002; compara con A | Referencia documental frente a A/B |
| Fabricante/modelo | Concepto propio, no producto | Concepto, no producto | Universal Robots UR5e, F05 diciembre 2024 |
| Prestación continua/pico | Muñeca ideal de dos enlaces; límites del [modelo](../../models/srr_agente_tecnico/README.md). Cargas/velocidades TBD | Recorrido/orientación y carga TBD; deberá cubrir mismas poses | 6 ejes; alcance 0,85 m; carga 5 kg, condiciones catálogo F05; no prestación espacial |
| Exactitud/repetibilidad | TBD; residuo matemático no es precisión | TBD; guías/encoders/calibración | No se asigna repetibilidad de catálogo al cordón |
| Masa/CG/inercia/envolvente | TBD kg, m, kg·m², m³; cuerpos no modelados | TBD, incluir marco/guías | Masa con cable 20,6 kg F05; CG/inercia TBD |
| Electricidad/consumo | TBD V/A/W; depende de actuadores/perfil | TBD V/A/W | F05: 200 W moderado, 570 W máximo; no presupuesto del concepto A |
| Interfaces | Brida/TCP/cables/tubos/base TBD, ICD-002/004 | Guías/cabezal y cableado TBD | Integración industrial no transferible automáticamente |
| Materiales/compatibilidad | BOM, lubricantes, sellos y emisiones TBD | Igual, más guías/portacables | Ficha no acredita compatibilidad de resina/recinto/host |
| Ambiente/límites | Estación como contexto del usuario por formalizar; no host elegido | Mismos requisitos de comparación | Equipo terrestre, sin calificación espacial presentada |
| Coste/disponibilidad | TBD USD; sin cotización 2026-10-12 | TBD USD; sin cotización | TBD USD y revisión actual; ficha histórica sin precio |
| Calificación | No existe evidencia | No existe evidencia | No se aporta calificación espacial |

Decisión: desarrollar A bajo TBR para justificar cinco variables de tarea; revisar sexto giro cuando óptica/cables lo requieran. B sigue en comparación. Primero alcance, seguridad/retención y compatibilidad; después masa/coste. Datos faltantes impiden ponderación sustentada. Para verificar: CAD con cuerpos y barrido continuo, cargas/tubos/rigidez y revisión independiente. [Propuesta](propuesta.md) · [Fuentes](../../models/srr_agente_tecnico/fuentes.md).
