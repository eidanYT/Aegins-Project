# FORGE UG SRR referencia documental

Transcripción del report inglés revisión 5 con adaptación al alcance 6R vigente. Se excluyen los resultados cinemáticos sustituidos; el documento fuente conserva el historial. Se conservan tablas, textos, enlaces de fuentes y transcripción lineal de fórmulas. Las imágenes se consultan en el report de Drive; no son CAD dimensionado. Este archivo no es el PDF oficial de entrega.

Fuente: [report inglés](https://docs.google.com/document/d/1sF6ue6xzVTxw11Q5jYj6G-STlRtV-LT6/edit). El año correcto del cronograma es 2026, confirmado por Eidan el 18 de octubre. El trabajo vigente se organiza en [PDR y desarrollo avanzado](../../system/objetivos_pdr_y_desarrollo.md). Las descripciones de estado del report corresponden a su fecha; la sincronización actual se propone en estos PR.

FORGE UG SRR REPORT

ACHIEVED Orbital - SRR

AEGINS Team

Ilustración en el report fuente de Drive; no constituye CAD dimensionado.

Preliminary design for team review

FORGE-UG

Project ACHIEVED Orbital 2026

Doc. Ref. FORGE-UG-SRR-2026-EN

Doc. Type Report

Issue 1

Revision 5

Date of issue 15 October 2026

Prepared by Ajahuana Quiroz , Eidan

Yauri Huamani, Shelton

Quispe Papuico, Nicolas

Zelada Adiel, Andres

Oscco Tomilla, Isaac

Hurtado Curi, Gabriel

Approved by AEGINS

Distribution Team review

Contents

1. Introduction 3

2. Context and objectives of the solution 3

3. Feasibility Analysis 5

4. Design Definition & Justification 8

5. Market Analysis & Costs Assessment 19

6. Risk Assessment 23

7. Project Management & Timeline 24

8. Verification and Development Plan 25

9. Physical validation and future activities 27

10. Conclusions 28

References and document basis 28

1. Introduction

Space crews need tools, replacement parts and custom components to maintain equipment and carry out new experiments. If the right item is not on board, work may be delayed or adapted while a replacement is manufactured on Earth and delivered on a later cargo mission. Launching finished articles also requires packaging, storage and logistics. Local manufacturing can address selected needs using feedstock and digital designs already available at the destination. NASA identifies this logistics problem as a motivation for in-space manufacturing [R1].

FORGE-UG proposes a robotic additive-manufacturing payload for operation inside a process chamber on a crewed space station. A six-axis articulated arm would position and fully orient a resin-extrusion head while ultraviolet light stabilises the deposited material. Orientable deposition could support non-planar trajectories and access to curved surfaces. The purpose is to develop a credible route to more adaptable local manufacturing, with geometric performance and operational benefit assessed against simpler alternatives.

The feasibility argument connects two established foundations: robotic printing demonstrated on Earth, including robotic resin extrusion with UV curing, and additive manufacturing demonstrated in reduced gravity and orbit. Our contribution is to analyse how these capabilities can be integrated for the selected station application, quantify initial process demands, and resolve the engineering challenges of motion, material delivery, curing, containment and measurement. This is a supported engineering concept; approval of one previous experiment does not transfer flight approval to the proposed integrated payload.

The competition deliverable is a preliminary design supported by literature, requirements, analysis and a CAD plan. The specimen is a square bipyramid with twelve 0.05 m edges and eight closed faces. The first material/component options in D1 are now the team-selected primary references; alternatives remain as backups. Thickness, detailed variants, dimensions and host allocation require engineering closure. Selection does not establish flight approval.

2. Context and objectives of the solution

Experimental foundations

The following examples identify who performed the work, where and when it was reported, and which capability it establishes. Laboratory demonstrations, short reduced-gravity campaigns and orbital operation are distinguished because they answer different engineering questions. Publication years are not treated as flight dates.

| Project and team | Place and date | Demonstrated capability and relevance |
| --- | --- | --- |
| Robotic UV extrusion — Luis Velazquez, Genevieve Palardy and Corina Barbalata [R2] | Louisiana State University, Baton Rouge, USA; manuscript posted 24 August 2021. | A UR5e arm with a custom extruder and UV source printed small 2D and 3D polymer specimens. Direct terrestrial precedent for combining an articulated arm, resin extrusion and UV curing. |
| Conformal Robotic Stereolithography — Adam G. Stevens and colleagues, MIT [R3] | Massachusetts Institute of Technology, USA; December 2016. | Six-axis robotic photopatterning produced features on curved substrates. Supports curved-surface path planning; this is projection photopolymerisation, not extrusion. |
| 3D Cocooner — Festo Bionic Learning Network [R4] | Festo, Germany; 2016 project brochure. | Parallel-kinematic robot placed resin-coated glass-fibre strands and cured them with UV to form lattices. A process analogue, not an articulated serial arm or a closed-face resin shell. |
| Free-flying robotic manufacturing — Declan Jonckers, Oliver Tauscher, Aditya R. Thakur and Lasse Maywald [R5] | TU Braunschweig, ELISSA laboratory, Germany; 14 April 2022 publication. | A mobile air-bearing platform with robotic arm and thermoplastic printhead produced truss segments. Demonstrates coordinated robotic deposition with a floating base; it remained a terrestrial experiment. |
| DREPP — Michael Kringer and colleagues, Munich University of Applied Sciences [R6] | Parabolic-flight experiments; article published 23 August 2022. | Photopolymer extrusion and UV curing produced geometric elements in reduced gravity. A two-translation, one-rotation mechanism was used; this was not an orbital articulated-arm experiment. |
| 3D Printing in Zero G — NASA and Made In Space [R7,R8] | International Space Station; first object manufactured 24 November 2014; full results published 2018/2019. | Fused-filament fabrication operated in orbital microgravity. Establishes the physical practicality of controlled extrusion printing aboard a crewed station, with its own materials and safety configuration. |
| Metal 3D Printer — ESA, Airbus and partners [R9] | ISS Columbus module; first completed metal shape in August 2024, reported 6 September 2024. | A metal-manufacturing demonstrator operated on station. Broadens orbital manufacturing evidence; it is a different process and is not a resin-system qualification. |

Further photopolymer evidence includes AIMIS-REXUS, reported by Kringer and colleagues in 2024 after a REXUS 27 experiment at Esrange, Sweden [R10], and PERSIS, reported by Raphael Strecker and colleagues in 2026 after a 2025 REXUS 33 flight [R11]. These studies extend extrusion and UV-curing research to suborbital conditions and identify defects and process sensitivities to address. Orbital Matter reported resin extrusion and UV curing in low Earth orbit in August 2026 [R12]; this is identified as a manufacturer report, not independent proof of our proposed arm configuration.

Challenge and rationale

The operational need is access to suitable parts without depending on a separate delivery for every new geometry. The proposed arm addresses access and orientation: it can potentially place the nozzle along non-planar paths and around curved workpieces. A Cartesian system remains the comparison because it may provide a smaller, stiffer or simpler solution for some tasks. FORGE-UG must establish when orientation freedom adds enough manufacturing value to justify its joints, calibration, cables and containment volume.

Our engineering task is to adapt the demonstrated process elements to a station-compatible design. Microgravity changes the balance between weight, surface tension, viscosity, adhesion and curing; it does not remove extrusion forces or ensure higher precision. A small initial anchor is a design option whose loads and stability will be analysed. Building the eight closed faces introduces additional challenges of track support, bonding, shadowing, final closure and inspection that do not follow automatically from successful rod printing.

Competition objective

During the competition, we will evaluate analytical feasibility and produce a traceable preliminary design. The deliverables are the reference mission and specimen, mission and system requirements, architecture comparison, nominal geometry and integrated-CAD plan, process and resource models, a verification strategy, risk assessment, business case and development schedule. Existing experimental data provide physical foundations and useful parameter ranges; calculations evaluate our selected geometry under declared assumptions.

Long term objective and innovation

The long-term objective is a commercial robotic manufacturing platform for crewed stations and other suitable facilities. Development will progress through a calibrated ground demonstrator, reduced-gravity testing and a hosted orbital demonstration. Target benefits are access to more complex geometries, lower support or fixture demand where practical, and improved measured performance for selected tasks. Commercial deployment requires those benefits, safe operation and customer value to be demonstrated.

The proposed innovation is the integration of orientable extrusion, UV curing, containment and metrology around an operational need in space. The project contributes a specific architecture, quantitative assessment and comparison protocol. Its value does not depend on claiming the first robotic printer: earlier work already supports the approach. Modular extensions could later address other materials and applications, as discussed in Section 5.

3. Feasibility Analysis

Technical feasibility

The concept does not require a new physical principle. Robotic deposition, pressure or positive-displacement feeding, photopolymerisation and optical measurement are available foundations. Space adaptation requires engineering of their interfaces, operating envelope and fault response. The repository already contains a five-module architecture, an ideal robot model, geometric raster, flow and exposure calculations, a containment balance and a conceptual control model [G1,G2]. We use these results as preliminary sizing evidence, with GE680 as the study reference.

The analytical case separates team-defined geometry from study assumptions. The square base, 0.05 m edges, closed faces and crewed-station chamber are the reference decisions. The 0.0012 m bead diameter and track width, 0.0005 m wall thickness, 0.005 m/s speed, feed-line geometry and optical exposure are sensitivity inputs. SI units are used in the models; millimetres, millilitres and watt-hours are used only for readable displays.

Motion and deposition

Six-axis 6R verification is pending: dimensioned CAD, full position and orientation FK/IK, continuous time-parameterised paths, singularities, collisions, hose twist and loads. Earlier kinematic results are excluded from current design evidence.

Fórmula del documento: `p W  = p − b − l d     p = f(q)`

Here p is TCP position, b base position, l the tool offset, d its axial unit direction, and pW wrist position. For the selected arm, q = (q1, q2, q3, q4, q5, q6). Full tool orientation R(q) is commanded in addition to p(q); direction d alone does not specify roll. Joint position, speed, acceleration, clearance and finite hose-twist limits constrain the six-axis path.

Fórmula del documento: `Q edge  =  π  d 2  v 4       Q face  = w t v`

For steady deposition, flow Q equals deposited cross-section times travel speed v. Edge strands use an ideal circular diameter d; face tracks use width w and thickness t. The repository case gives 5.655 × 10⁻⁹ m³/s for edges and 3.000 × 10⁻⁹ m³/s for face tracks. These demands are compatible with a pressure-driven or piston-driven concept; the head must be characterised to turn commanded flow into deposited geometry. Extrusion is driven by pressure or displacement, rather than gravity [G1,R6].

Fórmula del documento: `ΔP = Σ  8 η  L i  Q π  r i 4       F ideal  = ΔP  A p       u p  =  Q A p`

The pressure example treats each line segment as a straight circular duct with stationary, laminar, Newtonian flow. Viscosity η = 54 Pa·s is a single catalogue reference used in the repository, not a measured nozzle-flow law. With assumed nozzle radius 0.0006 m and length 0.01 m, tube radius 0.002 m and length 0.5 m, and a 0.02 m piston diameter, the edge-flow calculation gives ΔP = 84.3 kPa and ideal piston force 26.48 N; face-flow values are 44.72 kPa and 14.05 N. These are sensitivity results, excluding seals, friction, yield stress, bubbles, compliance and start/stop transients. The governing force model can be refined after rheology and circuit characterisation [G1].

Curing and thermal feasibility

Fórmula del documento: `H = ∫ E(t) dt      t exp  =  L UV v      H = E  t exp   (uniform E)`

Exposure H is the time integral of irradiance E at the material. The illustrative 0.002 m illumination length at 0.005 m/s gives 0.4 s residence time; a uniform 2500 W/m² gives 1000 J/m². This is an exposure calculation, not an established cure threshold. Wavelength, conversion, gel strength and bonding must be related to the selected formulation. A simple angular model gives an incidence factor of 0.577 on four faces and zero on the opposite four for illumination from +z, explaining why coordinated orientation merits study [G1].

Fórmula del documento: `C  dT dt  =  P heat  +  P reaction  − G(T −  T b ) − ε σ A( T 4  −  T env 4 )`

C is thermal capacitance, G conductance to Tb, ε emissivity, A radiating area and σ the Stefan–Boltzmann constant; temperature terms use kelvin. The repository optical case remains historical [G1,G2]. For the selected four-emitter cost scenario, Nichia specifies typical 3.85 V and 1.45 W radiant flux per U365 LED at 1 A and Ts = 25°C [P16]. This gives 15.4 W LED electrical input, 5.8 W emitted optical power and 9.6 W local LED heat before driver losses. Internally absorbed light and reaction heat are counted once in the enclosure heat balance. Temperature, bin variation, optics and actual duty require verification.

Measurement and analytical checks

Fórmula del documento: `e time  ≤  v max  Δt      Δt allow  =  e allow v max`

A timing mismatch contributes a displacement bounded by the speed bound multiplied by total delay. The existing example of 0.005 m/s and 0.05 s gives 0.00025 m. An illustrative 0.0001 m timing-error allocation would permit 0.02 s total delay; it is not an approved mission tolerance. We record acquisition time, command time, clock mapping and data validity so that a commanded robot position is not reported as a measured material position [G2].

Six-axis 6R verification is pending: dimensioned CAD, full position and orientation FK/IK, continuous time-parameterised paths, singularities, collisions, hose twist and loads. Earlier kinematic results are excluded from current design evidence.

Feasibility status by module

The available work is analytical. No project-specific physical test capability or completed test is documented. The matrix identifies what can be assessed now and what requires future equipment, funding and acceptance criteria; PV01 to PV06 are detailed in Section 9.

| Module | Current selection | Assessable now | Not established by this SRR |
| --- | --- | --- | --- |
| M1 Motion | 6R; 6061, EC 32 flat, CSF/CSG, RESOLUTE, EPOS4 | 6R CAD/kinematics, continuous paths, FEM and loads | Six-axis 6R verification is pending: dimensioned CAD, full position and orientation FK/IK, continuous time-parameterised paths, singularities, collisions, hose twist and loads. Earlier kinematic results are excluded from current design evidence. |
| M2 Process | GE680, viproHEAD 5, steel nozzle, PTFE and Kulite selected | SDS review, conditional flow/pressure and inventory models | No measured rheology, species emissions, bond or closed-face process; PV01. |
| M3 UV and heat | NVSU233B 365 nm, plate/straps, Pt100 and SG01D selected | Optical dose, thermal path and uncertainty models | No confirmed cure threshold, panel attenuation or temperatures; PV01/PV03. |
| M4 Containment | MSG-type barrier + fan depression; HM, Δp, U51 and HEPA/carbon selected | Pressure-hold protocol, air circuit, mass/power and loaded-filter analysis | Selected architecture; leak/pressure performance and UV safety not yet tested; PV02–PV04. |
| M5 Control | GR740, SAMRH71, RTG4, CASPEX, 3D PLUS, MRAM, SVR and CAN selected | TSIM/software studies, timing and data/uncertainty budgets | No hardware latency, metrology or radiation validation; PV05/PV06. |
| Integration and cost | References selected; 6R hardware: USD 157,086.91 | Interfaces, analytical budgets and RFQ packages | Host agreement, funded tests and qualification remain future gates; PV06. |

Economic feasibility

The initial business case is a research and development service that combines a contained robotic-printing experiment with calibrated process data. A later product could supply qualified parts on demand. Local manufacture still requires a printer, feedstock, power, inspection and maintenance; savings arise only when these costs are lower than the avoided inventory, delivery or disruption costs for suitable parts. Section 5 provides a transparent planning estimate and a break-even model rather than treating the price of a terrestrial printer as the price of a flight mission.

Environmental feasibility and sustainability

The environmental assessment uses one accepted specimen as the functional unit and compares equal useful performance. Its inventory includes feedstock manufacture and launch, cartridge and line losses, electricity, curing, cleaning, rejected parts, filters or sorbents if used, and waste storage or disposal. The illustrative UV subsystem consumes 24640 J during ideal deposition; this is a partial energy inventory, not the experiment total. Reuse of calibration fixtures, replaceable cartridges and process control may reduce waste.

The system will retain uncured material and waste throughout the operating cycle. Direct discharge into the cabin, life support or external space is not an available baseline interface. Environmental benefits will be assessed across the lifecycle, including the additional robot and chamber; reducing one shipment or one support structure is not by itself proof of lower total impact.

Resilience modularity autonomy and additional considerations

Durability will be addressed through material compatibility, protected storage, thermal control, launch retention, calibration stability and replaceable wear items. Modular mechanical, fluidic, optical and data interfaces allow a failed cartridge or printhead to be replaced without discarding the platform, subject to safe access. The station configuration protects the process from direct external vacuum and thermal cycling, but does not remove radiation, launch, contamination or reliability requirements.

Autonomy is initially limited to executing an approved path, monitoring valid signals and entering a controlled fault sequence. Recovery and access require authorised review; the logical HOLD state is not a substitute for physical isolation or retention after power loss. For future exploration logistics, digital designs could reduce the need to preselect every part geometry, while feedstock supply, qualification and inspection remain necessary. Social and ethical considerations include crew workload, transparent quality records and avoiding claims of medical or safety-critical use before the corresponding approvals.

4. Design Definition & Justification

Reference mission and operating environment

The reference mission is an intravehicular experiment on a crewed station in low Earth orbit. The ISS is used as an environmental reference: we adopt a round 400 km study altitude and its 51.6° inclination. NASA describes its orbital period as 90–93 min depending on altitude [R15]. This is not a booked ISS payload or a selected rack. A circular-orbit calculation with an adopted equatorial Earth radius of 6378137 m and gravitational parameter of 3.986004418 × 10¹⁴ m³/s² gives a period of about 92.6 min at the study altitude. These are modelling inputs and a representative orbit, not a current ephemeris.

Fórmula del documento: `T = 2π  ( R E  + h) 3 μ`

The payload’s actual boundary conditions come from its internal location: local pressure and temperature, residual accelerations, ventilation or conductive heat paths, radiation shielding, power quality, mounting and data service. Orbital altitude alone cannot specify them. The process is not exposed directly to vacuum in the reference configuration. The host interface must define allowed disturbances and contamination, while the launch provider defines the transport and vibration environments [R17]. No cabin pressure, cooling connection or vent capability is assumed from the orbit.

Functional architecture and Interfaces

Ilustración en el report fuente de Drive; no constituye CAD dimensionado.

Figure 1. 6R functional architecture and MSG containment. Hardware interlocking is independent of the CPU; the schematic does not replace air-circuit design or detailed CAD.

Preliminary 3D model

Ilustración en el report fuente de Drive; no constituye CAD dimensionado.

| Module | Function and principal interface | Design rationale |
| --- | --- | --- |
| M1 Motion | Control full tool pose with six axes; publish position, orientation and time to M5. Verify loads and hose routing in ICD-002. | Tool roll supports optical orientation and hose planning; compare its benefit and complexity against Cartesian motion. |
| M2 Material and extrusion | Store and meter material; exchange speed/flow commands with M1/M5 through ICD-001. Feed pressure and inventory inform ICD-005. | Controlled displacement or pressure drives extrusion. Remote feeding reduces moving inventory but adds retained volume and compliant tubing. |
| M3 UV and thermal | Coordinate optical exposure with deposition; provide temperature and exposure data. Share heat through ICD-004. | Curing follows the material and path, with optical shielding and a defined heat-rejection route. |
| M4 Chamber and integration | Provide mounting, containment, access and agreed host services through ICD-004/005. | Protect crew and host through assessed barriers and operating procedures; no direct gas discharge is assumed. |
| M5 Control and metrology | Supervise six axes and synchronise commands/measurements through ICD-001/003; coordinate valid signals, faults and resources with M4. | Separate observations from estimates, detect stale signals and coordinate recovery with M4 and the host. |

The first option for each of the 30 functions in register D1 is now the team-selected primary reference, marked S. The remaining options are backups. Selection fixes the preferred material, technology or product family; dimensions, suffixes, ratings and interfaces still require engineering verification. Selection does not establish procurement, successful testing or flight acceptance.

Material and component selection by module

The study reference adopts DELO KATIOBOND GE680 resin and 365 nm exposure. Wall thickness and the flow, dose and cure operating window remain open. GE680 appears in reduced gravity printing research [C7,C9]. Its SDS identifies hazards and reportable ingredients, but does not provide the complete formulation or emissions per cycle.

| Function | Reference and status | Alternatives | Reason and remaining evidence |
| --- | --- | --- | --- |
| M1 Arm structure | S: Aluminium 6061; 6R arm | 7075; Ti 6Al 4V; CFRP | Six joints; dimension links, wrist and hose twist. Material choice does not qualify the assembly. |
| M1 Motor | S: maxon EC 32 flat, adapted | Phytron phySPACE/VSS; Kollmorgen TBM2G | Primary motor family selected. Cost uses 24 V / 15 W / Hall variant 267121; NRND status requires availability review [P01]. Space adaptation and joint torque/life remain to be demonstrated. Budget: 6 units; size each joint. |
| M1 Transmission | S: Harmonic Drive CSF/CSG | adapted maxon GP 22 UP; direct drive | Compare reduction, backlash, compliance, lubrication and life. Direct drive removes the gearbox but increases torque demand. Budget: 6 units; size each joint. |
| M1 Angle sensing | S: Renishaw RESOLUTE | Celera Motion IncOder; Moog resolver | Compare resolution, contamination sensitivity, alignment and conditioning. No flight claim for the proposed article. Budget: 6 units; size each joint. |
| M1 Motor controller | S: maxon EPOS4 | Elmo Gold Twitter; custom MCU stage | Fast loops remain local. Budget uses EPOS4 Module 50/5 534130 [P02]. Carrier, power and encoder protocol must be matched; a published readhead price does not demonstrate direct EPOS4 compatibility. Budget: 6 units; size each joint. |
| M2 Feedstock | S: DELO KATIOBOND GE680 | Dymax 4 20806; Formlabs Tough 2000 V2 | Reduced-gravity process evidence motivates GE680 [C7,C9]. Verify rheology, bonding, dose and emissions; alternatives need free-strand testing. |
| M2 Dispenser | S: ViscoTec viproHEAD 5 | Custom motorised piston; Nordson Ultimus V | Positive displacement and parabolic-test precedent [C9]. Compare pulsation, cleaning, retained volume and transients; no orbital qualification. |
| M2 Nozzle | S: Stainless-steel nozzle | technical ceramic; Vieweg-type opaque conical tip | Check wear, wetting, UV entry, pressure loss and cleaning. Exact article and compatibility remain open. |
| M2 Feed line | S: UV-protected PTFE | opaque-protected PFA; 316L | Balance chemical compatibility and routing against permeation, retained volume, compliance and moving mass. |
| M2 Extrusion pressure | S: Kulite aerospace/space pressure-sensor family | Keller 33X; Honeywell PPT2 | Select range and response from maximum credible pressure and transients; verify wetted materials. Separate from chamber air pressure. |
| M3 UV source | S: Nichia NVSU233B, 365 nm | Thorlabs mounted 365 nm LED; Phoseon FireJet 365 nm | Selected NVSU233B U365: 3.85 V, 1 A and 1.45 W optical typical per LED at Ts=25 °C; four give 15.4 W electrical before drivers [P16]. Dose map and cooling require verification. |
| M3 Heat removal | S: Conductive plate and thermal straps | Heat pipe; liquid cold plate | Passive reference with routing flexibility; requires host sink and conductance. Technology heritage does not qualify the assembly. |
| M3 Temperature | S: Pt100 on thermal plate | Type K thermocouple; TI TMP461-SP | Stable calibrated measurement at the mounting point; does not directly measure LED junction, resin or nozzle temperature. |
| M3 UV monitoring | S: SiC photodiode, SG01D type | Thorlabs S120VC; Ophir PD300RM UVA | SG01D is the primary family; cost uses SG01D-18 [P05]. Its listed 10%-of-peak response band ends near 358 nm; responsivity and signal margin at 365 nm must be verified before use. |
| M4 Opaque base | S: Aluminium 6061 opaque base | 316L; Ti 6Al 4V | Machinability and heat conduction motivate 6061. Thickness, finish, mounting and cleaning remain to be designed. |
| M4 Transparent panels | S: Lexan polycarbonate sides and roof | Borosilicate; fused silica | Impact tolerance motivates polycarbonate. MSG/Cupola are material precedents [C6]; our grade, seals, fire and ageing need verification. |
| M4 Window UV barrier | S: Rosco R3114 absorbing film | Custom UV-absorbing coating; specified UV-absorbing glass | Preserve visible observation. R3114 transmission claim alone is insufficient: verify 365 nm, exposure, adhesive and ageing [C5]. |
| M4 Opaque optical finish | S: Acktar Fractal Black | Specified space black anodising; specified space black paint | Low-reflectance reference with declared heritage [C5]. Check 365 nm and resin/cleaning compatibility; apply only to opaque parts and count absorbed heat. |
| M4 Door closure | S: Honeywell HM closure switch | Reed and magnet; optical sensor | Sealed contact selected reference [C8]. Analyse mounting and faults; physical UV inhibition is required. Closed contact does not demonstrate leak tightness. |
| M4 Air differential pressure | S: Low-differential piezoresistive sensor | capacitive differential; paired absolute sensors | Monitor chamber versus cabin. Define range, drift and uncertainty; subtraction of large absolute pressures can be inadequate. |
| M4 Ventilation | S: Micronel U51 centrifugal blower; 3 units | Axial; mixed-flow fan | Selected MSG-type suction/return/reference circuit [C3]; 2 active + 1 standby U51. Size valves and loaded curves; verify pressure, power and vibration. |
| M4 Contaminant retention | S: HEPA and activated carbon in MSG-type air circuit | HEPA and species-specific sorbent; sealed retention or approved receiver | Selected MSG-type containment [C3]. Test GE680 species, filter capacity, bypass and contained exchange; no achieved removal efficiency claimed. |
| M5 Central computer | S: GR740-based central computer | GR712RC OBC; RAD750 SBC | Four-core space processor motivates study [C1,C2]. Processor heritage is distinct from board qualification; CPU, memory, heat and interfaces remain open. |
| M5 Local MCU | S: Microchip SAMRH71 | SAMV71Q21RT; STM32H743 ground comparator | Compare deadlines, interfaces and radiation strategy. Space-oriented chips still require board and software verification. |
| M5 FPGA | S: Microchip RTG4 | RTAX; AMD XQRKU060 | RTG4 is selected as the FPGA reference. B25 budgets one separate evaluation kit for integration work; deployment and workload remain to be validated. Development kits do not qualify a flight assembly [P10,P17]. |
| M5 Imaging | S: CASPEX 4 Mp camera family | CIS115-based camera; Basler ace 2 global shutter | Compare field, optics, exposure, interfaces and uncertainty. Sensor/family heritage does not establish an integrated qualified camera. |
| M5 Working memory | S: 3D PLUS space SDRAM | Frontgrade UT8R1M39; ISSI IS42S16160L comparator | Size CPU/image buffers and verify interface, ECC and radiation strategy. Family heritage does not identify the required article. |
| M5 Storage by function | S: Frontgrade UT8MR2M8 MRAM | RTIMS VIM1 NAND for bulk; industrial Kioxia eMMC comparator | MRAM is selected for critical states and parameters. UT8MR2M8 is 16 Mbit (2 MB); it does not close bulk image storage. Size buffers and image offload separately. |
| M5 Power conversion | S: VPT SVR power-conversion family | Crane Interpoint SMRT; custom front end with TPS7H4001-SP | Select input, rails, isolation and derating. The TI low-voltage regulator needs preconversion; it is not an arbitrary direct host input. |
| M5 Internal bus | S: CAN for internal control | SpaceWire; Ethernet | CAN is selected for internal control. Camera throughput, image transfer and timestamping need a separate interface/buffer budget; CAN selection alone does not establish image-link capacity. |

Seals, adhesives, bearings, wiring, connectors, valves, brakes and anchors remain implementation items. Their hardware allowances appear in B31–B37. The selected first choices include RTG4, 3D PLUS SDRAM and UT8MR2M8 MRAM; the board-level allocation and image-storage capacity still need verification.

Polycarbonate has heritage in MSG windows and borosilicate in Cupola inner protection [C6]. Our panel grade, thickness. Rosco states less than 10% transmission below 390 nm; this figure does not demonstrate adequate crew protection. Acktar declares JWST and BepiColombo heritage for its technology; the proposed finish still needs 365 nm reflectance, resin compatibility and cleaning evaluation [C5].

Control architecture and study software

GR740 would coordinate trajectories, dispensing and UV, run the supervised sequence and log sensors and images. Fast motor loops would remain in local controllers; physical UV inhibition and safe retention would not depend on the central computer continuing to execute. The manufacturer declares four LEON4FT cores up to 250 MHz and TRL 9 for GR740. This evidence applies to the processor: the GR740 with RTG4 reference board is not flight qualified [C1]. FORGE-UG CPU, vision, memory, latency and fault tolerance budgets have not been demonstrated.

SAMRH71, RTG4, CASPEX 4 Mp, 3D PLUS SDRAM, UT8MR2M8, VPT SVR and CAN are the selected primary references. Detailed board variants, capacities, signal conditioning and interface compatibility must be dimensioned and verified. Evaluation hardware in the cost case is for ground development; announced or inherited heritage does not qualify the integrated assembly.

| Work | Candidate tools | Verifiable output |
| --- | --- | --- |
| CAD and materials | SolidWorks; Siemens NX; CATIA | Integrated model, joints, swept volume, masses and documented properties. |
| Structure and vibration | Ansys Mechanical; Abaqus; SolidWorks Simulation | Stress, modes and sensitivity; future physical correlation. |
| Flow and heat | COMSOL; Ansys Fluent; OpenFOAM | Circuit losses and thermal map with host boundary conditions. |
| Robot and control | Simscape Multibody; Gazebo with ROS 2; CoppeliaSim; TSIM for GR740 | 6R kinematic model, collisions, dynamics and timing. TSIM evaluates CPU; it does not replace tests. |
| Optics | Ansys Speos; OpticStudio; COMSOL Ray Optics | Irradiance, reflections and transmission using measured spectral data. |

Simulation uses actual grades and operating conditions. Section 5 now gives a numerical component-based procurement scenario, with published prices separated from internal allowances. The estimate includes development hardware and does not establish a flight-unit procurement price.

Containment and operations

Fórmula del documento: `V  dC dt  = G − R     C(t) =  C 0  +  G t V   (R = 0)`

The selected containment baseline follows the ISS Microgravity Science Glovebox (MSG): a physical enclosure plus fan-driven negative pressure and HEPA/activated-carbon treatment. The contaminant balance includes circulation, filtration, leakage and the filtered reference path. GE680 species and removal capacity still require PV01/PV04; choosing this architecture does not imply completed containment testing [C3].

Operations proceed through retained launch/storage, installation, checkout, calibration, anchor preparation, contained priming, printing, stabilisation/postcure, inspection and secure storage. Start requires the closed barrier, passed leak check, valid pressure and sensor/calibration/time data. A fault coordinates motion, resin pressure, flow and UV inhibition. Power-loss retention is physical. Access requires acceptable pressure, temperature, optical exposure and contamination. PV02 establishes tested thresholds and frequency.

Barriers and closure verification

The selected seal-verification system combines the Honeywell HM door contact, chamber-to-cabin piezoresistive differential-pressure sensing, and an isolated pressure-hold test. The pressure sensor has a chamber tap and a cabin reference; it checks the pressure condition, while the HM checks mechanical closure. Kulite separately measures resin pressure. Door open, invalid pressure, failed leak check or lost power removes the physical UV/extrusion permissive. The system principle is defined; calibration, thresholds and demonstrated performance are PV02 outputs.

We adopt the MSG leak-test method: close and lock the barrier, isolate intentional airflow openings, establish negative pressure, stop the fans and record chamber/cabin pressure and temperature over the hold interval. ESA’s June 2007 MSG benchmark was −5 mbar initially and no rise above −3.75 mbar after 30 min (a rise toward cabin pressure of at most 1.25 mbar) [C3, pp. 9–10]. These are proposed reference conditions for our test planning, not demonstrated FORGE-UG results or automatically approved acceptance limits.

Filtration and air mass balance

Normal mode follows the MSG arrangement: air is drawn from the working chamber through filters and fans, then routed through the air-handling/valve path back to the chamber, with a filtered reference outlet. Pressure in the working volume is monitored relative to cabin; pressure losses across filters are separate quantities. Our selected U51 configuration is two active plus one standby with branch isolation. MSG is the architectural precedent; this specific 2+1 arrangement remains our implementation choice [C3].

The selected circuit has separate suction, return and filtered-reference paths, rather than a fan mixing one undivided volume. Sealed mode closes intentional paths and stops the fans. Size ducts, valves and loaded-filter operating points against Micronel curves [C3,J04].

Host review must accept the filtered reference path for the actual GE680 emissions; no unfiltered release or ISS vacuum access is assumed. PV02/PV04 verify filter capacity, bypass, valve closure, fan loss and safe access. The sealing architecture is already selected.

Resource budgets and host compatibility

Line masses are totals in grams (g); the summary uses kilograms (kg). V denotes volts only and A amperes. “ref.” identifies a reference variant and “calc.” a calculation; missing values are not zero. Passive parts need no supply. S1/S2 remain partial scenarios, not measured consumption.

Component mass and electrical inventory

| Component | Qty | Total mass g | Voltage / current | W S1 / S2 | Basis / missing detail |
| --- | --- | --- | --- | --- | --- |
| M1 6061 arm | 1 | CAD | Passive | 0 | Arm geometry required |
| M1 EC32 flat 267121 | 6 | 342 | 24 V; 0.5 A/motor | 43.20 / 72 | 57 g/u; catalogue + S1 factor [P01] |
| M1 CSG-14-50-2UH-LW | 6 | 1920 | Passive | 0 | 320 g/u; reference variant [J01] |
| M1 RESOLUTE BiSS C | 6 | 108 | 5 V ±10%; ≤0.25 A/head | 7.50 / 7.50 | 18 g/u; excludes rings/cables [J02] |
| M1 EPOS4 Module 534130 | 6 | 102 | 10–50 V; design 24 V | 12 / 12 | 17 g/u; 2 W/u assumed loss [P02] |
| M2 GE680 resin | 2 × 50 g | 100 | Passive | 0 | Stock allowance; containers extra |
| M2 vipro-HEAD 5 | 1 | ≈750 | 24 V; ≤1.4 A/phase | 7.2 / 12 | Head catalogue; W assumed [J03] |
| M2 Steel nozzle | 2 | CAD | Passive | 0 | Need length and inner/outer diameters |
| M2 Protected PTFE | 0.5 m ref. | CAD | Passive | 0 | Need tube diameters and protection |
| M2 Kulite pressure | 1 | PN | PN required | ND | Kulite model/range not specified |
| M3 NVSU233B U365 | 4 | 0.148* | 3.85 V typ.; 1 A/LED | 15.4 / 15.4 | 0.037 g/u bare package [P16] |
| M3 Plate + straps | 1 set | CAD | Passive | 0 | Need plate/strap dimensions |
| M3 Pt100 + MAX31865 (bench) | 1 | 22.0 ref. | 3–5 V readout; passive RTD | ND | 3290: 19.3 g + 3328: 2.7 g [J06] |
| M3 SG01D + amplifier | 1 | Not stated | 0 V bias possible; amplifier TBD | ND | SG01D-18; mass not in sheet [J07] |
| M4 Al6061 base | 1 | 2160 calc. | Passive | 0 | Illustrative base; CAD not final |
| M4 Lexan sides + roof | 5 panels | 3840 calc. | Passive | 0 | Illustrative 5 panels; CAD not final |
| M4 Rosco R3114 | 2 sheets | Area | Passive | 0 | Need installed area/areal mass |
| M4 Acktar coating | 1 lot | 16–32 × S | Passive | 0 | g/m² × coated area S [C5] |
| M4 Honeywell 1HM1 | 1 | ≤6.35 | Dry contact; no supply | ND | 1HM1 maximum; sense circuit TBD [J08] |
| M4 Differential pressure | 1 | PN | PN required | ND | Piezoresistive Δp: model missing |
| M4 U51DL-024KK-4 | 3; 2 on | 360 | 12–28 V; nominal 24 V | 46 / 86 | 120 g/u; two active + spare [J04] |
| M4 HEPA + carbon | 2 sets | PN | Passive | 0 | Need filter/cartridge model |
| M5 GR740 computer | 1 | Board | 5 V; <1.4 A reference | 7 / 7 | GR-SBC reference; board mass unstated [J05] |
| M5 SAMRH71 | 1 | Board | 12 V EK; chip 1.8/3.3 V | ND | EK mass not published; rails ≠ input [J09] |
| M5 RTG4 | 1 | Board | Chip 1.2/3.3 V; I/O varies | ND | Board mass/input TBD; see rail note [J10] |
| M5 CASPEX 4 Mp | 2 | 128 | 5–9 V; design 5 V | 10 / 10 | 64 g/u budget; 62 g brochure [J11] |
| M5 3D PLUS SDRAM | 1 scope | PN | Depends on exact PN | ND | Family only; embedded RAM not added |
| M5 UT8MR2M8 MRAM | 1 scope | Package | 3.3 V nominal (3.0–3.6 V) | ND | Need package/count; read/write load [J12] |
| M5 VPT SVR + PDU | 1 set | ≤55 ref. + PDU | 18–40 V in; 5 V ref. out | Losses ND | SVRTR2805S reference only; see note [J13] |
| M5 CAN interfaces | 7 assm. | PN/PCB | Transceiver PN required | ND | 6 axes + supervisor; PN/PCB pending |
| M3 LED driver B33 | 1 set | PN/PCB | 24 V assumed; 0.755 A total | 2.72 / 2.72 | Driver PN missing; η=85% assumed |
| Shared auxiliaries | 1 scope | Inventory | Rail allocation TBD | 5 / 5 | 5 W partial allowance |
| Joints, rings, seals, valves, harness, optics | B31–B37 | Inventory | By fitted part | ND | Need dimensions/PNs and quantities |

LED masses exclude PCB/optics; RESOLUTE excludes rings/cables. Six EPOS4 534130 modules weigh 6 × 17 g = 102 g = 0.102 kg; input 10–50 V DC (24 V design). The 206 g value belongs to 546047. RESOLUTE may require separate 5 V: its 250 mA bound exceeds EPOS4’s 100 mA sensor output [J02,P02].

The sixth motor/gear/readhead/EPOS4 package adds 0.412 kg (0.057 + 0.320 + 0.018 + 0.017). M1 accounted mass is 2.472 kg; total partial mass is 9.838498 kg plus missing items. The illustrative 6.000 kg base/panels, 0.100 kg resin stock, 22 g bench Pt100 assembly, 6.35 g switch allowance and 128 g cameras are retained. Sixth-axis housing, joints, rings, wiring, structure and other unquantified items are additional. The reference VPT converter remains excluded until variant/count are fixed [J01,J02,P01,P02,J06,J08,J11,J13].

Module totals and operating assumptions

| Module | Mass kg | S1 W | S2 W | S2 share* |
| --- | --- | --- | --- | --- |
| M1 | 2.472000 + TBD | 62.70 | 91.50 | 39.8% |
| M2 | 0.850000 + TBD | 7.20 | 12.00 | 5.2% |
| M3 | 0.022148 + TBD | 18.12 | 18.12 | 7.9% |
| M4 | 6.366350 + TBD | 46.00 | 86.00 | 37.5% |
| M5 | 0.128000 + TBD | 17.00 | 17.00 | 7.4% |
| Shared auxiliaries | TBD | 5.00 | 5.00 | 2.2% |
| Partial subtotal | 9.838498 + TBD | 156.02 | 229.62 | 100%* |

* Shares use only the tabulated DC subtotal. They equal current shares only when all loads are referred to the same voltage with equal conversion efficiency. Do not add currents from 3.85, 5 and 24 V rails. ND loads are excluded from both the denominator and the scenarios.

Ilustración en el report fuente de Drive; no constituye CAD dimensionado.

Figure 2. Six-axis partial mass and nominal voltages. TBD is unquantified mass; the sixth axis does not change nominal rails. M5 shows chip/board rails, not a single module input. Ranges and conditions are in the component table.

For six motors, S1/S2 inputs are 43.2/72 W; add 7.5 W for six readheads and 12 W assumed EPOS4 losses. M1 is 62.70/91.50 W. S1 retains the 60% motor factor, 7.2 W dispensing and 23 W per active blower at pressure shutoff (zero flow); it is a sensitivity case, not a valid mission operating point [J04]. S2 uses 12 W dispensing and two 43 W blower ratings. Both retain 5 W per camera. Missing MCU/FPGA/memory/sensor/CAN loads and transients are additional. Six stalled motors alone imply 250.56 W at 24 V.

Six-axis DC subtotals S1/S2 are 156.02/229.62 W. At assumed 28 V host input and 85% upstream efficiency, input is 183.55/270.14 W and 6.56/9.65 A. A 20% allowance on S2 gives 324.17 W / 11.58 A, still plus missing loads/transients. S1 over the inherited 1600 s deposition-only example gives 81.58 Wh; six-axis timing and full mission energy require re-evaluation. Host voltage/allocations remain subject to ICD. The <7 W GR-SBC reference is not the B23 evaluation-board load, and its onboard SDRAM is not added twice [J05,D4].

Voltage details: Pt100 is resistive; the bench MAX31865 board takes 3–5 V. SG01D supports zero-bias readout; 20 V is a reverse limit, not its supply. SAMRH71 core: 1.65–1.95 V; I/O: 3.0–3.6 V; its EK takes 12 V. RTG4 adds bank/SerDes rails (1.2/1.5/1.8/2.5/3.3 V by function); board design is pending. VPT 2805S is a 5 V/30 W reference, not a whole-system supply. Retain CASPEX allowance of 5 W/head; catalogue average is 1.5 W at 25 °C. Four LEDs produce 9.6 W local heat and the assumed driver adds 2.72 W; complete thermal/host closure remains to be verified [J06–J13].

Fórmula del documento: `m total  = Σ  m i       E el  = Σ  P i   Δt i`

Fórmula del documento: `m panels  ≈ 2(LW + LH + WH) t ρ`

Mission and system requirements

This is a proposed baseline. To follow template nomenclature, SYS-SRR-01 to SYS-SRR-15 retain repository IDs in parentheses; SYS-SRR-16 to 20 add current decisions. MIS-SRR requirements are retained. A denotes analysis, T test, I inspection and D demonstration. Pending thresholds are not approved limits.

| Mission ID | Requirement | Acceptance evidence and relationship |
| --- | --- | --- |
| MIS-SRR-01 | Define a crewed-station, contained manufacturing mission and host boundary. | I: mission and agreed host-interface baseline; maps to SYS-001 and INT-002. Scenario selected; host limits open. |
| MIS-SRR-02 | Evaluate full 6R tool position/orientation against fixed orientation on equivalent accessible tasks. | A/I: same-task protocol, registered conditions and geometric metrics; maps to SCI-001/002 and MOT-001. |
| MIS-SRR-03 | Protect crew and host throughout operation, failure response and recovery. | A/I/T: reviewed hazards, retained materials and verified access/fault criteria; maps to INT-001, EXT-002 and SAF-001. |

| SRR ID and prior ID | Proposed system requirement | Method and acceptance basis |
| --- | --- | --- |
| SYS-SRR-01 (SYS-001) | Maintain one reference mission and environmental boundary. | I: controlled mission record and host-specific limits; Systems/M4. |
| SYS-SRR-02 (SCI-001) | Compare fixed and variable orientation with traceable conditions. | I/A: same accessible task, exposure and material controls, replication plan; Systems/M5. |
| SYS-SRR-03 (SCI-002) | Define measurable geometry and process metrics with uncertainty. | A/T: declared metrics, scientific effect and adequate uncertainty; M5. |
| SYS-SRR-04 (MOT-001) | Reach position/orientation paths with six actuated joints and defined tool roll, within joint and clearance limits. | Six-axis 6R verification is pending: dimensioned CAD, full position and orientation FK/IK, continuous time-parameterised paths, singularities, collisions, hose twist and loads. Earlier kinematic results are excluded from current design evidence. |
| SYS-SRR-05 (MOT-002) | Keep mounting loads and disturbances within host allocations. | A/T: six-axis dynamics/loads, sixth-axis transport retention and host-interface comparison; M1/M4. |
| SYS-SRR-06 (EXT-001) | Supply edge and face flow with controlled transients. | A/T: measured flow/pressure response across the derived operating range; M2. |
| SYS-SRR-07 (EXT-002) | Keep material and pressure within circuit limits. | I/A/T: compatibility, maximum credible pressure and fault-retention test; M2/M4. |
| SYS-SRR-08 (UV-001) | Deliver a spectrum and exposure history compatible with the material. | A/T: irradiance map and formulation-specific gel, bond and final-cure criteria; M3. |
| SYS-SRR-09 (THM-001) | Keep temperatures and heat transfer within applicable limits. | A/T: thermal model with six drives, driver losses and motor heat; correlation and temperature/host-heat measurements; M3/M4. |
| SYS-SRR-10 (INT-001) | Retain liquids, particles and workpiece in defined operating and fault cases. | A/T: inventory-specific barrier and access verification; M4. |
| SYS-SRR-11 (INT-002) | Respect allocated mass, envelope, power, energy, heat and data. | I/A: six-axis/seven-node budgets against host ICD; M4 tracks missing items for review before PDR. |
| SYS-SRR-12 (CTL-001) | Synchronise six joint commands/readheads, full TCP pose and process sensors with timestamp origin and validity. | A/D/T: temporal-error budget, clock mapping and measured latency; M5. |
| SYS-SRR-13 (MET-001) | Resolve relevant geometric differences with documented coverage. | A/T: independent calibration checks and propagated uncertainty; M5. |
| SYS-SRR-14 (SAF-001) | Enter and maintain the reviewed physical condition for each selected fault. | A/D/T: fault-specific tests including power loss and authorised recovery; M4/M5. |
| SYS-SRR-15 (DOC-001) | Deliver a traceable SRR package and visualisation. | I: guideline/template checklist, sources, versioned models and team review; Systems. |
| SYS-SRR-16 | Detect closure and physically inhibit UV if a permissive condition is lost. | I/A/T: fault analysis and injection; PV02. M4/M5. |
| SYS-SRR-17 | Monitor chamber-to-cabin differential pressure to verify the selected MSG-type containment condition and detect invalid signals. | A/T: range, uncertainty, threshold and response to be defined; PV02/PV04. M4. |
| SYS-SRR-18 | Verify the selected seal using an isolated MSG-type pressure-hold test before operation; define safe access. | A/T: protocol, volume, temperature, sensitivity and maximum leak to be defined; PV02. M4. |
| SYS-SRR-19 | Limit UV exposure while retaining useful observation through panels. | A/T: exposure limit to be agreed; spectrum, ageing and film to panel bond; PV03. M3/M4. |
| SYS-SRR-20 | Demonstrate flow, emission retention and response to loaded filters or fan loss. | A/T: real emissions and curves; criteria to be defined; PV01/PV04. M4. |

5. Market Analysis & Costs Assessment

Customers value proposition and competition

The first target market is hosted space research: agencies, station operators, research institutions and payload integrators seeking controlled manufacturing experiments and useful process data. A second stage targets operators needing qualified tools, fixtures and selected replacement parts. The value proposition is adaptable geometry and local availability within a contained, inspectable process. Customer interviews should establish eligible parts, annual demand, waiting-time consequences, acceptance requirements and willingness to pay before projecting sales.

| Alternative | Current advantage | FORGE-UG comparison |
| --- | --- | --- |
| Earth manufacture and resupply | Established materials, inspection and broad production capability. | Assess delivery dependence and inventory against platform/feedstock cost. Local manufacture only applies to eligible parts. |
| Fixed-orientation or Cartesian space printing | Orbital process heritage and simpler motion for suitable geometries [R7,R8]. | Demonstrate whether orientation freedom gives useful access or quality benefits after accounting for added complexity. |
| Specialised orbital manufacturing | Metal printing and reported resin-printing demonstrations address related needs [R9,R12]. | Compare material, geometry, containment, metrology, host resources and service scope rather than claiming a universal replacement. |
| Ground robotic manufacturing | Established examples of orientable deposition and curved-surface processing [R2–R5]. | Space adaptation and integration evidence are the development focus; terrestrial success alone is not the product differentiation. |

The initial business model could combine development contracts, experiment integration and a paid data or manufacturing service. A mature offer could add qualified replaceable heads, consumables and maintenance. Revenue means payment for these products or services; it is not inferred from the existence of a technical demonstration. No defensible market-size or growth-rate estimate is available from the present project data. A bottom-up serviceable market should count compatible host opportunities and qualified use cases.

Long term applications and technology development

The immediate development step is a controlled robotic resin-printing experiment. A subsequent station product could manufacture suitable fixtures, tools, structural elements and selected parts for robots or rovers. A rover still needs separately supplied electronics, power, sensors and qualified assemblies. Metal heads, printed conductors or other process modules are future product options, each with its own feedstock, energy, contamination and qualification requirements. Semiconductor-chip fabrication is not established by this resin process.

Medical research illustrates why orientable deposition could matter beyond station maintenance. In 2023, Aleksandr A. Levin and colleagues reported a collaborative articulated bioprinter that deposited bioink on curved, moving wound surfaces in animal experiments [R14]. In a separate 2023 study, Thanh Nho Do, Mai Thanh Thai and colleagues at UNSW Sydney developed the flexible F3DB prototype for depositing biomaterials in confined spaces, including tests on a pig kidney surface [R13]. These are real research precedents for the proposed future direction.

An illustrative future application is a miniaturised, image-guided head following a curved wound to deposit a tissue-compatible scaffold where it is needed. Achieving that would require validated tracking, sterile and biocompatible materials, force control, biological evidence and medical-device approval. It would be a separate biomedical development programme, not a simple resin substitution. The strategic value of FORGE-UG is to develop coordinated deposition, calibration and modular integration methods that may contribute to such later programmes.

Lifecycle cost model and planning estimate

This is the six-axis hardware/initial-consumables procurement estimate in USD, using the 15 October 2026 price basis. P is published price, R a reference variant/conditional offer, F a EUR price converted at EUR 1 = USD 1.1195, and E an internal allowance without a supplier quote. The scenario includes six motor/gear/readhead/EPOS4 packages, six joint/ring assemblies, seven CAN nodes, four UV LEDs, three blowers and two cameras. Identical axis packages are provisional until torque, stiffness and life are sized per joint. Labour, services and a development reserve are not included in this hardware subtotal.

| Component | Qty | Unit USD | Line USD | Price basis |
| --- | --- | --- | --- | --- |
| B01 M1 6061 arm stock and machining | 1 | 800.00 | 800.00 | E: CAD-dependent lot; internal estimate |
| B02 M1 maxon EC 32 flat 267121 | 6 | 109.89 | 659.34 | P: 5–19 tier [P01]; catalogue unit, adaptation excluded |
| B03 M1 Harmonic Drive CSF/CSG | 6 | 1,500.00 | 9,000.00 | E: Allowance per gearbox; size/ratio to dimension |
| B04 M1 RESOLUTE readheads | 6 | 1,652.00 | 9,912.00 | R: RA26BTA052B10F price reference [P03]; rings B32 |
| B05 M1 EPOS4 Module 50/5 534130 | 6 | 371.30 | 2,227.80 | F: EUR 331.67 × 1.1195; unit rounded [P02,P12] |
| B06 M2 GE680 50 g cartridges | 2 | 200.00 | 400.00 | E: Allowance per 50 g pack; not a published price |
| B07 M2 viproHEAD 5 dispensing package | 1 | 8,000.00 | 8,000.00 | E: Head/drive allowance; supplier quotation required |
| B08 M2 Stainless-steel nozzles | 2 | 50.00 | 100.00 | E: One operating + one spare; bore to dimension |
| B09 M2 UV-protected PTFE line | 1 | 25.00 | 25.00 | E: One 0.5 m study line; connections in B36 |
| B10 M2 Kulite pressure sensor | 1 | 1,500.00 | 1,500.00 | E: Space-family allowance; range/wetted face to verify |
| B11 M3 Nichia NVSU233B 365 nm on PCB | 4 | 39.93 | 159.72 | P: Lumistrips SKU 31715 [P04]; drivers/optics B33 |
| B12 M3 Conductive plate and straps | 1 | 400.00 | 400.00 | E: Custom thermal assembly allowance |
| B13 M3 Pt100 with bench readout | 1 | 26.90 | 26.90 | R: Adafruit 3290 + MAX31865: 11.95 + 14.95 [P11] |
| B14 M3 SG01D-18 SiC photodiode | 1 | 65.75 | 65.75 | P: sglux via DigiKey [P05]; 365 nm calibration required |
| B15 M4 6061 base and frame | 1 | 600.00 | 600.00 | E: Custom stock/machining lot; separate from arm |
| B16 M4 Lexan panels and cutting | 1 | 600.00 | 600.00 | E: One enclosure lot; area/grade/thickness to dimension |
| B17 M4 Rosco R3114 sheets | 2 | 11.50 | 23.00 | P: 20 × 24 inch sheet reference [P08]; adhesive B36 |
| B18 M4 Acktar Fractal Black initial lot | 1 | 810.00 | 810.00 | R: Conditional 1–2 parts ≤250×150×60 mm [P09] |
| B19 M4 Honeywell HM, 1HM1 reference | 1 | 829.34 | 829.34 | P: DigiKey/Powell listing [P07]; mounting to verify |
| B20 M4 Piezoresistive differential sensor | 1 | 200.00 | 200.00 | E: Low-differential measurement allowance, not Kulite |
| B21 M4 Micronel U51DL-024KK-4 | 3 | 398.00 | 1,194.00 | P: Two active + one spare [P06]; isolation B36 |
| B22 M4 HEPA and carbon cartridges | 2 | 500.00 | 1,000.00 | E: One operating set + one spare; custom capacity |
| B23 M5 GR740 evaluation platform | 1 | 15,000.00 | 15,000.00 | E: Board allowance [P13]; loan availability not assumed |
| B24 M5 SAMRH71 evaluation platform | 1 | 4,500.00 | 4,500.00 | E: Board allowance; SAMRH71F20-EK quote-only [P14] |
| B25 M5 RTG4-DEV-KIT-CG-1 | 1 | 26,054.06 | 26,054.06 | P: Mouser engineering kit [P10]; not a flight-unit price |
| B26 M5 CASPEX 4 Mp camera heads | 2 | 25,000.00 | 50,000.00 | E: Two-camera study allowance; no public price [P15] |
| B27 M5 3D PLUS space SDRAM test article | 1 | 4,000.00 | 4,000.00 | E: Standalone target-memory allowance; not dev-board RAM |
| B28 M5 UT8MR2M8 MRAM test article | 1 | 2,500.00 | 2,500.00 | E: Critical-state storage; not bulk image storage |
| B29 M5 VPT SVR power assembly | 1 | 6,000.00 | 6,000.00 | E: Conversion/rail allowance; variants to dimension |
| B30 M5 CAN interface nodes | 7 | 100.00 | 700.00 | E: Six axes + supervisory node; transceiver/PCB allowance |
| B31 Mechanical joints and bearings | 6 | 250.00 | 1,500.00 | E: Joint hardware excluding motors/gears; internal estimate |
| B32 RESOLUTE rings and mounting | 6 | 250.00 | 1,500.00 | E: Ring/fixture allowance; not included in readhead price |
| B33 UV drivers and shaping optics | 1 | 800.00 | 800.00 | E: Four-channel driver/optics hardware lot |
| B34 Interlocks conditioning and adapter PCBs | 1 | 1,000.00 | 1,000.00 | E: Physical UV inhibit, sensor readout and feedback interfaces |
| B35 Camera lenses and visible illumination | 1 | 2,000.00 | 2,000.00 | E: Two-camera optical/lighting lot; no camera duplicated |
| B36 Seals valves harness anchors and connectors | 1 | 1,500.00 | 1,500.00 | E: Interfaces, opaque sleeve and containment hardware lot |
| B37 Initial spares and process consumables | 1 | 1,500.00 | 1,500.00 | E: Other initial items; excludes spares already counted |
| Procurement total Hg |  |  | 157,086.91 | P/R/F references + E allowances |

Hardware subtotal Hg = USD 157,086.91, comprising USD 41,961.91 in P/R/F references and USD 115,125.00 in E allowances. Six-axis planning estimate; unquoted services, taxes, freight, hosting and qualification are separate.

The immediate competition phase uses existing analysis/CAD access. Replace each E allowance with a dated quote and confirm R configurations and quantities. The hardware subtotal excludes labour, software licences, launch, hosting, qualification, crew services, return/disposal, import costs and unpriced interfaces; no total development or flight price is established.

Fórmula del documento: `C LC  =  C dev  +  C build  +  C qual  +  C mission  +  C ops`

Fórmula del documento: `N BE  =  F c delivered  +  c downtime  −  c local`

A lifecycle comparison includes development, build, qualification, launch and integration, operations, maintenance and disposal. In the break-even expression, F is incremental fixed cost and the denominator is the avoided delivered-part and downtime cost minus the full local cost per accepted part. If that denominator is non-positive, increasing production alone does not recover the investment. Capacity, failure rate and demand must also support the required number of accepted parts. At present this is a decision model, not a calculated return on investment.

6. Risk Assessmentv

The initial register prioritises consequences and evidence needs. High means a potential crew/host hazard or a threat to the core experiment; Medium means a material performance, schedule or business concern requiring active review. These are provisional review priorities. Likelihood is unquantified because there is no characterised integrated prototype or agreed host context; a numerical probability or residual-risk score would be unsupported. A high-consequence item is not downgraded because a probability is unknown.

| Risk and priority | Consequence | Response evidence and proposed owner |
| --- | --- | --- |
| R04/R07/R10 High — release or gas accumulation | Crew exposure, contamination or pressure hazard. | Inventory, species-specific emissions, compatible barriers and opening criteria; leak/retention tests. M2/M4 with host. |
| R01/R02/R03 High — flow UV or thermal mismatch | Rupture, blocked nozzle, excess pressure or heat. | Measured process window, optical shielding, transient response and thermal/fault tests. M1/M2/M3/M5. |
| R05/MOT-002 High — interference or mounting loads | Collision, hose damage or excessive host disturbance. | 6R swept-volume paths, finite hose/cable roll, sixth-axis and mounting loads; M1/M4 verification. |
| R08/R13 High — power loss or false safe indication | Residual flow or exposure despite a stopped controller. | Stored-energy analysis, physical retention and coordinated fault injection. M4/M5. |
| R12 High — unsupported face or final closure | Detachment, weak bonding, trapped gas or uninspectable defects. | Stage-wise deposition/cure/inspection and closure trials. M1/M2/M3/M5. |
| R11 Medium — invalid optical reconstruction | Incorrect conclusion about accuracy or surface quality. | Calibration through real windows, coverage and independent reference measurements. M5. |
| R09 High — untraceable or misapplied model | Incorrect design decisions from plausible numbers. | Versioned inputs, dimensional checks, independent recomputation and comparison with physical data. All modules. |
| R14 High — host or launch access unavailable | Orbital demonstration delayed or redesigned. | Early partner interface review; retain a ground/reduced-gravity development path. Systems/M4. |
| R15 Medium — cost schedule or supply uncertainty | Funding gap or delayed development. | Work-package estimate, quotations, critical-path review and alternative sourcing. Coordination. |
| R16 Medium — IP regulatory or market mismatch | Restricted use, integration delay or insufficient demand. | Prior-art/IP review, applicable export and host rules, customer validation before commercial claims. Coordination. |
| R17 High — optical panel degradation | UV exposure or lost observation. | Test panel, film, adhesive and cleaning; PV03. M3/M4. |
| R18 High — loaded filter or failed branch | Loss of flow or depression and release. | Curves, isolation, sensors and safe state; PV04. M4. |
| R19 High — unsuitable CPU or board | Loss of timing, data or control. | CPU and interface budgets, faults and board review; PV05/PV06. M5. |

Response to the first review

| Review observation [T3] | Progress incorporated in this SRR | Evidence needed for closure |
| --- | --- | --- |
| Expert 1: complexity and suitability of the arm | Six-axis 6R verification is pending: dimensioned CAD, full position and orientation FK/IK, continuous time-parameterised paths, singularities, collisions, hose twist and loads. Earlier kinematic results are excluded from current design evidence. | Continuous 6R validation, bodies/hoses, loads and measured comparison; document edits do not close the finding. |
| Expert 1: gases and dust not addressed | Contained reference mission, inventory and species-balance model, access/fault strategy and risk entries. | Selected material/emissions, designed barriers and verification with the host. |
| ACHIEVED Orbital Team: broaden safety and include cost impact | UV, pressure, thermal, chemical, moving-part and power-loss hazards included; safety and qualification costs separated. | Reviewed hazard assessment, applicable criteria and cost quotations. |

7. Project Management & Timeline

The project is at the SRR analytical-design stage. The current evidence includes a defined specimen and mission scenario, literature review, module proposals, reproducible calculations and a verification framework. An integrated machine CAD, characterised material process and host agreement are subsequent design work. This report follows the official SRR template [T1] and Review 2 guidelines [T2], including response to the first review, business considerations, sustainability, resilience and modularity. Final approval and the team logo remain with the team. This revision adds study decisions; technical synchronisation with the repository is pending.

| Workstream | Current repository responsibility | Review interface |
| --- | --- | --- |
| M1 Motion | Nicolas Quispe Papuico | M2/M3 for head and tubing; M4 mounting; M5 trajectories. |
| M2 Material and extrusion | Gabriel Hurtado Curi | M3 curing; M4 inventory/containment; M5 flow and timing. |
| M3 UV and thermal | Andres Zelada Solano | M2 process window; M4 heat and protection; M5 exposure. |
| M4 Chamber and integration | Shelton Yauri Huamani | All modules and host for resources, access and safety. |
| M5 Control and metrology | Isaac Oscco Tomilla | All modules for valid signals, measurement and recovery. |
| Systems and programme coordination | Eidan Ajahuana Quiroz | Requirement approval, risk ownership, budget and delivery dates. |

These are documented responsibilities and proposed review interfaces. Changes are reviewed through versioned branches and pull requests; shared interfaces require the affected modules’ review.

Where we are and what’s next

FORGE-UG is preparing the SRR after incorporating first-review feedback. Component selection, analyses, partial resource budgets and a verification plan are documented; physical validation belongs to later stages. The next milestones follow SGAC’s official agenda [D3]. The last column links each milestone to our planned work.

| Date printed in agenda* | SGAC milestone | FORGE-UG deliverable and work |
| --- | --- | --- |
| 05 Sep 2026 | MDR / Review 1 | DL1 concept and DL2 system specifications v1.0; submit one week before the review. |
| 17 Oct 2026 | SRR / Review 2 | DL1 concept design and DL2 specifications v2.0 plus DL3 3D visualisation; submit one week before review. Present requirements, feasibility and responses to R1. |
| 23 / 30 Oct 2026 | Attitude control; OBDH / telecommunications | Use the sessions to refine motion/control architecture, onboard data and interfaces. |
| 06 / 13 / 20 Nov 2026 | Power; thermal control; structures | Refine electrical distribution, thermal paths and integrated structural/CAD analyses. |
| 27 Nov 2026 | Costs, risks and AIV | Consolidate the cost basis, risk register and assembly, integration and verification plan. |
| 05 Dec 2026 | PDR / Review 3 | Submit all documents one week before review; present the integrated preliminary design and verification evidence. |
| 19 Dec 2026 | Grand Final | If selected as a finalist, present the final project, development path and value proposition. |

In the long term, our goal is to evolve this design into a ground demonstrator, validate the process and containment, and perform reduced-gravity tests. After manufacturing and qualifying a host-compatible unit, we aim to demonstrate FORGE-UG in orbit and operate it on space stations to manufacture useful parts and support experiments. The results will guide improvements in precision, autonomy, materials and interchangeable modules. This progression could support a commercial in-orbit manufacturing and research service, with maintenance and modular upgrades. Orbital demonstration and commercial operation depend on test results, funding, operator agreements, safety acceptance and a launch opportunity; neither has a committed date.

8. Verification and Development Plan

Functional comparison and measurement

The experiment compares fixed and variable nozzle orientation on tasks both configurations can access. Material batch, feed settings, deposition speed, optical history and environment are held equivalent or their differences recorded. A geometry inaccessible to one configuration is an access-capability result, not an equal-condition precision comparison. Test order will be randomised where practical, with pieces treated as replicates. The number of pieces must follow pilot variability and the minimum effect worth detecting; it is not set arbitrarily. Record tool roll in each case and keep access and optical history comparable; six axes alone do not demonstrate improved accuracy.

Fórmula del documento: `e RMS  =  Σ  δ i 2 N`

Fórmula del documento: `u c 2  = Σ  c i 2   u i 2  + 2  Σ i<j   c i   c j   u ij      U = k  u c`

The geometric metric eRMS is the root-mean-square normal distance δ from reconstructed points to the nominal geometry after a declared external registration. We also report maximum deviation, coverage, invalid data, strand diameter variation, continuity and accepted-part yield. Face thickness and internal bonding require staged or additional inspection. Combined standard uncertainty uc is formed from a sensitivity model including covariances [R18]; simple root-sum-square is appropriate only for uncorrelated contributions already propagated to the output. Expanded uncertainty U requires a stated coverage factor k and justification.

Calibration will use traceable dimensions over the relevant volume, with the actual optical windows and lighting. A separate reference or withheld artefact checks the reconstruction. Scale in metres per pixel and calibration reprojection error are diagnostic quantities, not the full geometric uncertainty. The protocol will set acceptance thresholds before comparing results, based on the scientific effect and measurement capability. This avoids defining success after seeing the measurements.

Launch vibration and environmental verification

Fórmula del documento: `M  x  + D  x  + K x = −M r  a g`

Fórmula del documento: `f 1  ≈  1 2π k m       a rms  =  0 ∞ | H a (f)| 2   S a (f) df`

The structural model uses mass matrix M, damping D, stiffness K, relative displacement x and a base-excitation influence vector r. The scalar frequency estimate f is only a first-order stiffness-to-mass relation. Random-vibration response is derived from the input acceleration spectral density Sa and transfer function Ha. Final stresses, fastener loads, displacements and modes require an actual mass/stiffness model; none is claimed from the ideal kinematic arm.

The launch analysis will use the locked transport configuration, retained material, mounting interface and provider-defined loads. The future test plan includes modal survey where appropriate, sine/random vibration and other exposures required by the carrier, with functional and leak/retention checks before and after. GEVS is a methodological reference [R16], not an automatically applicable set of qualification levels. Local operating vibration and arm-induced disturbances are assessed separately from launch survival. Thermal and radiation verification will use the selected internal location and mission duration, rather than external-vacuum conditions by default.

Verification gates and evidence

| Gate | Evidence required | Decision supported |
| --- | --- | --- |
| Analytical SRR | Reproducible geometry/flow/optical/resource calculations; literature and declared assumptions. | Proceed to detailed design within the analysed scope. |
| Ground process | Flow-pressure transients, material cure/bond tests, staged face formation and containment measurements. | Choose material and operating window; refine the models. |
| Integrated demonstrator | Continuous 6R paths, independent metrology, budgets and fault tests with traceable records. | Compare configurations and evaluate reduced-gravity readiness. |
| Host and flight qualification | Agreed interfaces, reviewed hazards, environmental qualification and verified transport/operations. | Host acceptance and readiness for delivery; not established by the present SRR. |
| Orbital demonstration | Checkout/calibration, controlled experiment and recorded performance under actual conditions. | Assess actual orbital capability and later commercial development. |

9. Physical validation and future activities

This main section records experimental work not performed in the current theoretical phase. Analysis supports proposals and sizing; future tests must close acceptance criteria before claims of safety, performance or flight suitability. No test results are fabricated and future tasks are not treated as available evidence. Module responsibilities are proposed.

| Test | Question and evidence | Scope and responsibility |
| --- | --- | --- |
| PV01 Material/process | GE680 rheology, emissions by species/mass per cycle, dose, gel, bond, shrinkage and closed faces. | Now: SDS and conditional modelling. Later: samples, emission capture and independent metrology; M2/M3. No physical result or facility is established. |
| PV02 Barrier/door | Selected MSG-type seal: HM closure, chamber/cabin Δp, isolated fans-off pressure hold, and independent UV/flow inhibit. | Now: architecture and ESA test reference defined; calculate volume/temperature sensitivity and acceptance thresholds. Later: hold/leak and fault tests; M4/M5. No completed test claimed. |
| PV03 Optics/heat | Actual Lexan/film/adhesive stack, opaque finish and Nichia assembly: 365 nm/visible transmission, ageing and temperatures. | Now: spectral/thermal models with declared inputs. Later: calibrated optical and thermal measurements; M3/M4. No safe-exposure claim. |
| PV04 Air/filters | GE680 emission retention, HEPA/carbon capacity, clean/loaded curves, bypass, failed branch and contained exchange. | Now: conditional sizing and mass balance. Later: actual cartridges, species measurements, flow and fan-loss tests; M4. No removal-efficiency claim. |
| PV05 Dynamics/control | 6R motion, tool roll and hoses, structural modes, metrology, six-axis synchronisation, faults and recovery. | Six-axis 6R verification is pending: dimensioned CAD, full position and orientation FK/IK, continuous time-parameterised paths, singularities, collisions, hose twist and loads. Earlier kinematic results are excluded from current design evidence. |
| PV06 Space acceptance | Crew/material/fire compatibility, radiation, EMC, launch loads and host interface compliance. | Now: plan, evidence gaps and interface requests. Later: funded tests and host review; Systems. Simulation does not establish flight acceptance. |

10. Conclusions

FORGE-UG has a credible experimental foundation: orientable robotic manufacturing has been demonstrated on Earth, robotic resin extrusion with UV curing has been reported, and additive manufacturing has operated in orbital microgravity. The proposed station payload connects these capabilities to the practical need for tools, selected replacement parts and adaptable local manufacturing. The literature makes the integration worth developing; the project’s analytical work provides an initial quantitative design case.

Six-axis 6R verification is pending: dimensioned CAD, full position and orientation FK/IK, continuous time-parameterised paths, singularities, collisions, hose twist and loads. Earlier kinematic results are excluded from current design evidence.

The next review must verify GE680 and face formation, complete CAD and loads, close measurement criteria and agree air, heat, data and power interfaces. The GR740 reference, transparent UV absorbing panels and three fan filtration guide the study; integrated performance is unvalidated. Section 9 separates analytical closure from future physical tests and acceptance.

References and document basis

Original references and G1/G2 commits are retained. C1 to C10 provide the cited background; D1 records the study decisions, candidates and open items transferred into this revision. Heritage is not assembly qualification. Report changes still require repository synchronisation; no repository update or new test is claimed.

[R1] [NASA 2019. Solving the Challenges of Long Duration Space Flight with 3D Printing](https://www.nasa.gov/missions/station/solving-the-challenges-of-long-duration-space-flight-with-3d-printing/)

[R2] [Velazquez L, Palardy G, Barbalata C. 2021. Design and integration of end-effector for 3D printing of novel UV-curable shape memory polymers with a collaborative robotic system. Author manuscript, LSU.](https://arxiv.org/abs/2108.10810)

[R3] [Stevens AG et al. 2016. Conformal Robotic Stereolithography. 3D Printing and Additive Manufacturing 3(4), 226–235. DOI 10.1089/3DP.2016.0042.](https://dspace.mit.edu/entities/publication/eec57523-b2e1-4f00-b644-901bfca163b9)

[R4] [Festo. 2016. 3D Cocooner. Project brochure and manufacturer description; parallel-kinematic system.](https://www.festo.com/PDF_Flip/corp/Festo_3DCocooner/en/4-5/)

[R5] [Jonckers D, Tauscher O, Thakur AR, Maywald L. 2022. Additive Manufacturing of Large Structures Using Free-Flying Satellites. Frontiers in Space Technologies 3:879542.](https://doi.org/10.3389/frspt.2022.879542)

[R6] [Kringer M, Böhrer C, Frey M, Pimpi J, Pietras M. 2022. Direct Robotic Extrusion of Photopolymers DREPP Influence of microgravity on an in-space manufacturing method. Frontiers in Space Technologies 3:899242.](https://www.frontiersin.org/articles/10.3389/frspt.2022.899242/full)

[R7] [NASA. 25 November 2014. Open for Business 3-D Printer Creates First Object in Space on International Space Station.](https://www.nasa.gov/missions/station/open-for-business-3-d-printer-creates-first-object-in-space-on-international-space-station/)

[R8] [Prater T et al. 2019 journal issue, online 2018. 3D Printing in Zero G Technology Demonstration Mission Complete Experimental Results and Summary of Related Material Modeling Efforts. DOI 10.1007/s00170-018-2827-7.](https://pmc.ncbi.nlm.nih.gov/articles/PMC7243176/)

[R9] [ESA. 6 September 2024. ESA 3D prints first metal part on the International Space Station.](https://www.esa.int/Newsroom/Press_Releases/ESA_3D_prints_first_metal_part_on_the_International_Space_Station)

[R10] [Kringer M et al. 2024. Effects of microgravity and reduced atmospheric pressure on manufacturing photopolymer specimens. Acta Astronautica 218, 314–325.](https://doi.org/10.1016/j.actaastro.2024.01.033)

[R11] [Strecker R et al. 4 August 2026. Effects of reduced gravity and reduced atmospheric pressure on in-space manufacturing of carbon-fiber-reinforced structures.](https://doi.org/10.1038/s44334-026-00104-w)

[R12] [Orbital Matter. 12 August 2026. A first in orbit 3D printing in the open vacuum of space. Manufacturer mission report.](https://www.orbitalmatter.com/newsroom-first-print)

[R13] [UNSW Sydney. 28 February 2023. 3D bioprinting inside the human body could be possible thanks to new soft robot. F3DB research prototype.](https://www.unsw.edu.au/newsroom/news/2023/02/3d-bioprinting-inside-the-human-body-could-be-possible-thanks-to)

[R14] [Levin AA et al. 2023. Commercial articulated collaborative in situ 3D bioprinter for skin wound healing. International Journal of Bioprinting 9(2):675. DOI 10.18063/ijb.v9i2.675. Animal research.](https://accscience.com/journal/IJB/9/2/10.18063/ijb.v9i2.675)

[R15] [NASA Johnson Space Center. Orbit Tutorial. ISS inclination and altitude-dependent orbital geometry.](https://eol.jsc.nasa.gov/Tools/orbitTutorial.htm)

[R16] [NASA GSFC. General Environmental Verification Standard GSFC-STD-7000. Methodological reference; applicable levels require mission review.](https://standards.nasa.gov/standard/gsfc/gsfc-std-7000)

[R17] [NASA. Quick Start Guide to Payload Design and linked ISS payload-design guide. Use host-approved current requirements for an actual mission.](https://www.nasa.gov/missions/station/quick-start-guide-to-payload-design/)

[R18] [NIST Technical Note 1297, Section 5. Combined Standard Uncertainty.](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty)

[G1] [AEGINS technical package M1–M3. Commit 97ecaa8b791a9ba015076693d992796fa5ad2276; merged via PR 6. Inputs, results, code and source-access limitations.](https://github.com/eidanYT/Aegins-Project/tree/97ecaa8b791a9ba015076693d992796fa5ad2276/models/srr_agente_tecnico)

[G2] [AEGINS integration package M4/M5. Commit c95708bcdcef988c369dc8e6fbe77a82c24c642e; integration proposal associated with PR 7, not represented as merged approval. See system, interfaces, models and evidence.](https://github.com/eidanYT/Aegins-Project/tree/c95708bcdcef988c369dc8e6fbe77a82c24c642e)

[T1] [ACHIEVED Orbital 2026. Official Report Template SRR. Maximum 30 pages; original source retained.](https://docs.google.com/document/d/1VEZzT6vw134w6CKLxHCs_u7poRDYHhSM/edit)

[T2] [ACHIEVED Orbital 2026. Review 2 Guidelines. Technical presentation 10 min and Q&A 15 min; evaluation criteria.](https://docs.google.com/document/d/12ZDWNiUHeyCW8tckpVIAnYeAPqpNIW_J/edit)

[T3] [AO2026 Evaluation Grid Review 1 AEGINS. MDR, 5 September 2026. Expert feedback and ACHIEVED Orbital Team comments.](https://drive.google.com/file/d/1fCPoGXb0Y6MstuKdieDDerOqg5v8OnwV/view)

[C1] Gaisler, GR740 product and single board computer reference design. Processor heritage and reference-board limitations are distinct. https://www.gaisler.com/products/gr740 https://www.gaisler.com/products/gr740-single-board-computer-reference-design

[C2] Gaisler, GR712RC On Board Computer; BAE Systems, Radiation hardened electronics. https://www.gaisler.com/products/gr712rc-on-board-computer https://www.baesystems.com/en/product/radiation-hardened-electronics

[C3] NASA, MSG facility development and operations, 2008; ESA, Human Spaceflight Science Newsletter 3, June 2007. Historical ventilation and leak testing. https://ntrs.nasa.gov/api/citations/20090017703/downloads/20090017703.pdf https://wsn.spaceflight.esa.int/docs/HumanSpaceflightScienceNewsletters/2007/Newsletter%203%20-%20June%202007.pdf

[C4] NASA, Life Sciences Glovebox, 2018. Two levels of containment and negative airflow. https://ntrs.nasa.gov/api/citations/20180007895/downloads/20180007895.pdf

[C5] Rosco, UV Filter R3114; Acktar, Fractal Black. Optical examples and declared heritage, not integrated payload qualification. https://emea.rosco.com/en/product/uv-filter https://acktar.com/product/fractal-black/

[C6] ESA, ISS climate change announcement annex, July 2011, Cupola description; NASA MSG utilization handbook, 2007. Window material examples. https://wsn.spaceflight.esa.int/docs/201107/Annex1-ESA-ISS-CC-AO-Climate-Change.pdf https://ntrs.nasa.gov/citations/20070013892

[C7] DELO, KATIOBOND GE680 safety data sheet, version 2.02, 22 May 2025, manufacturer document hosted by VIBA. The SDS is not an emission measurement. https://www.viba.nl/media/files/msds/vib0016280.pdf

[C8] Micronel, U51DL-024KK-4 specification; manufacturer document Rev. 02, 20 April 2021, hosted copy. Honeywell HM series. https://inelso.ru/upload/specs/U51DL.pdf https://automation.honeywell.com/gb/en/products/sensing-solutions/switches-and-controls/sealed-switches/hm-series-sealed-switch

[C9] ViscoTec, vipro HEAD 5 parabolic flight test; Frontiers, DREPP paper, 2022. Reduced gravity process evidence. https://www.viscotec.de/en/vipro-head-5-suitable-for-use-in-zero-gravity/ https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2022.899242/full

[C10] Software documentation for proposed CAD, multiphysics, robot and CPU modelling tools. https://www.solidworks.com/product/solidworks-simulation https://www.comsol.com/ https://www.mathworks.com/products/simscape-multibody.html https://www.gaisler.com/products/tsim

[D1] AEGINS. Cambios y pendientes del SRR de FORGE UG. 14 October 2026. Project decision register supplied as FORGE_UG_Cambios_y_Pendientes (1) (1).docx. Source for component alternatives and PV01 to PV06; no hardware quotations.

Pricing and component data sources

Accessed 15 October 2026 UTC. Public listings are price references, not binding offers. Every E amount is an internal assumption; cited product information does not substantiate that assumed price.

[P01] maxon EC 32 flat 267121; USD 109.89 at 5–19 units; NRND. [Source](https://www.maxongroup.us/maxon/view/product/motor/ecmotor/ecflat/ecflat32/267121)

[P02] maxon EPOS4 Module 50/5 534130; EUR 331.67 at 5–19 units. [Source](https://www.maxongroup.com/maxon/view/product/control/Positionierung/EPOS-4/534130)

[P03] E-MotionSupply; RESOLUTE RA26BTA052B10F rotary readhead; USD 1652; ring excluded. [Source](https://www.e-motionsupply.com/Renishaw_s/4331.htm)

[P04] Lumistrips; NVSU233B U365 on PCB, SKU 31715; USD 39.93. [Source](https://us.lumistrips.com/nichia-led-nvsu233b-uv-cu-pcb-10x10mm-1450mw-365nm.html)

[P05] sglux via DigiKey; SG01D-18; USD 65.75; spectral calibration at 365 nm required. [Source](https://www.digikey.com/en/products/detail/sglux-gmbh/SG01D-18/28741729)

[P06] Micronel via DigiKey; U51DL-024KK-4; USD 398; catalogue input 43 W. [Source](https://www.digikey.com/en/products/detail/micronel-usa/U51DL-024KK-4/14545086)

[P07] DigiKey/Powell; Honeywell 1HM1; USD 829.34; stock/lead time require reconfirmation. [Source](https://www.digikey.com/en/products/detail/honeywell-sensing-and-productivity-solutions/1HM1/3072634)

[P08] BarnDoor Lighting; Rosco R3114 20 × 24 inch sheet; USD 11.50. [Source](https://www.filmandvideolighting.com/rospgelsh.html)

[P09] Acktar fixed-price initial lot; USD 810; conditional part dimensions, quantity and masking. [Source](https://acktar.com/product/acktar-fixed-price-initial-lot/)

[P10] Mouser; RTG4-DEV-KIT-CG-1; USD 26054.06; development hardware. [Source](https://www.mouser.com/en/ProductDetail/Microchip-Technology/RTG4-DEV-KIT-CG-1?qs=WodfsLuQpFpb8eUdSH8h0A%3D%3D)

[P11] Adafruit 3290 Pt100 USD 11.95; linked MAX31865 readout USD 14.95; bench reference. [Source](https://www.adafruit.com/product/3290)

[P12] ECB, 14 October 2026; EUR 1 = USD 1.1195; accounting conversion only. [Source](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.ff.html)

[P13] Gaisler GR740-MINI; no public purchase price retrieved; time-limited loan is conditional; purchased boards require GRMON Professional. [Source](https://www.gaisler.com/products/gr740-mini)

[P14] Mouser SAMRH71F20-EK; non-stocked, request quotation; no price used from this page. [Source](https://www.mouser.pe/en/ProductDetail/Microchip-Technology/SAMRH71F20-EK?qs=7MVldsJ5Uaz5zVodUap1Cg%3D%3D)

[P15] 3D PLUS CASPEX 4 Mp family; no public price retrieved; E allowance is internal. [Source](https://www.3d-plus.com/products/caspex-4mpx-space-camera-heads/)

[P16] Nichia NVSU233B U365 specification STS-DA1-4890F; 1 A, typical 3.85 V and 1.45 W radiant flux at Ts = 25°C. [Source](https://led-ld.nichia.co.jp/en/product/led_product_data.html?kbn=1&type=NVSU233B+(365nm))

[P17] Microchip RTG4 development kits; prototype devices and separate Libero Platinum licence. [Source](https://www.microchip.com/en-us/development-tool/RTG4-DEV-KIT)

[J01] Harmonic CSG-14-50-2UH-LW: 0.32 kg. [Source](https://www.harmonicdrive.net/products/gear-units/gear-units/csg-2uh-lw/csg-14-50-2uh-lw)

[J02] Renishaw RESOLUTE standard datasheet, p. 10: 18 g readhead, 5 V, 1.25 W; rings/cables excluded. [Source](https://www.renishaw.com/resourcecentre/download/(6b1c98777ab2431a88f7e02cdc70d9d0)?userLanguage=en)

[J03] ViscoTec manufacturer brochure: vipro-HEAD 5 approx. 750 g; manual INST-005513/A, pp. 29–30: 24 V, 1.4 A/phase, not bus current. [Source](https://www.viscotec.de/wp-content/uploads/2024/03/broschuere-viscotec-additive-manufacturing-en-102023_web.pdf)[ Manual](https://icube-robotics.github.io/viproHEAD5_viscotec_ros2/datasheet/Vipro-HEAD3_5_manuel.pdf)

[J04] Micronel authored specification Rev. 02, pp. 2–3: 120 g, 24 V, 43 W rating; 23 W pressure shutoff / 30 W vacuum shutoff / 41 W free-air. [Source](https://inelso.ru/upload/specs/U51DL.pdf)

[J05] Gaisler GR-SBC-GR740: 5 V, <7 W and integrated 3D PLUS memory; representative SBC, not B23 evaluation-platform data. [Source](https://www.gaisler.com/products/gr-sbc-gr740)

[D2] AEGINS. Informe Técnico FORGE UG SRR Arquitectura Hardware Cronograma, v1.0, 14 October 2026, pp. 9–12. Independent analytical proposal; resource assumptions reconciled here with selected variants and two-camera cost case.

[J06] Adafruit 3290 Pt100 19.3 g; 3328 MAX31865 board 2.7 g; bench reference, 3–5 V input. [3290](https://www.adafruit.com/product/3290) [3328](https://www.adafruit.com/product/3328) [Vin](https://learn.adafruit.com/adafruit-max31865-rtd-pt100-amplifier/pinouts)

[J07] sglux SG01D-18 rev. 5.3: photovoltaic readout; reverse-voltage limit 20 V is not a required supply. [Datasheet](https://www.farnell.com/datasheets/1681849.pdf)

[J08] Honeywell 1HM1 manufacturer sheet: maximum mass 6.35 g; contact rating is not consumption. [Datasheet](https://indusautomation.co/wp-content/uploads/2023/04/Honeywell-1HM1.pdf)

[J09] Microchip SAMRH71: chip core 1.8 V, I/O 3.3 V nominal; SAMRH71F20-EK input 12 V. [Chip](https://www.microchip.com/en-us/product/samrh71) [EK AN4008](https://ww1.microchip.com/downloads/aemDocuments/documents/AERO/ApplicationNotes/ApplicationNotes/Getting_Started_with_the_SAMRH71F20_Evaluation_Kit_DS00004008A.pdf)

[J10] Microchip RTG4 supply-pin table: core 1.2 V, VPP/PLL 3.3 V; I/O and SerDes supplies depend on bank/use. [Pin datasheet](https://ww1.microchip.com/downloads/aemDocuments/documents/FPGA/ProductDocuments/PackagingSpecifications/rtg4/RTG4_FPGA_Pin_Description_Datasheet_DS0130_V7.pdf)

[J11] 3D PLUS CASPEX 4M webpage: 64 g, 5–9 V; Aug. 2026 brochure: 62 g, 4.5–9 V, 1.5 W average at 25 °C. [Web](https://www.3d-plus.com/products/caspex-4mpx-space-camera-heads/) [Brochure](https://www.3d-plus.com/app/uploads/2024/05/Brochure-Camera-systems-Digital-Version.pdf)

[J12] Frontgrade UT8MR2M8: 3.3 V nominal, operating range 3.0–3.6 V. [Datasheet](https://www.frontgrade.com/sites/default/files/documents/datasheet-ut8mr2m8.pdf)

[J13] VPT SVRTR2800S rev. 12: maximum 55 g; 18–40 V continuous input; 2805S output 5 V/30 W. [Datasheet](https://cdn.craft.cloud/8b2193af-9254-40b8-94b1-f0108baf88de/assets/products/datasheets/DS-SVRTR2800S-9860-12.pdf)

[D3] SGAC. ACHIEVED Orbital 2026 Official Agenda v1.0.

[D4] Team decision, 15 October 2026: adopt exclusively a six-axis 6R arm with full tool orientation. Six-axis kinematic and physical verification remains pending.
