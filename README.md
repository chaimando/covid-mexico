# Modelo de predicción de casos de COVID-19 en México

## Objetivo

El objetivo de este modelo matemático es de proposito meramente informativo, y no pretende ser usado como fuente de información oficial. 

Debe ser tomado como un recurso para informar a la gente sobre la velocidad con la que se ha propagado el virus y cuál podría ser el número de casos en un futuro cercano si no se acatan las medidas pertinentes.

Espero que este modelo sea tomado también como una inspiración para estudiantes de ingeniería para que generen sus propias propuestas para modelar el comportamiento de este virus.

Inspirado en el trabajo de @prestevez disponible en: https://github.com/prestevez/covid-19-mx

## Base de datos

Se descargó la base de datos de casos diarios a partir del 5 de enero hasta el 20 de abril de la página del CONACyT y se depuró para tener solo los datos a nivel nacional así como el número total de casos.

Base de datos utilizada disponible en: https://datos.covid-19.conacyt.mx/#DownZCSV

A continuación se muestra una porción de los datos:

![Base de datos](/images/base-de-datos.PNG)

### Gráfica de la base de datos:

![Datos graficados](/images/grafica-base-de-datos.PNG)

Podemos notar que la función tiene una forma entre sigmoidal y exponencial

## Modelo matématico

Se eligió una función sigmoidal/logistica de modo que el modelo resultante tendría la siguiente forma:

![Base de datos](/images/funcion.PNG)

La siguiente tarea fue el cálculo de los parametros beta_1 y beta_2. Dicha tarea se llevó a cabo utilizando las siguiente librerías.

## Librerías

### Scipy

Para el cálculo de los parámetros de la función se utilizó las librería [Scipy](https://www.scipy.org/.)

A continuación se muestra el fragmento del código para cálcular e imprimir los parámetros beta_1 y beta_2
```python
popt, pcov = curve_fit(sigmoid, xdata, ydata)
#imprimir los parámetros finales
print(" beta_1 = %f, beta_2 = %f" % (popt[0], popt[1]))
```

### Pandas y Numpy

Para tareas básicas se utilizaron [Pandas](https://pandas.pydata.org/) (librería de análisis de datos) [Numpy](https://numpy.org/) (contiene funciones matemáticas)

## Resultados y predicciones

A continuación se muestra la función calculada en una gráfica

![Resultado](/images/modelo-vs-datos.PNG)

