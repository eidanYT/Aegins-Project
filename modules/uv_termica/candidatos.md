# Selección de referencia de M3

Fuente: report SRR inglés revisión 5 y traducción española. S significa seleccionado para diseño; alternativas como respaldo. Faltan dimensionamiento por función, compatibilidad y aceptación física.

| Función | Referencia y estado | Alternativas | Motivo y evidencia pendiente |
| --- | --- | --- | --- |
| M3 Fuente UV | S: Nichia NVSU233B de 365 nm | LED montado Thorlabs 365 nm; Phoseon FireJet 365 nm | NVSU233B U365 elegido: 3.85 V, 1 A y 1.45 W ópticos típicos por LED a Ts=25 °C; cuatro dan 15.4 W eléctricos antes de drivers [P16]. Verificar dosis y refrigeración. |
| M3 Disipación | S: Placa conductora y correas térmicas | Heat pipe; placa fría líquida | Referencia pasiva y flexible; exige sumidero y conductancia al alojamiento. El antecedente tecnológico no califica el conjunto. |
| M3 Temperatura | S: Pt100 en placa térmica | Termopar K; TI TMP461-SP | Medida estable y calibrable en el montaje; no mide directamente la unión LED, la resina ni la boquilla. |
| M3 Seguimiento UV | S: Fotodiodo SiC tipo SG01D | Thorlabs S120VC; Ophir PD300RM UVA | SG01D es la familia principal; se presupuesta SG01D-18 [P05]. La banda declarada al 10% del máximo llega cerca de 358 nm; verificar responsividad y margen de señal a 365 nm antes de usarlo. |

[Objetivos del módulo](README.md) · [Estado de cierre](propuesta.md).
