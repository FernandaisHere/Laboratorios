![Logo UCN](images/60x60-ucn-negro.png)
# Laboratorio 02: Cálculo de frecuencia peatonal 


## 1. Introducción 

El presente laboratorio se basa en la información obtenida del proyecto BaSiGo, que fue respaldado por el Ministerio Federal de Educación e Investigación (BMBF) en el programa "Investigación para la Seguridad Civil". 
En este proyecto, se llevaron a cabo nueve carreras en las que se ajustó la cantidad de personas en un corredor y  los anchos (b_1 y b_2) de estos pasillos.

Este laboratorio hace uso de los archivos "UNI_CORR_500_01" y "UNI_CORR_500_07" obtenidos del proyecto, en donde se registrarón  las coordenadas de movimiento de los usuarios en los ejes X, Y y Z.
El enfoque se centra en identificar patrones, rutas y tendencias en cómo las multitudes se mueven en espacios limitados, un analisis fundamental para mejorar la seguridad en eventos masivos y situaciones similares. Además, se compara cómo diferentes bibliotecas afectan el uso de la unidad de procesamiento central (CPU) al ejecutar los códigos correspondientes.


### 1.1 Justificación 

Este experimento brinda una oportunidad concreta para enfrentar desafíos genuinos y complejos relacionados con la congestión en áreas restringidas y altamente transitadas.
A través del análisis de datos, se puede explorar la movilidad, comprender las dinámicas de congestión y localizar puntos críticos en sistemas, fortaleciendo así la capacidad de analizar y diseñar soluciones a partir de las herramientas proporcionadas por la ciencia de datos. Estos esfuerzos no solo optimizan la planificación de infraestructuras en ciertos espacios urbanos, sino que también tienen un impacto en la mejora de la seguridad de los peatones al identificar puntos de conflicto y patrones de movimiento.
 
Además, esta comprensión detallada de los flujos peatonales tiene una consecuencia directa en la mejora sustancial de la eficiencia de espacios públicos clave, como por ejemplo las estaciones de metro. Esta mejora se traduce en una experiencia más fluida y satisfactoria para los usuarios.


### 1.3 Objetivos 

**Objetivo General**

Analizar flujos peatonales en áreas congestionadas mediante dos métodos de obtención de matrices de calor para comprender el impacto en el rendimiento computacional al variar las librerías.

**Objetivos específicos**

1. Explorar y entender la base de datos.
2. Limpiar y extraer los datos necesarios, en este caso las coordenadas a utilizar.
3. Manipular los datos filtrados según lo solicitado (transformar de metros a pixeles).
4. Confeccionar mapas de calor para un análisis más interactivo.
5. Comparar los tiempos de procesamiento al usar diferentes librerias

## 2. Marco teórico

A continuación, se presentan una serie de herramientas, estructuras y librerías que se utilizarán a lo largo del laboratorio:

*Conda*: Se usará para la gestión de paquetes, ya sea buscar, instalar, actualizar o eliminarlos. A su vez permitirá crear y gestionar entornos virtuales que contendrá las bibliotecas necesarias para un proyecto en específico.

*Ipython*: Permitirá que la programación mediante Python se vuelva más eficiente e interactiva, utilizando diversas bibliotecas de análisis de datos.

*Visual Studio*: Es el entorno de desarrollo integrado (IDE) a usar que permitirá editar, depurar y compilar códigos para su posterior análisis.

*Numpy*: Esta librería proporciona distintas operaciones numéricas, matriciales y arreglos multidimensionales. Además, permite realizar arreglos más eficientes que las listas tradicionales de Python.

*Matplotlib*: Esta librería entrega múltiples códigos para realizar distintos tipos de gráficos, en este laboratorio se utilizara el gráfico de calor.

*Pandas*: Se utilizará la librería Pandas para la manipulación y análisis de datos.Esta herramienta permitirá transformar la información en un dataframe, lo que permitirá una mayor eficiencia en la limpieza, filtrado y transformación de datos antes de su visualización y análisis.

## 3. Materiales y métodos

Para la confección de este laboratorio se utilizará un dataset identificado como "UNI_CORR_500_01.txt" y , ambos archivos de texto contienen cinco columnas, las primeras dos corresponden a identificadores y las tres restantes son las coordenadas (X, Y y Z) las cuales serán procesadas. Estos datos (coordenadas) corresponden a datos de tipo float. Para este archivo la medida correspondiente a b_1 y b_2 es de 1,00 y 5,00 metros respectivamente.

Para lograr identificar con qué frecuencia pasan las personas por ciertos puntos del corredor se manipulo el dataset y así obtener lo necesario para generar una visualización para su posterior análisis, es importante mencionar que se generaron dos códigos, cada uno dedicado a calcular las matrices de calor a partir de los archivos "UNI_CORR_500_01.txt" y "UNI_CORR_500_07.txt". A pesar de que ambos códigos realizan la misma tarea, es importante señalar que cada cogigo lee un archivos distintos es decir archivo_1 lee el archico uni_corr_500_01 y el archivo 2 lee el archivo uni_corr_500_07. En ambos casos, el objetivo es obtener mapas de calor para visualizar la información de manera efectiva.

Se crearon dos códigos distintos, uno para cada archivo de datos, "UNI_CORR_500_01" y "UNI_CORR_500_07". A pesar de realizar la misma tarea, cada código procesa su propio archivo.

En el primer programa, se emplearon diccionarios, ciclos for y listas para extraer las coordenadas, identificar las más repetidas y convertirlas de metros a píxeles mediante cálculos de pendiente. Luego, se usó Matplotlib para generar mapas de calor.

En el segundo enfoque, se emplea la biblioteca Pandas para importar, manipular y visualizar la frecuencia de peatones en un histograma bidimensional. Los archivos de texto se leen usando pd.read_csv(), y se omiten las primeras 3 filas para formar un DataFrame. Se utiliza plt.hist2d() para generar un histograma 2D, seguido de plt.show() para mostrar el resultado.

Ambos códigos se encapsularon en funciones para medir los tiempos de procesamiento y comparar los enfoques de obtención de matrices de calor.

## 4. Resultados obtenidos

Luego de realizar, ejecutar y corroborar que el código funciona correctamente se obtienen los siguientes resultados en las métricas de rendimiento:

| Tipo de Experimento   | Tiempo de ejecucion (seg) |  Memoria utilizada (Mb) |
|-----------------------|---------------------------|-------------------------|
| Programa 1 (Archivo_1.py) | 0.806511402130127         | 120.69921875        |
| Programa 2 (Archivo_1.py)|  0.1570277214050293  |   129.77734375  |
| Programa 1 (Archivo_2.py)|  6.3635852336883545  |   120.4296875   |
| Programa 2 (Archivo_2.py)|  0.5664870738983154  |   132.65625   |

La comparación del rendimiento entre los programas 1 y 2 para la obtención de mapas de calor muestra que el programa 2, usando Pandas, es más eficiente en términos de tiempo. En el archivo 1, el programa 2 es cinco veces más rápido (0.16s vs. 0.81s), mientras que en el archivo 2, la diferencia es aún mayor (0.57s vs. 6.36s). Sin embargo, el programa 2 tiende a usar un poco más de memoria, aunque la diferencia no es significativa en la mayoría de los casos (alrededor de 130 MB frente a 120 MB). 
además es importante destacar que el archivo "UNI_CORR_500_07.txt" parece ser más exigente en términos de tiempo de ejecución para ambos programas, ya que en ambos casos el tiempo es significativamente mayor que en el archivo "UNI_CORR_500_01.txt".


<img src="images/Cmap_1.png" width="420">
<img src="images/Cmap_2.png" width="420">

## 5. Conclusiones
Durante el desarrolo de este laboratorio se destaca la eficacia de la extracción de elementos de una lista por su índice en comparación con la creación de nuevas listas utilizando ciclos for. Esta práctica se ha demostrado más rápida y práctica, evitando códigos extensos y reduciendo el tiempo de procesamiento.

Asimismo,  se destaca la utilidad y eficiencia del uso de diccionarios, pues permitieron establecer relaciones entre coordenadas y sus repeticiones sin necesidad de crear listas separadas, lo que simplifica el código y optimiza su desempeño.

Es interesante observar que, a pesar de obtener la misma gráfica final, la elección entre distintos métodos de programación tiene un impacto en la eficiencia de tiempo y memoria. La opción de utilizar funciones se resalta como ventajosa, ya que realiza cálculos necesarios sin aumentar la memoria en uso hasta que la función se llama. Este enfoque permite lograr resultados con menos impacto en la memoria tanto en el programa 1 como en el programa 2 , ahora,  utilizar módulos para encapsular estas funciones favorece aun más a generar una estructura de código más organizada y mantenible. 

En general los resultados indican que, la biblioteca Pandas presenta un mejor rendimiento en términos de tiempo de ejecución, lo cual se vuelve especialmente valioso para el análisis de conjuntos de datos más extensos y en términos de eficiencia computacional, sin embargo puede requerir de más memoria.

Se puede destacar la importancia de la semántica y sintaxis en la programación, y cómo decisiones sobre las técnicas a utilizar pueden influir en el rendimiento y recursos requeridos.






