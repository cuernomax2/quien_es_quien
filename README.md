### Quién es quién
=============================
Mateo Manuel González Ulla - IES de Teis - 06/2024

## Reglas del juego

La lógica del juego es la esperada, salvo porque en las instrucciones del juego vintage se indica que la primera pregunta no puede ser "es hombre" o "es mujer" (consecuencia de la cultura de los 80).

Extrae de la imagen proporcionada (versión vintage del juego) las características de los personajes, de la manera más realista posible, sin inventar ninguno de los rasgos. Respeta los nombres de los personajes.

![Quien es quien - azul](./doc/Quien-es-quien.jpg)

### 1. Optimización vs Búsquedas

El juego del "quién es quién" puede considerarse un problema de optimización porque implica la búsqueda de una solución óptima en el menor número de pasos posible y no se tiene en cuenta el camino tomado hasta dicha solución. En este contexto, el objetivo es identificar al personaje correcto mediante la formulación de preguntas estratégicas que maximicen la información obtenida y minimicen el número de preguntas necesarias.

### 2. Entorno del agente

Entorno de tareas | Completamente / parcialmente Observable| Agentes | Determinista / Estocástico | Episódico / Secuencial | Estático / Dinámico | Discreto / Continuo
:---: | :---: | :---: | :---: | :---: | :---: | :---: |
 Quién es quién | Parcialmente observable | Multiagente | Determinista | Secuencial | Estático | Episódico |

Parcialmente observable: Al inicio del juego, el personaje que se debe adivinar es una carta que nuestro oponente elige al azar. Así, a medida que avanza el juego, solo podemos ver los personajes que descartamos y los que nos quedan como opciones posibles en nuestro tablero. No podemos ver las características del personaje objetivo ni el tablero del adversario para saber sus opciones restantes.

Multiagente: Durante la partida, es necesaria la interacción con otro jugador, quien formula y responde preguntas para avanzar en la búsqueda del personaje que intentamos adivinar.

Determinista: Aunque puede parecer aleatorio porque el personaje se elige al azar al comienzo del juego, el proceso es determinista. Las preguntas realizadas durante el juego tienen respuestas fijas de "sí" o "no", sin aleatoriedad.

Secuencial: Es un proceso secuencial porque la respuesta de cada pregunta influye en las siguientes. Dependiendo de si la respuesta es "sí" o "no", se eliminan o se mantienen ciertos personajes con diferentes características, lo que afecta la próxima pregunta.

Estático: El entorno del juego es estático, ya que durante las preguntas, el entorno, el tablero y el personaje objetivo no cambian.

Discreto: Es un agente discreto debido a que tiene un número finito de estados. Al seleccionar el personaje, se elige de una baraja con un número limitado de personajes. Además, el número de preguntas también es limitado, dependiendo de las características de los personajes, y las respuestas solo pueden ser "sí" o "no".

### 3. Algoritmo.

He observado la cantidad de características que se repiten entre los diferentes personajes y la conclusión a la que he llegado es que había varias que aparecían con más freciencia que otras. He hecho un conteo de todas las características y he decidido que la forma más óptima de adivinar un personaje es haciendo preguntas que descarten un total de personajes de aproximadamente la mitad

### 4. Programación lógica

El problema del "quién es quién" se presta bien para ser resuelto usando el paradigma de programación lógica debido a la naturaleza declarativa y basada en reglas de este enfoque. La programación lógica (la cual se utiliza en Prolog) permite definir hechos y reglas que describen las relaciones y propiedades de los personajes en el juego. Este paradigma facilita la representación de conocimientos y la realización de inferencias lógicas necesarias para identificar personajes basándose en preguntas y respuestas, lo cual es ideal para este tipo de problema deductivo.

### 5. Base de datos Prolog

He utilizado un archivo en prolog (main.pl). Cada una de las entradas de dicha base de datos (personaje()) está formada por el nombre del personaje y una lista de las características por las cuáles podemos definir y diferenciar al mismo de los demás personajes del tablero. Ningún personaje utiliza nombres repetidos & características completamente iguales, por lo que no es necesario definir reglas o claves.

### 6. Instalación

```
https://github.com/yuce/pyswip
```

Tras haber instalado la última versión disponible de pyswip simplemente situarse en la carpeta "src" y utilizar el comando:

```
python main.py
```

## Bibliografía

Bratko, I. _Prolog, programming for Artificial Intelligence_. Addison-Wesley/Pearson, 2012.

Hurbans, Rishal. _grokking Artificial Intelligence Algorithms_. Manning Publications Co, 2020. 

Lutz, Mark. _Learning Python_. Sebastopol, Ca, O’reilly, 2018.

Martin, Robert C. _Clean Code a Handbook of Agile Software Craftmanship_. Upper Saddle River [Etc.] Prentice Hall, 2010.

Martin, Robert C. _Clean Architecture: A Craftsman’s Guide to Software Structure and Design_. Prentice Hall, 2018.

S. McConnel. _Code Complete: A Practical Handbook of Software Construction_, 2dn Edition. Microsoft Press, 2004.

Sharan, Kishori. _Beginning Java 8 Fundamentals: Language Syntax, Arrays, Data Types, Objects, and Regular Expressions_. Apress, 2014.

Russell, Peter. _ARTIFICIAL INTELLIGENCE : A Modern Approach_, Global Edition. S.L., Pearson Education Limited, 2021.

@dfleta. "Prolog for IA". _github_, 28 de febrero de 2024. https://github.com/dfleta/prolog-for-IA

@dfleta. "API REST con Flask y Mongo Atlas". _github_, 29 de marzo de 2022. https://github.com/dfleta/ollivanders

@yuce. Latest pyswip prolog version. https://github.com/yuce/pyswip
