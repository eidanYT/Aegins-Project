# Fichas ópticas — M3

Versión 0.1, 2026-10-12, **TBR**. Humano M3/revisión especializada por asignar. [Fuentes F01–F04](../../models/srr_agente_tecnico/fuentes.md); [combinaciones material–fuente](propuesta.md).

| Campo de componente | M3-OPT-A: sectores/anillo 365 nm | M3-OPT-B: foco orientable 365 nm | M3-REF: emisor M365L3 |
|---|---|---|---|
| Fabricante/modelo | Concepto, no producto | Concepto, no producto | Thorlabs, referencia terrestre de catálogo histórico F04 |
| Requisitos / comparación | UV-001, THM-001; compara B | Mismos, compara A | Referencia de presupuesto, no selección |
| Prestación continua/pico | Mapa E y límites TBD; no asumir emisión uniforme | Mapa E/óptica/recorrido TBD | Datos espectrales/radiantes típicos en F04; no mapa de pieza |
| Exactitud/repetibilidad | Radiometría/calibración y tolerancia TBD | Igual | No se deriva dosimetría de potencia radiante |
| Masa/CG/inercia/envolvente | TBD kg, m, kg·m², m³ | Igual, incluir obturador/óptica | Cabezal/disipador/driver TBD |
| Electricidad / calor | Modelo de cuatro emisores como hipótesis, no BOM | Número de emisores/duty cycle TBD | I/V/Φ en F04; máximos de conjunto y driver TBD |
| Conexiones | Brida, corriente regulada y sensores TBD | Igual; orientación y sombra con M1 | Driver/térmica necesarios, interfaces por confirmar |
| Materiales/compatibilidad | Ventanas/pantallas/reflector y resina TBD | Igual | Banda de referencia respaldada para GE680, sin ventana de proceso propia |
| Ambiente/límites | Encapsulado/temperatura/host TBD | Igual | No calificación espacial aportada |
| Coste/disponibilidad | TBD USD; consulta 2026-10-12 sin cotización | Igual | Precio/versión/stock actual TBD; no precio histórico |
| Verificación | Mapa E, gel y curado, boquilla/sombras, calor y enclavamiento | Igual y cobertura de caras/nodos | Obtener datasheet vigente y óptica/driver exactos |

La alternativa Dymax + UV/visible tiene fuente exacta **TBD** hasta justificar su banda y exposición. No asignar un LED de 405 nm solo por disponibilidad. Elegir entre A/B según ventana material y cobertura/anclaje; mantener coexistencia de gel localizado y postexposición como propuesta hasta medir cinética. No declarar mitigación UV eficaz por dibujar un recinto opaco.
