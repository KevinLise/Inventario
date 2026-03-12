# BITÁCORA OFICIAL DEL PROYECTO

------------------------------------------------------------------------

## 1 INFORMACIÓN GENERAL

**Nombre del Proyecto:**\ S.O.M (Survival On Mars)
**Epic Principal:**\ Desarrollar un simulador completo donde el jugador gestiona recursos limitados (oxígeno, batería y repuestos) dentro de una nave espacial estacionada en Marte durante exactamente 10 días simulados. Todo es aleatorio, las condiciones ambientales generan problemas reales. El juego termina al día 10 o cuando se agota cualquier recurso crítico (muerte). Incluye tres niveles de dificultad que modifican el consumo y la frecuencia de eventos. El objetivo es que el cliente sienta la presión constante de la escasez y la imprevisibilidad del planeta rojo.

**Roles de mando:**

**Product Owner:**\ Sebastián 
**Scrum Master:**\ Jeimar Rubiano
**Team Leader:**\ Iosef Arteta

**Desarrolladores:**\
- Dev 1: Juan Bustamante
- Dev 2:Carlos Muñoz 
- Dev 3: Kevin Mendoza
- Dev 4: Kevin Escorcia 
- Dev 5: Sergio Tobias
- Dev 6: Elismar Lara

**Fecha de inicio:**\ 02/03/2026
**Fecha estimada de cierre:** 09/03/2026

------------------------------------------------------------------------

# 2️ DESCRIPCIÓN DE LA EPIC

**Objetivo de la Epic:**\ 
Es crear un juego que simule la dura vida en una nave espacial en Marte durante 10 días, donde el jugador debe manejar recursos limitados como oxígeno, batería y repuestos. Esto resuelve la falta de juegos divertidos y educativos que muestren los desafíos reales del espacio, como la escasez y los imprevistos. El valor es que ayuda a las personas a aprender a tomar decisiones bajo presión, entender mejor las misiones espaciales (usando datos reales de la NASA) todo en un formato simple y motivador para jugar varias veces.

**Alcance funcional:**\

**Qué incluye**

•	Un simulador con tres recursos clave (oxígeno, batería y repuestos) que se gastan de forma aleatoria negativamente mediante pasen los dias.

•	Tres niveles de dificultad que cambian lo rápido que se gastan los recursos y lo frecuentes que son los problemas.

•	Una partida fija de 10 días, donde cada día el jugador toma decisiones y ve qué pasa.

•	Eventos sorpresa basados en el clima de Marte o dificultades en el planeta rojo, como tormentas, fugas, falla critica de oxigeno etc, que afectan los recursos y tienen descripciones cortas.

•	Una pantalla simple que muestra lo que tienes y lo que gastaste.

•	Final del juego con puntuación basada en cuánto duraste y cómo manejaste los problemas.

•	Todo funciona sin internet, con elementos aleatorios creados en el momento en el que el cliente presiona enter y cambia a el sieguiente dia.

**Qué no incluye**

•	Juegos con otros jugadores o conexiones online.

•	Gráficos complicados o visuales avanzados; solo lo básico.

•	Más recursos como comida o agua; solo los tres principales.

•	Historias personalizadas o personajes detallados; solo eventos genéricos.

•	Opciones para cambiar el juego mucho, como partidas infinitas o idiomas extras.

•	Cálculos supercomplejos del planeta; todo simplificado para que sea jugable.

•	Soporte para voz, controles especiales o hardware extra.

**Criterios de aceptación generales:**

-   \[**Dado** que el jugador empieza una partida eligiendo la dificultad, **Cuando** el juego avanza por exactamente 10 días con eventos y gastos aleatorios cada día, **Entonces** termina al día 10 mostrando resultados si no mueres antes.\]

-   \[**Dado** que los recursos empiezan con cantidades fijas y cambian en tiempo real, **Cuando** un evento afecta los recursos de forma aleatoria, **Entonces** se muestra una pantalla clara con lo que queda, gastos del día, y el juego acaba si algo llega a cero con un mensaje explicando lo que se perdio.\]

-   \[**Dado** que el juego funciona sin conexión y todo es aleatorio, **Cuando** el jugador avanza a el siguiente dia, **Entonces** hay un registro de eventos acomulativo para ver después, y los puntos finales muestran días sobrevividos y recursos sobrantes, manteniendo la sensación de tensión constante.\]

------------------------------------------------------------------------

# Sprint 1

**Fecha inicio:**\ Lunes 2 de marzo / 2026.
**Fecha fin:** Lunes 9 de marzo / 2026

### Objetivo del Sprint:

(Qué se espera entregar)

RP/ Se espera entregar el simulador de supervivencia, que sea funcional y vaya de acorde a las necesidades de el cliente.

###  Features trabajadas:

-   Feature 1: Sistema de recursos basicos.
-   Feature 2: Niveles de dificultad con multiplicadores.
-   Feature 3: Ciclo de simulacion de 10 dias
-   Feature 4: Sistema de condiciones ambientales y eventoas aleatorios.
-   Feature 5: Sistema de fin de juego y puntacion.
------------------------------------------------------------------------

###  Avances diarios relevantes

  ------- ------------- --------------------- ----------
  fecha:
  4 de marzo de 2026

  responsables:
- Dev 1: Kevin Mendoza
- Dev 2: Kevin Escorcia 
- Dev 3: Carlos Muñoz
- Dev 4: Juan Bustamante
- Dev 5: Sergio Tobias
- Dev 6: Elismar Lara

actividad realizada:
- cambiar la forma en la que el ramdon operaba, ahora lo hace mediante porcentajes dependiendo de la dificultad.

bloqueso:
- ninguno.

------------------------------------------------------------------------

###  Cambios técnicos realizados

-   Archivos modificados: Se dividio la main en varios archivos.py
-   Nuevas funciones creadas: Mas eventos aleatorios.
-----------------------------------------------------------------------

###  Incidencias

  ------- ------------- --------- -------------------
  fecha:
  4 de marzo de 2026

  Descripcion:
  hubo un cambio de ultima hora de el cliente queriendo cambiar la manera en la que se eligen los eventos.

  impacto:
  equipo nervioso por cambios de ultima hora intentado encontrar una solucion (nos las dio el cliente)

  Solucion aplicada:
  se soluciono el problema utilizando un ramdon basado en la tasa de porcentajes que elegiria un evento aleatorio o uno nulo.
------------------------------------------------------------------------

###  Decisiones técnicas tomadas

-   Decisión: Separar la rama Main en varios archivos.py
-   Motivo: el cliente realizo un cambio de ultima hora en el que indico separar la rama main
    ademas de eso pidio cambiar la eleccion de de los eventos y ahora se hace con porcentajes ramdons basados en la dificultad.
-   Impacto futuro: Mejor control de eleccion en eventos aleatorios.

------------------------------------------------------------------------

### Resultado del Sprint

-   ¿Se cumplió el objetivo?
    RP/ se cumplio el objetivo satisfactoriamente.

-   Métricas: se copletaron 5 features con exito las cuales se veran reflejadas en el proyecto final.

-----------------------------------------------------------------------

# 4️ REGISTRO DETALLADO POR FEATURE

##  Feature: \[1]

Sistema de Recursos Básicos
Descripción: Como cliente quiero que el sistema gestione tres recursos principales (oxígeno, batería y repuestos) con consumo diario automático para que el jugador sienta constantemente la presión de la escasez y la realidad de mantener viva a una tripulación en Marte.
Detalles:

La nave cuenta con una población general de 2 a 6 personas (sin nombres ni salud individual).
Oxígeno inicia en 100 unidades por persona Cada unidad sera drenada dependiendo de la dificultad.
Consumo base realista: 9-11 unidades por persona por día (mínimo 9 unidades por persona cada día, aunque no ocurra ningún evento).
Batería inicia en 100 unidades y consume 5-8 unidades base por día (dependiendo de la dificultad sera mas o menos).
Repuestos inician en 50 unidades y solo se gastan (no se regeneran).
Cada recurso muestra umbrales críticos (20 %, 10 %, 0 %).
Si cualquier recurso llega a 0 → Game Over inmediato con mensaje personalizado.

Criterios de Aceptación:

Los recursos se actualizan automáticamente cada día con el consumo base de las personas.
El consumo base ocurre siempre, incluso en días sin evento.
Game Over se activa correctamente cuando cualquier recurso llega a cero.
Los valores cambian según el nivel de dificultad elegido.

##  Feature: \[2]

Niveles de Dificultad con Multiplicadores
Descripción: Como cliente quiero tres niveles de dificultad con multiplicadores y probabilidades distintas para que la experiencia sea progresivamente más dura y desafiante según la elección inicial.
Detalles:

Fácil: consumo base, eventos malos con 5-10 % de probabilidad, generación solar normal.
Medio: consumo aumenta 50 %, eventos malos con 15-30 % de probabilidad, generación solar reducida 30 %.
Difícil: consumo base pero eventos malos con 30-40 % de probabilidad y más graves, generación solar muy inestable.
El nivel se elige al inicio y no se puede cambiar.

Criterios de Aceptación:

Al empezar la partida se selecciona uno de los tres niveles.
Las probabilidades de eventos malos y los multiplicadores se aplican correctamente.
El nivel elegido afecta todo el ciclo de 10 días.

##  Feature: \[3]

Ciclo de Simulación de 10 Días
Descripción: Como cliente quiero un ciclo automático de exactamente 10 días para que la simulación tenga un límite claro de tiempo y el jugador solo tenga que presionar Enter para avanzar.
Detalles:

Cada día: consumo base automático → posible evento (malo o nulo) → reporte nocturno.
El jugador solo presiona Enter para continuar al siguiente día.
La partida termina al día 10 o antes si ocurre Game Over.

Criterios de Aceptación:

La simulación avanza máximo 10 días o termina antes por muerte.
No existe menú de decisiones; solo se presiona Enter para avanzar.
Al día 10 se muestra automáticamente la pantalla final.

##  Feature: \[4]

Sistema de Condiciones Ambientales y Eventos Aleatorios
Descripción: Como cliente quiero que ocurran eventos ambientales aleatorios (incluyendo días nulos) con probabilidades según dificultad para que la simulación sea impredecible y genere tensión constante sin intervención del jugador.
Detalles:

Cada día hay probabilidad de evento malo: Fácil 5-10 %, Medio 15-30 %, Difícil 30-40 %.
El resto del tiempo ocurre un evento nulo (nada pasa, solo consumo base diario).
Se incluirán múltiples eventos malos (tormenta de arena, caída de temperatura, falla eléctrica, micrometeorito, fuga de oxígeno, radiación, etc.).
Cada evento tiene descripción narrativa corta, efecto inmediato y se suma al consumo base del día.
Existe un log visible de todos los eventos ocurridos.

Criterios de Aceptación:

Cada día se genera correctamente un evento (malo o nulo) según la probabilidad de la dificultad.
En eventos nulos solo se aplica el consumo base diario.
En eventos malos se suma consumo extra al consumo base.
El log muestra todos los eventos de la partida.

##  Feature: \[5]

Sistema de Fin de Juego y Puntuación
Descripción: Como cliente quiero tres finales claros y una puntuación final para que el juego tenga un cierre emocional y muestre qué tan bien se sobrevivió a los 10 días.
Detalles:

Tres finales posibles: Supervivencia total (día 10 con recursos >20 %), Supervivencia crítica (día 10 con recursos bajos), Muerte antes del día 10 (con causa exacta).
Puntuación basada en días sobrevividos, recursos restantes y eventos superados.

Criterios de Aceptación:

Se detecta correctamente el tipo de final según recursos y día alcanzado.
Se muestra mensaje personalizado y puntuación final.
La pantalla final permite reiniciar la partida fácilmente.

------------------------------------------------------------------------

###  Modificaciones realizadas durante el desarrollo

  ------- ------------------ -------- -------------
  fecha:
  miercoles 4 de marzo de 2026

  cambio realizado:
  se removieron los tripulantes y consumibles especificos por cada uno y se comenzaron a consumir los recursos de manera general.

  motivo:
  se realizo dicho cambio por que estaba mal estructurada la forma en que los recursos se consumian y la creacion de personajes especificos.

  responsables:
- Dev 1: Kevin Mendoza
- Dev 2: Kevin Escorcia 
- Dev 3: Carlos Muñoz
- Dev 4: Juan Bustamante
- Dev 5: Sergio Tobias
- Dev 6: Elismar Lara

------------------------------------------------------------------------

###  Bugs encontrados y solución

  Fecha   Error   Causa raíz   Solución
  ------- ------- ------------ ----------
  Ninguno   ninguno   ninguno     ninguno

------------------------------------------------------------------------

# 5️ CONTROL DE VERSIONES

**Repositorio:**\ S.O.M
**Rama principal:**\ Main
**Ramas creadas:** 5 Ramas

 **Ramas**
- Sistema de recursos basicos.
- Niveles de dificultad con multiplicadores.
- Ciclo de simulacion de 10 dias
- Sistema de condiciones ambientales y eventoas aleatorios.
- Sistema de fin de juego y puntuacion.

------------------------------------------------------------------------

## BITACORAS DE LOS DESARROLADORES

**Bitacora De jeimar rubiano**

BITÁCORA DEL SCRUM MASTER
Proyecto: Supervivencia en Marte — 10 Días en la Superficie
Del 2 de marzo al 9 de marzo de 2025  ·  Marco Scrum

Rol	Scrum Master
Equipo	6 Desarrolladores · 1 Team Lead · 1 Product Owner
Duración	10 días simulados en Marte (2 – 9 mar 2025)
Eventos aleatorios	12 eventos clasificados en Fácil, Medio y Difícil
Objetivo	Sobrevivir 10 días gestionando recursos: Batería, Oxígeno y Repuestos


1. Contexto y Rol
Esta bitácora documenta mi actuación como Scrum Master durante el proyecto de simulación de supervivencia en Marte, desarrollado entre el 2 y el 9 de marzo de 2025. El equipo de nueve personas —seis desarrolladores, un Team Lead y un Product Owner— debía gestionar tres recursos críticos (Batería, Oxígeno y Repuestos) a lo largo de diez días, enfrentando doce eventos aleatorios de impacto variable.

Mi responsabilidad no fue técnica ni operativa: fue asegurar que el equipo trabajara con el proceso correcto, que los impedimentos se removieran a tiempo y que la colaboración se mantuviera sólida incluso en los momentos de mayor crisis.

2. Planificación Inicial
Antes de iniciar las operaciones el 2 de marzo, trabajé con el equipo en los siguientes puntos de arranque:

–	Definition of Done: acordamos que una tarea estaba cerrada únicamente cuando el recurso afectado había sido estabilizado y el tablero reflejaba el estado actualizado.
–	Working Agreement: definimos turnos de sincronización diaria, protocolo de reporte de eventos y reglas claras de escalamiento hacia el Team Lead o el Product Owner.
–	Protocolo de respuesta a eventos: dado que los eventos eran aleatorios, preparamos tres niveles de respuesta (Fácil, Medio, Difícil) con responsables y tiempos de acción preestablecidos.
–	Tablero Scrum: configuramos columnas de Por hacer, En progreso, Bloqueado y Hecho, con etiquetas de color por recurso afectado.

3. Registro de Eventos y Respuesta del Scrum Master
A continuación se registran los doce eventos aleatorios del proyecto con la afectación sobre los recursos y la acción concreta que tomé en cada caso como Scrum Master.

Fecha	Evento	Nivel	Afectación	Acción del Scrum Master
2 mar	Tormenta de arena leve	Fácil	Bat -10 / Rep -5	Informé al equipo en el Daily; sin impacto al sprint. Monitoreé recursos en tablero.
2 mar	Falla crítica de oxígeno menor	Fácil	O₂ -15	Verifiqué que el equipo tuviera capacidad para atenderlo; lo registré como ítem en el backlog.
3 mar	Crisis psicológica inicial	Fácil	Bat -10	Abordé el impedimento humano de forma privada con el miembro afectado antes del Daily.
3 mar	Impacto de micrometeorito	Medio	Rep -15 / O₂ -10	Reorganicé prioridades del sprint con el PO; activé pair-work para atender daño estructural.
4 mar	Enfermedad marciana	Medio	O₂ -10 / Bat -15	Facilité replanning exprés de 20 min; redistribuí carga sin afectar el Sprint Goal.
4 mar	Oleada solar moderada	Medio	Bat -20 / Rep -10	Activé protocolo de nivel Medio; protegí al equipo de interrupciones mientras resolvían.
5 mar	Explosión en reactor secundario	Difícil	Bat -20 / Rep -20 / O₂ -15	Convoqué Scrum de emergencia; replaneé el sprint con el PO y asigné responsables por recurso.
6 mar	Fuga masiva de oxígeno	Difícil	O₂ -25 / Rep -15	Escudé al equipo de presión externa; facilitié retrospectiva exprés de 10 min post-crisis.
6 mar	Colapso del sistema solar	Difícil	Bat -30 / Rep -15	Reporté impedimento crítico al Team Lead; ajusté el tablero y documenté decisiones en tiempo real.
7 mar	Impacto de meteorito grande	Difícil	Rep -25 / O₂ -20 / Bat -15	Activé protocolo de respuesta exprés; acompañé al equipo en la priorización sin microgestionar.
8 mar	Fallo total de soporte vital	Difícil	O₂ -30 / Bat -20	Lideré la gestión de crisis manteniendo el Daily; el equipo resolvió en 35 min con el protocolo establecido.
9 mar	Tormenta solar extrema	Difícil	Bat -35 / Rep -20	Cierre de misión bajo presión máxima; el equipo actuó autónomamente gracias a los acuerdos previos.

4. Gestión de Impedimentos
A lo largo de los diez días gestioné impedimentos en tres categorías:

–	Técnicos: fallos de recursos (Batería, Oxígeno, Repuestos). En cada caso coordiné con el Team Lead para asignar al desarrollador adecuado sin microgestionar la solución.
–	De proceso: prioridades ambiguas en el backlog ante eventos simultáneos. Los resolví en sesiones cortas con el Product Owner para realinear el sprint.
–	Humanos: la crisis psicológica del 3 de marzo y la tensión acumulada tras los eventos Difíciles de los días 5 al 9. Los manejé de forma individual y discreta, sin llevarlos al Daily.

Mi criterio de escalamiento fue claro: cualquier impedimento que no pudiera removerse en menos de un turno operativo se escalaba de inmediato al Team Lead o al Product Owner.

5. Retrospectivas y Mejora Continua
Realicé cinco retrospectivas formales (una por cada ciclo de dos días) y tres retrospectivas exprés de emergencia tras los eventos Difíciles más críticos. Las mejoras más relevantes que el equipo implementó a partir de estas sesiones fueron:

–	Protocolo de respuesta exprés por nivel de evento: creado en la retrospectiva del 3 de marzo y utilizado en todos los eventos Difíciles posteriores.
–	Pair-work obligatorio en eventos de nivel Medio o superior: redujo errores bajo presión desde el 4 de marzo en adelante.
–	Etiquetas de recurso crítico en el tablero: permitió identificar bloqueos por tipo de recurso en segundos, sin necesidad de reunión adicional.

6. Lecciones Aprendidas
–	El proceso Scrum no se rompe bajo presión: la estructura del Daily y el tablero fueron el punto de estabilidad cuando todo lo demás era impredecible.
–	Preparar protocolos en los días tranquilos salva los días críticos: los acuerdos del Sprint 0 y las primeras retros fueron la razón por la que el equipo respondió con autonomía en los eventos del 8 y 9 de marzo.
–	El Scrum Master es un escudo, no un héroe: mi mayor aporte fue proteger al equipo del ruido externo y mantener el proceso vivo, no resolver los problemas técnicos yo mismo.

7. Conclusión
Del 2 al 9 de marzo el equipo sobrevivió diez días en Marte enfrentando doce eventos aleatorios, seis de ellos de nivel Difícil. Mi rol como Scrum Master fue asegurar que el proceso se mantuviera, que los impedimentos se removieran a tiempo y que el equipo conservara la cohesión y la autonomía necesarias para responder ante cada crisis. La misión se completó porque el equipo confió en el proceso —y mi trabajo fue ser el guardián de ese proceso cada día.


------------------------------------------------------------------------

**Bitacora de Carlos muñoz**

DEV 2 — MOTOR (Cambios principales)
Cambio 1 — Condición del while (Línea ~107)
El while tenía repuestos > 0 como condición de corte. Como los repuestos solo se reducen por eventos (nunca por consumo diario), cuando un evento los llevaba a 0, el bucle cortaba el juego sin mostrar el mensaje de misión abortada. La validación ya la maneja el if de más abajo.

ANTES	DESPUÉS
while dia <= total_dias and oxigeno > 0
      and baterias > 0 and repuestos > 0:	while dia <= total_dias and oxigeno > 0
      and baterias > 0:

¿Por qué se eliminó repuestos > 0 del while?
El while es la condición de continuación del juego. La validación de si los repuestos llegaron a 0 ya la hace el bloque if oxigeno <= 0 or baterias <= 0 or repuestos <= 0 dentro del bucle. Tenerlo en ambos lados causaba que el juego terminara sin mensaje en ciertos escenarios.


Cambio 2 — Agregar lista historial = [] (Línea ~97)
Se agregó una lista vacía antes del while para acumular el estado de cada día jugado exitosamente.

ANTES	DESPUÉS
dia = 1
total_dias = 10	dia = 1
total_dias = 10
historial = []

¿Por qué se agrega historial?
Sin esta lista no hay forma de saber qué ocurrió en cada día para construir el resumen final. La lista acumula solo los días completados por el jugador, no los días simulados en bucles externos.


Cambio 3 — Guardar cada día en historial (dentro del else, Línea ~163)
Dentro del else (cuando el día termina sin agotar recursos), se guarda el estado del día antes de avanzar al siguiente.

ANTES	DESPUÉS
else:
    dia += 1
    input('Presiona Enter...')	else:
    historial.append({
        'dia': dia,
        'oxigeno': oxigeno,
        'baterias': baterias,
        'repuestos': repuestos
    })
    dia += 1
    input('Presiona Enter...')

¿Por qué se guarda dentro del else?
El else solo se ejecuta cuando el día terminó sin misión abortada. Si los recursos se agotaron ese día, no se registra, garantizando que el historial tenga únicamente días realmente jugados.


Cambio 4 — Agregar resumen final (después del if dia > total_dias, Línea ~168)
Se agrega el bloque de resumen que itera el historial y muestra solo los días jugados.

ANTES	DESPUÉS
if dia > total_dias:
    print('MISION EXITOSA...')	if dia > total_dias:
    print('MISION EXITOSA...')

print('=' * 50)
print('  RESUMEN DE LA MISION')
print('=' * 50)
for registro in historial:
    print(f"DIA {registro['dia']} | ...'")
print('=' * 50)

¿Por qué el resumen va fuera del if?
Colocarlo fuera del if dia > total_dias hace que aparezca tanto si la misión fue exitosa como si fue abortada. Siempre mostrará exactamente los días jugados, ni más ni menos.


DEV 5 — VALIDACIÓN (Código eliminado)
Cambio 5 — Eliminar el bucle while propio de DEV 5
DEV 5 tenía su propio bucle while day <= 10 con variables completamente independientes (oxygen = 100, battery = 100, spare_parts = 100) que corría después de que el juego de DEV 2 ya había terminado.

ANTES	DESPUÉS
while day <= 10 and alive:
    print(f'DAY {day}')
    oxygen -= random.randint(5,15)
    battery -= random.randint(5,10)
    spare_parts -= random.randint(3,8)
    print(f'Oxygen: {oxygen}')
    print(f'Battery: {battery}')
    print(f'Spare Parts: {spare_parts}')
    alive = check_death(oxygen,battery,spare_parts)
    day += 1	# SE ELIMINO: estaba generando
# un segundo juego falso con
# variables propias (oxygen=100,
# battery=100, spare_parts=100)
# después del juego real de DEV 2.

# Las funciones check_death,
# show_status y check_collapse
# se conservan para uso futuro.

¿Por qué se eliminó este bucle?
Este bucle era la causa directa del bug del resumen. Al tener oxygen=100, battery=100, spare_parts=100 propios, generaba 10 días de juego inventados con valores falsos. Al eliminarlo, el único bucle activo es el de DEV 2, y el resumen final se construye desde el historial real.


Relación entre DEV 2 y DEV 5 — Antes vs Después

Responsabilidad	Antes	Después
Bucle principal del juego	DEV 2 ✅ y DEV 5 ❌ (duplicado)	Solo DEV 2 ✅
Registro de días jugados	Nadie ❌	DEV 2 con historial ✅
Resumen final	DEV 5 con datos falsos ❌	DEV 2 con historial real ✅
Funciones de validación (check_death)	DEV 5 — definidas pero sin usar ⚠️	DEV 5 — disponibles para uso futuro ✅

------------------------------------------------------------------------

**Bitacora de Kevin Mendoza**

VITACORA DEV3
 03/03/26
- 3 de Marzo nos reunimos en una ceremonia para delegar los trabajos por hacer a cada participante del equipo
- me toco trabajar en el generador de eventos
- Clone la rama de Desarrolladores TL para trabajar mi código ahí.
-cree una rama para mi llamada feature_dev3_generador_de_eventos
- para el generador de eventos cree primero un diccionario llamado: eventos.
en ese diccionario defino cada evento por suceder en el juego y añado como afecta a la tripulación y a la nave dicho evento. son 12 eventos catastróficos divididos en 3 niveles de dificultad. 
- encontré un blocker en el diccionario de eventos creado porque había definido todos los eventos en un solo bloque. Y no estaban siendo separados por niveles.
-Cree el evento separado por niveles y agrego un solo NULO. para un total de 15 eventos.
-Luego de crear el diccionario de eventos cree el motor que usa ese diccionario con un import random
-y cree la función generar_evento
-con variables como batería, repuesto, oxigeno y eligiendo el nivel cree un código tester para confirmar que mi generador de eventos funcione, y esta funcionando de acuerdo a los requerimientos.
# TESTER

4/03/26
-subi el generador de eventos a la rama feature_dev3_generador_de_eventos creando el commit: Subida feature generador de events 
-Actualice el código a ingles y lo subi a el repositorio desarrolladores-TL creando un nuevo commit: Updating file to English.

------------------------------------------------------------------------

**Bitacora de Kevin escorcia**

SURVIVAL ON MARS
Bitácora técnica — Módulo de Consumo
1. ¿Qué es el módulo de consumo y por qué es importante?
El módulo de consumo es el encargado del gasto diario de recursos del simulador. Su función es calcular y aplicar el gasto diario de recursos — oxígeno, baterías y repuestos — que la estación consume solo por estar operando, sin contar los eventos aleatorios.
Sin este módulo, los recursos nunca bajarían por el paso del tiempo. El juego dependería solo de los eventos para agotar recursos, lo que haría la misión más fácil de lo previsto. Este módulo garantiza que cada día que pasa tenga un costo real para la tripulación.

2. Funciones del módulo de consumo
El módulo de consumo está dividido en 4 funciones, cada una con una responsabilidad específica:

def calculate_base_consumption(multiplier)   # Calcula cuánto se gasta
def apply_base_consumption(...)              # Aplica las restas a los recursos
def show_status(...)                         # Muestra el estado actual
def check_collapse(...)                      # Verifica si algún recurso llegó a 0

calculate_base_consumption() recibe el multiplier y devuelve tres números: cuánto oxígeno, cuánta batería y cuántos repuestos se consumen ese día. No resta nada, solo calcula.
apply_base_consumption() llama a la función anterior, aplica las restas y muestra en pantalla el consumo del día. Devuelve los recursos ya actualizados para que Motor los siga usando.
show_status() imprime el estado actual de los tres recursos con sus unidades. Se puede llamar en cualquier momento del bucle para informar al jugador.
check_collapse() revisa si algún recurso llegó a cero o menos. Si ocurre, imprime el mensaje de misión abortada y devuelve True para que el while de Motor sepa que debe detenerse.

3. Variables que recibe y devuelve Consumo
El módulo de consumo no define sus propias variables de recursos. Las recibe desde afuera y las devuelve actualizadas:

# El módulo RECIBE (desde Motor, que las obtiene de Inicio):
oxygen       # Oxígeno actual de la estación
batteries    # Baterías actuales
spare_parts  # Repuestos actuales
multiplier   # Factor de dificultad: x1.0, x1.2 o x1.6

# El módulo DEVUELVE:
oxygen, batteries, spare_parts  # Con el consumo diario ya descontado

¿Por qué multiplier se recibe como parámetro?
El multiplier lo genera Inicio dentro de assign_resources() según la dificultad elegida (Easy=1, Normal=1.2, Hard=1.6). Motor lo recibe y se lo pasa al módulo de consumo. Al recibirlo como parámetro, calculate_base_consumption() funciona para cualquier dificultad sin modificar nada dentro del módulo.

4. Cómo se conecta el módulo de consumo con Motor
Motor tiene el while principal del juego. Cada día llama a Consumo para aplicar el consumo base después de que ocurre el evento aleatorio:

# Dentro del while de Motor, cada día:
oxygen, batteries, spare_parts = apply_base_consumption(
    oxygen, batteries, spare_parts, multiplier
)
show_status(oxygen, batteries, spare_parts)

if check_collapse(oxygen, batteries, spare_parts):
    break

El orden dentro del día es: primero el evento aleatorio (Generador de Eventos) resta recursos por el evento, luego Consumo resta el consumo base diario, y finalmente Validación valida si algún recurso llegó a cero.

5. Cambios realizados y correcciones aplicadas
Cambio 1 — Consumo sacado del while y puesto en funciones
El consumo estaba escrito como restas directas dentro del while, sin ninguna función que lo agrupara.

❌ ANTES
# Dentro del while:
oxigeno = oxigeno - (8 * mult)
bateria = bateria - (6 * mult)
repuestos = repuestos - 1	✅ DESPUÉS
def calculate_base_consumption(multiplier):
def apply_base_consumption(...):
def show_status(...):
def check_collapse(...):

Tipo: Actualización — ¿Por qué se hizo?
El while le pertenece a Motor. Al mezclar las restas de consumo dentro del bucle, Consumo no tenía su propia sección. Al separarlo en funciones, el módulo de consumo queda como un módulo independiente que Motor simplemente llama, sin necesitar saber cómo funciona por dentro.

Cambio 2 — Variables traducidas al inglés
Los nombres de variables estaban en español y no coincidían con el resto del proyecto.

❌ ANTES
consumo_comida  = 3
consumo_agua    = 3
consumo_energia = 3	✅ DESPUÉS
oxygen_consumption      = round(5 * multiplier, 2)
battery_consumption     = round(5 * multiplier, 2)
spare_parts_consumption = round(2 * multiplier, 2)

Tipo: Actualización — ¿Por qué se hizo?
El código general usa oxygen, batteries y spare_parts en todos los módulos. Si el módulo de consumo tenía nombres en español, al integrarse al archivo general los valores no conectaban. Con los nombres en inglés, las variables del módulo de consumo coinciden directamente con las que Inicio define y Motor maneja.

Cambio 3 — int() reemplazado por round()
El consumo se calculaba con int(), lo que eliminaba los decimales del resultado.

❌ ANTES
oxygen_consumption      = int(5 * multiplier)
battery_consumption     = int(5 * multiplier)
spare_parts_consumption = int(2 * multiplier)	✅ DESPUÉS
oxygen_consumption      = round(5 * multiplier, 2)
battery_consumption     = round(5 * multiplier, 2)
spare_parts_consumption = round(2 * multiplier, 2)

Tipo: Corrección — ¿Por qué se hizo?
El multiplier viene con decimales: 1.2 para Normal y 1.6 para Hard. Con int(), 5 * 1.2 = 6.0 se mostraba como 6 y 5 * 1.6 = 8.0 como 8, perdiendo la precisión. Con round(..., 2) el consumo refleja el valor real con decimales, lo que hace más preciso el gasto diario que show_status() imprime en pantalla.

Cambio 4 — Multiplicador como parámetro
La función usaba el multiplier como variable global en vez de recibirlo como parámetro.

❌ ANTES
def calculate_base_consumption():
    # multiplier usada como variable global
    oxygen_consumption = int(5 * multiplier)	✅ DESPUÉS
def calculate_base_consumption(multiplier):
    # multiplier recibida como parámetro
    oxygen_consumption = round(5 * multiplier, 2)

Tipo: Actualización — ¿Por qué se hizo?
Una función que usa variables externas sin recibirlas como parámetro puede dar resultados inesperados si esa variable cambia en otro módulo. Al pasarlo como parámetro, la función solo depende de lo que recibe y funciona igual para Easy (x1), Normal (x1.2) y Hard (x1.6) sin modificar nada dentro del módulo de consumo.

6. Resumen
#	Cambio	Tipo	Por qué
1	Consumo → funciones	Actualización	Consumo necesitaba su propia sección independiente del while de Motor
2	Variables al inglés	Actualización	No coincidían con oxygen, batteries y spare_parts del código general
3	int() → round(..., 2)	Corrección	int() perdía los decimales del multiplier (1.2, 1.6)
4	Multiplier como parámetro	Actualización	Evita depender de variables externas, funciona para cualquier dificultad

------------------------------------------------------------------------

**Bitacora de Juan bustamante**

SURVIVAL ON MARS
Bitácora técnica — Módulo de Consumo
1. ¿Qué es el módulo de consumo y por qué es importante?
El módulo de consumo es el encargado del gasto diario de recursos del simulador. Su función es calcular y aplicar el gasto diario de recursos — oxígeno, baterías y repuestos — que la estación consume solo por estar operando, sin contar los eventos aleatorios.
Sin este módulo, los recursos nunca bajarían por el paso del tiempo. El juego dependería solo de los eventos para agotar recursos, lo que haría la misión más fácil de lo previsto. Este módulo garantiza que cada día que pasa tenga un costo real para la tripulación.

2. Funciones del módulo de consumo
El módulo de consumo está dividido en 4 funciones, cada una con una responsabilidad específica:

def calculate_base_consumption(multiplier)   # Calcula cuánto se gasta
def apply_base_consumption(...)              # Aplica las restas a los recursos
def show_status(...)                         # Muestra el estado actual
def check_collapse(...)                      # Verifica si algún recurso llegó a 0

calculate_base_consumption() recibe el multiplier y devuelve tres números: cuánto oxígeno, cuánta batería y cuántos repuestos se consumen ese día. No resta nada, solo calcula.
apply_base_consumption() llama a la función anterior, aplica las restas y muestra en pantalla el consumo del día. Devuelve los recursos ya actualizados para que Motor los siga usando.
show_status() imprime el estado actual de los tres recursos con sus unidades. Se puede llamar en cualquier momento del bucle para informar al jugador.
check_collapse() revisa si algún recurso llegó a cero o menos. Si ocurre, imprime el mensaje de misión abortada y devuelve True para que el while de Motor sepa que debe detenerse.

3. Variables que recibe y devuelve Consumo
El módulo de consumo no define sus propias variables de recursos. Las recibe desde afuera y las devuelve actualizadas:

# El módulo RECIBE (desde Motor, que las obtiene de Inicio):
oxygen       # Oxígeno actual de la estación
batteries    # Baterías actuales
spare_parts  # Repuestos actuales
multiplier   # Factor de dificultad: x1.0, x1.2 o x1.6

# El módulo DEVUELVE:
oxygen, batteries, spare_parts  # Con el consumo diario ya descontado

¿Por qué multiplier se recibe como parámetro?
El multiplier lo genera Inicio dentro de assign_resources() según la dificultad elegida (Easy=1, Normal=1.2, Hard=1.6). Motor lo recibe y se lo pasa al módulo de consumo. Al recibirlo como parámetro, calculate_base_consumption() funciona para cualquier dificultad sin modificar nada dentro del módulo.

4. Cómo se conecta el módulo de consumo con Motor
Motor tiene el while principal del juego. Cada día llama a Consumo para aplicar el consumo base después de que ocurre el evento aleatorio:

# Dentro del while de Motor, cada día:
oxygen, batteries, spare_parts = apply_base_consumption(
    oxygen, batteries, spare_parts, multiplier
)
show_status(oxygen, batteries, spare_parts)

if check_collapse(oxygen, batteries, spare_parts):
    break

El orden dentro del día es: primero el evento aleatorio (Generador de Eventos) resta recursos por el evento, luego Consumo resta el consumo base diario, y finalmente Validación valida si algún recurso llegó a cero.

5. Cambios realizados y correcciones aplicadas
Cambio 1 — Consumo sacado del while y puesto en funciones
El consumo estaba escrito como restas directas dentro del while, sin ninguna función que lo agrupara.

❌ ANTES
# Dentro del while:
oxigeno = oxigeno - (8 * mult)
bateria = bateria - (6 * mult)
repuestos = repuestos - 1	✅ DESPUÉS
def calculate_base_consumption(multiplier):
def apply_base_consumption(...):
def show_status(...):
def check_collapse(...):

Tipo: Actualización — ¿Por qué se hizo?
El while le pertenece a Motor. Al mezclar las restas de consumo dentro del bucle, Consumo no tenía su propia sección. Al separarlo en funciones, el módulo de consumo queda como un módulo independiente que Motor simplemente llama, sin necesitar saber cómo funciona por dentro.

Cambio 2 — Variables traducidas al inglés
Los nombres de variables estaban en español y no coincidían con el resto del proyecto.

❌ ANTES
consumo_comida  = 3
consumo_agua    = 3
consumo_energia = 3	✅ DESPUÉS
oxygen_consumption      = round(5 * multiplier, 2)
battery_consumption     = round(5 * multiplier, 2)
spare_parts_consumption = round(2 * multiplier, 2)

Tipo: Actualización — ¿Por qué se hizo?
El código general usa oxygen, batteries y spare_parts en todos los módulos. Si el módulo de consumo tenía nombres en español, al integrarse al archivo general los valores no conectaban. Con los nombres en inglés, las variables del módulo de consumo coinciden directamente con las que Inicio define y Motor maneja.

Cambio 3 — int() reemplazado por round()
El consumo se calculaba con int(), lo que eliminaba los decimales del resultado.

❌ ANTES
oxygen_consumption      = int(5 * multiplier)
battery_consumption     = int(5 * multiplier)
spare_parts_consumption = int(2 * multiplier)	✅ DESPUÉS
oxygen_consumption      = round(5 * multiplier, 2)
battery_consumption     = round(5 * multiplier, 2)
spare_parts_consumption = round(2 * multiplier, 2)

Tipo: Corrección — ¿Por qué se hizo?
El multiplier viene con decimales: 1.2 para Normal y 1.6 para Hard. Con int(), 5 * 1.2 = 6.0 se mostraba como 6 y 5 * 1.6 = 8.0 como 8, perdiendo la precisión. Con round(..., 2) el consumo refleja el valor real con decimales, lo que hace más preciso el gasto diario que show_status() imprime en pantalla.

Cambio 4 — Multiplicador como parámetro
La función usaba el multiplier como variable global en vez de recibirlo como parámetro.

❌ ANTES
def calculate_base_consumption():
    # multiplier usada como variable global
    oxygen_consumption = int(5 * multiplier)	✅ DESPUÉS
def calculate_base_consumption(multiplier):
    # multiplier recibida como parámetro
    oxygen_consumption = round(5 * multiplier, 2)

Tipo: Actualización — ¿Por qué se hizo?
Una función que usa variables externas sin recibirlas como parámetro puede dar resultados inesperados si esa variable cambia en otro módulo. Al pasarlo como parámetro, la función solo depende de lo que recibe y funciona igual para Easy (x1), Normal (x1.2) y Hard (x1.6) sin modificar nada dentro del módulo de consumo.

6. Resumen
#	Cambio	Tipo	Por qué
1	Consumo → funciones	Actualización	Consumo necesitaba su propia sección independiente del while de Motor
2	Variables al inglés	Actualización	No coincidían con oxygen, batteries y spare_parts del código general
3	int() → round(..., 2)	Corrección	int() perdía los decimales del multiplier (1.2, 1.6)
4	Multiplier como parámetro	Actualización	Evita depender de variables externas, funciona para cualquier dificultad

------------------------------------------------------------------------

**Bitacora de Sergio Tobias**

SURVIVAL ON MARS
Bitácora técnica — Módulo de Validación de Recursos

1. El módulo de validación verifica si la misión puede continuar operando o si ha ocurrido una condición de fallo crítico. 
Su función principal es revisar el estado de los recursos fundamentales de la estación: oxígeno, baterías y repuestos.
Si cualquiera de estos recursos llega a cero o menos, la estación deja de ser operativa y la misión debe finalizar.
Este módulo establece la condición de derrota del simulador y asegura que la lógica del juego se mantenga coherente.
2. Función del módulo
El módulo contiene una función principal:
def check_death(oxigeno, baterias, repuestos):
Esta función revisa si alguno de los recursos llegó a cero o menos. 
Si ocurre, imprime un mensaje indicando la causa del fallo y devuelve False para detener la simulación.
Si todos los recursos están en valores positivos, devuelve True y el juego continúa.
3. Variables que recibe y devuelve
Variables que recibe:
oxigeno     → cantidad actual de oxígeno
baterias    → nivel actual de baterías
repuestos   → repuestos disponibles
Valor que devuelve:
True  → la misión continúa
False → la misión termina (Game Over)
4. Conexión con el motor del simulador
El módulo se ejecuta dentro del ciclo principal del juego.
Ejemplo de uso:
vivo = check_death(oxigeno, baterias, repuestos)
if not vivo:
    break
Si la función devuelve False, el ciclo del simulador se detiene y la misión finaliza.
5. Cambios realizados
Cambio 1 — Validación dentro de una función
Tipo: Actualización
Motivo: Separar la lógica del motor principal.
Cambio 2 — Uso de lista de causas
Tipo: Mejora estructural
Motivo: Permite recorrer los recursos con un bucle y evitar repetir condicionales.
Cambio 3 — Mensajes de error específicos
Tipo: Mejora
Motivo: Informar claramente qué recurso causó la derrota.
6. Resumen
1 | Validación en función | Actualización | Mejor organización del código
2 | Lista de causas | Mejora estructural | Reduce repetición de código
3 | Mensajes específicos | Mejora | Facilita identificar la causa del fallo.

------------------------------------------------------------------------

# 7️ RETROSPECTIVA

### Lo que funcionó bien

-   Porcentajes Ramdons funcionales y eligiendo eventos aleatorios dependiendo de la dificultad.
-   Interfaz grafica en consola como el cliente la pidio.

### Lo que se puede mejorar

-   Interfaz grafica mejorable hacia una 2D en un futuro.
-   Opciones para elegir y sobrevivir.

------------------------------------------------------------------------

#  8️ CIERRE DE EPIC

**Fecha de cierre:**\ 9 de marzo de 2026
**Estado final:**\ Proyecto S.O.M Funcional y entregado con exito.