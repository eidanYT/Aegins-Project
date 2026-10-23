# Software y estrategia de simulación

## Software recomendado y criterio de elección

La elección propuesta se debe confirmar con una prueba corta de importación del mismo CAD 6R y el mismo tramo de impresión. Comparar tiempo de preparación, soporte del brazo personalizado, orientación completa, acceso a señales, automatización, exportación y licencias disponibles. Fijar versiones compatibles y dependencias reproducibles; no se incluyen precios ni licencias supuestamente disponibles.

| Necesidad | Opción propuesta | Uso y límite |
|---|---|---|
| CAD y planos | El CAD paramétrico con licencia y experiencia del equipo; FreeCAD puede evaluarse como alternativa | Mantener una fuente nativa, exportar STEP y propiedades de masa; comprobar que el exportador del robot conserva marcos, ejes y unidades. Elegir por el ensamble real, planos y tolerancias. |
| Primera simulación de impresión robótica | RoboDK más slicer/CAM y modelo personalizado | Su documentación permite G-code y eventos de extrusor. Comprobar integración del brazo propio, postprocesador y orientación 6R; no asumir que un slicer convencional resuelve trayectorias no planas ni que el visor modele resina y curado. |
| Integración abierta y fallos | ROS 2, MoveIt 2, ros2_control y Gazebo mediante gz_ros2_control | MoveIt planifica trayectorias con restricciones y colisiones; Gazebo permite integrar controladores y modelos. Añadir el modelo de dosificación, cordones y UV: no vienen validados para GE680. Empezar en PC; no presupone portabilidad directa a GR740. |
| Dinámica y control con acceso institucional | MATLAB y Simulink con Simscape Multibody y Robotics System Toolbox | Importación URDF/CAD y simulación multicuerpo/control. Requiere toolboxes/licencias y revisión de propiedades importadas; el proceso de resina necesita modelo adicional. |
| Estructuras y lanzamiento | Ansys Mechanical si hay acceso; SimScale para estudiar modalidades disponibles | Modelo estático, modal y respuesta dinámica. Confirmar solver y licencia para PSD aleatoria, excitación de base y choque. No sustituir vibración aleatoria por solo un cálculo modal o armónico. |
| Extrusión y física de material | Modelo reducido propio y calibrado; COMSOL Polymer Flow para preguntas avanzadas | COMSOL ofrece modelos de flujo no newtoniano; la superficie libre, cinética de GE680 y acoplamiento UV requieren configuración, datos y módulos adecuados. Evitar CFD completo como primer entregable. |
| Arquitectura de sistema | Eclipse Capella con Arcadia | Contexto, escenarios, funciones y arquitectura lógica/física. Enlazar IDs de requisitos y contratos de ICD; no es simulador cinemático ni FEA. |

Ruta sugerida: una prueba de RoboDK para obtener pronto una secuencia visible y comprobar el robot personalizado; ROS 2/MoveIt/Gazebo si se necesita integrar señales, control, proceso y fallos con mayor flexibilidad. Si el equipo ya domina MATLAB y tiene acceso, Simulink/Simscape puede cubrir la integración dinámica. Mantener CAD, requisitos y archivos de parámetros comunes cualquiera que sea la elección.

### Software propio e IA como última instancia

Antes de desarrollar una plataforma completa, registrar qué requisito no cubre la solución existente y si basta un complemento o adaptador. La primera versión propia debe importar CAD/URDF, planificar una trayectoria determinista restringida y reproducirla con modelos de proceso y registros. La IA se estudia después como generador de propuestas de orientación, secuencia o parámetros a partir de geometría.

La puerta de entrenamiento exige datos de simulación y/o ensayos con procedencia, límites de validez y métricas. Reservar familias de geometrías para prueba, comparar con un planificador convencional y comprobar colisiones, límites, caudal, dosis y construcción antes de aceptar una propuesta. La recuperación y ejecución física mantienen autorización humana y controles independientes. Esta línea no es condición para el PDR ni compromiso de entrenar un modelo para diciembre.

### Fuentes técnicas de las recomendaciones

- [RoboDK y eventos del extrusor](https://robodk.com/doc/en/Robot-Machining-Robot-3D-Printing-Project.html).
- [MoveIt y planificación con restricciones](https://moveit.picknik.ai/main/doc/concepts/motion_planning.html).
- [Integración Gazebo y ros2_control](https://control.ros.org/rolling/doc/gz_ros2_control/doc/index.html). Esta página corresponde a desarrollo; seleccionar una combinación estable soportada para el proyecto.
- [MathWorks e importación CAD y URDF](https://www.mathworks.com/help/sm/ref/smimport.html).
- [Ansys Mechanical](https://ansys.synopsys.com/products/structures/ansys-mechanical) y [análisis de vibraciones de SimScale](https://www.simscale.com/simulations/vibration-analysis/).
- [COMSOL Polymer Flow](https://www.comsol.com/polymer-flow-module).
- [Capella y Arcadia](https://mbse-capella.org/).
- [NASA GEVS GSFC-STD-7000B](https://standards.nasa.gov/node/791): referencia metodológica de verificación ambiental; aplicar el perfil y criterios acordados con el proveedor y host reales.


## Cómo simular la impresión con seis ejes

1. **Caso mínimo.** Línea, esquina y pista sobre una cara; después las doce aristas, la formación de caras y el cierre de la bipirámide. M1 y M2 definen soporte y secuencia con M3. Una malla cerrada de la pieza no demuestra que su fabricación sea posible.
2. **De CAD a trayectoria.** Importar la pieza y el robot dimensionado, fijar marcos, TCP y sujeción, generar curvas de deposición y orientaciones completas. Un slicer de capas planas no resuelve automáticamente el acceso no plano, las ocho caras o el giro de herramienta.
3. **Planificación 6R.** M1 y M5 resuelven IK/FK, continuidad, singularidades, límites de velocidad/aceleración/par, colisiones de robot, recinto y material ya construido, y torsión de tubos. Temporizar incluyendo aceleraciones, aproximación, reposicionamiento y pausas.
4. **Proceso sincronizado.** M2 aporta Q(t), presión, retardo y rezume; M3 aporta E(t), dosis, curado y temperatura. M5 intercambia esos datos bajo un reloj de simulación común y realimenta velocidades y estado de fallo. El dosificador es una variable de proceso adicional, no una séptima articulación del brazo.
5. **Material incremental.** Añadir cordones o volúmenes conforme a pose y caudal real estimado; registrar el material depositado para detectar colisiones y cobertura. Para pistas usar Q = ancho × espesor × velocidad y para cordón circular Q = π × diámetro² × velocidad / 4 como primeras aproximaciones; integrar dosis H = ∫E(t)dt. En v = 0, una parada exige tratar presión residual y curado, sin dividir por cero ni seguir extruyendo por defecto.
6. **Fidelidad física.** Empezar con cordones geométricos y modelos reducidos calibrables. Escalar a reología, superficie libre, unión o contracción y curado acoplado solo para preguntas concretas; una animación de cordones no predice estabilidad ni resistencia en microgravedad. Comparar gravedad terrestre, microgravedad y aceleraciones residuales dentro del alcance elegido.
7. **Demostración aceptada.** Publicar entradas, versiones, procedimiento, vídeo y registros sincronizados. Evaluar error TCP y orientación, restricciones, caudal/dosis, espesor, cobertura, volumen, tiempo y fallos. Las tolerancias se fijan y revisan antes de evaluar; declarar qué parte del proceso sigue sin validación física.

## Contratos de simulación de interfaces

El modelo intercambia tiempo monótono en segundos, secuencia, versión de esquema y configuración, marco, unidades, validez e incertidumbre. La pose usa metros y cuaternión normalizado con convención documentada; las articulaciones usan radianes. Mantener campos separados para commanded, estimated y measured. Indicar origen del reloj y transformación de tiempos; no usar hora de pared como sustituto del reloj de simulación.

ICD-001 coordina trayectoria, velocidad, Q, presión, irradiancia y estado; ICD-002 contiene marcos, límites 6R, TCP, masas, montaje y tubos; ICD-003 define adquisición, imágenes, calibración y tiempo; ICD-004 contiene potencia, calor, datos y límites del host; ICD-005 contiene permisos, fallos y recuperación. Las pruebas incluyen retraso, jitter, sensor obsoleto, dato inválido, pérdida de comunicación, puerta abierta, atasco, presión anómala, pérdida de soplador y energía.

Usar software en el lazo primero, luego procesador o hardware en el lazo cuando existan interfaces y equipos. Una red ROS de simulación no acredita por sí misma temporización ni comportamiento del CAN o del hardware de vuelo.


## Condiciones para evaluar aptitud de lanzamiento

La configuración de lanzamiento debe incluir las seis articulaciones retenidas, cabezal, cartucho, fluidos, filtros, electrónica y cableado, con la base de montaje real. Separar cargas de ensayo terrestre de la operación en microgravedad. La ecuación estructural de excitación de base es M ẍ + C ẋ + K x = −M r a_base; evaluar condiciones de contorno, contactos y amortiguamiento con sus incertidumbres.

Los criterios de evaluación son tensiones y deformaciones admisibles, resistencia de uniones y fijaciones, márgenes de fluencia/rotura/pandeo/fatiga cuando corresponda, pérdida de precarga, desplazamientos relativos, modos y respuesta de componentes sensibles. Los factores de seguridad, PSD, niveles de seno, choque, duración y ejes deben proceder del proveedor o de una hipótesis de estudio declarada. Sin esos datos, la salida es sensibilidad paramétrica, no compatibilidad de lanzamiento.

La verificación exige convergencia de malla, comprobación de masas/reacciones, sensibilidad a contactos y correlación mediante inspección modal y campaña ambiental cuando exista hardware. Planificar comprobaciones funcionales y de calibración antes y después, instrumentación, útiles y criterios de interrupción. Además de vibración se requieren revisiones de materiales, incendio, contaminación, UV, radiación, EMC y host. Ningún resultado FEA aislado acredita lanzamiento o vuelo.
