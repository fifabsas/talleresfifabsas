#Taller de LaTeX FIFA Bs As

## Programas básicos

### Compilador
Este es el programa que traduce los comandos del archivo tex
* [MikTeX](http://miktex.org/download) (Para Windows, bajar versión recomendada). Este compilador agrega los paquetes que se necesitan on-fly, por lo que no es necesario hacer nada más
* [TeXLive](https://www.tug.org/texlive/) (Para Linux). Para Ubuntu/Debian se debe usar el siguiente comando en consola:
```sudo apt-get install texlive-full```. Si no funciona, en Ubuntu, se deben agregar los repositorios Universe.

Con lo anterior se instala la mayoría de los paquetes, pero en caso de necesitar uno muy especial se debe buscar en CTAN e instalarlo como dice [aqui](http://en.wikibooks.org/wiki/LaTeX/Installing_Extra_Packages).

### Editores/IDEs de TeX
Estos programas son editores de texto con ventajas para la escritura de LaTeX o TeX, como autocompletado, búsqueda de referencias, marcado de sintaxis, generación de tablas. 
- [TeXMaker](http://www.xm1math.net/texmaker/download.html)
- [ShareLatex](http://www.sharelatex.com)  
 
Después cada uno elige el que le gusta más para trabajar.

### Visores de archivo .pdf
El archivo generado por el compilador en general corresponde a un archivo .pdf, para el cual necesitas un programa para leerlo. Para Windows tenemos el Adobe Reader (el programa oficial) y el [Sumatra PDF](http://blog.kowalczyk.info/software/sumatrapdf/download-free-pdf-viewer.html), que es libre y además permite leer archivos .djvu. En Linux uno de los mejores visores es el Evince, que también permite leer .djvu (y otros más).


## Recursos

En esta sección vamos a ir subiendo algunas páginas web y algunos programas simples que mejoran de forma 
substancial la escritura en este espléndido (pero complicado) lenguaje:

* Existen muchos tutoriales en internet, pero el de WikiBooks sigue siendo uno de los más útiles e importantes. Años despuése de usar LaTeX de forma continua y sigue siendo indispensable WikiBooks

* Después de estar un rato escribiendo matemática en LaTeX llegas a aprenderte muchos símbolos usuales, pero siempré está ese complicado que no te vas a acordar nunca. Es más, a veces ni sabés como se llama el símbolo en la vida real. Para esos cosas, y mucho más, existe [Detexify](http://detexify.kirelabs.org/classify.html). Ahí podés dibujar los simbolos sobre el sector indicado y la misma página web  busca en el archivo [symbols-a4.pdf](http://www.ctan.org/tex-archive/info/symbols/comprehensive/) (que es la referencia de TODOS los símbolos aceptados como tal) y presenta varias opciones posibles a lo que ingresaste. Muy útil.

* En línea con la página buscadora de símbolos, tenemos varias servicios generadores de ecuaciones. Existe un [editor online de ecuaciones](http://www.codecogs.com/latex/eqneditor.php), que nos permite guardar la ecuación compilada como imagen en varios formatos (por ejemplo .png o en formato vectorial .svg para agrandarla todo lo que uno quiera). También existe un servicio, mathurl, que crea direcciones web cortas (como bit.ly o goo.gl) para una ecuación escrita ahí mismo, para no necesitar pasando imágenes para pasar las fórmulas que tanto tiempo tardaste en deducir y escribir.

* Como ya deben haber visto y sufrido, hacer tablas en LaTeX es sin dudas unas de sus grandes falencias. Existen varias opciones para salvarnos el día, entre ellas: 

   - Un [editor online de tablas](http://truben.no/latex/table/), que nos permite hacer tablas simples (sin filas o columnas unidas) con la alineación, el texto a pie de tabla, el nombre para referenciarlo y algunas otras opciones más. También nos permite editar tablas ya hechas, importando el bloque ya escrito; nuevamente sólo reconoce tablas simples.
   - También hicimos un programa hecho en Python que permite transformar muchos archivos .csv (que se pueden hacer en programas como Excel) en un archivo .tex con las tabla dentro. El programa requiere que los archivos se llamen lista_NOMBRE.csv y los tranforma en lista_NOMBRE.tex. El script, con su documentación, lo van a encontrar en este [link](http://pastebin.com/FEHbfiLj), y cuando lo bajan observen que el archivo es un .txt, que debe ser cambiado a .py para ser ejecutado en Python.

* Además de permitirnos crear documentos con impecable calidad, LaTeX nos permite generar gráficos con le paquete TikZ. No es un lenguaje fácil de manejar, comparativamente con un editor de imagenes como el Photoshop o el muy querido Paint, pero permite generar de forma sistemática y consistente esquemas y gráficos para nuestros informes. Además existe una cantidad infinta de ejemplos en [Texample](http://www.texample.net/tikz/), para ir agarrandole el gusto.
