## Pandas - DataFrames

En esta carpeta van a encontrar algunos ejemplos prácticos sobre algunas pequeñas cosas
que son posibles con la librería Pandas. Sepan que esta librería es increiblemente extensa
y hay muchisimas opciones/tutoriales/ejemplos dando vueltas.

**No** se queden con que lo que ven acá es lo único posible, o la única forma de lograr los
objetivos que se plantean.


 - [braindiseases.ipynb](braindiseases.ipynb)

 En este archivo tomamos una base de datos que extragimos de [DisGeNET](https://www.disgenet.org/) sobre asociaciones de Genes-Enfermedades.
 En particular tomamos algunas sobre enfermedades del cerebro, les dejamos el dataset en este archivo: [braindiseases_data.csv](braindiseases_data.csv).
 La intención de este archivo es mostrarles algunas cosas super básicas que cualquiera haría con una base de datos de este estilo, con una metodología mas explorativa.
 Es decir, sin tener un objetivo claro en cada momento.
 Solamente tratando de aprender cómo hacerle preguntas al dataset y que este responda.

 - [inscripcion_al_curso.ipynb](inscripcion_al_curso.ipynb)

 Este archivo es aun mas bajado a tierra.
 Tomamos un [set](inscripcion_data.csv) de respuestas del formulario de inscripción de algún curso previo de este mismo taller (no se preocupen: le quitamos la información personal).

 Acá hacemos una limpieza de los datos para que sean más fáciles de trabajar en el código.
 Hacemos algún que otro gráfico con los datos obtenidos.
 Y luego les mostramos una forma cavernicola para encontrar cuánta gente inscripta hubo en cada turno, y el solapamiento de inscriptes si se anotaron a mas de un horario.
