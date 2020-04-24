# Modelo de predicción de casos de COVID-19 en México

## Objetivo

El objetivo de este modelo matemático es de proposito meramente informativo, y no pretende ser usado como fuente de información oficial. 

Debe ser tomado como un recurso para informar a la gente sobre la velocidad con la que se ha propagado el virus y cuál podría ser el número de casos en un futuro cercano si no se acatan las medidas pertinentes.

Inspirado en el trabajo de @prestevez disponible en: https://github.com/prestevez/covid-19-mx

## Datos oficiales

Se descargó la base de datos de casos diarios a partir del 5 de enero hasta el 20 de abril y se depuró para tener solo los datos a nivel nacional así como el número total de casos.

Base de datos utilizada disponible en: https://datos.covid-19.conacyt.mx/#DownZCSV

A continuación se muestra una porción de los datos:

![Base de datos](/images/base-de-datos.PNG)

Gráfica de la base de datos:

![Datos graficados](/images/grafica-base-de-datos.PNG)

Podemos notar que la función tiene una forma entre sigmoidal y exponencial

## Modelo matématico

Se eligió una función sigmoidal/logistica de modo que el modelo resultante tendría la siguiente forma:

![Base de datos](/images/funcion.PNG)


## Resultados y predicciones

A continuación se muestra la función calculada en una gráfica

![Resultado](/images/modelo-vs-datos.PNG)

