import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from scipy.optimize import curve_fit

# datos a partir del 5 de enero
df = pd.read_csv("covid-mexico-20-abril-subido.csv")
df.head(10)

plt.figure(figsize=(8,5))
x_data, y_data = (df["fecha"].values, df["acumulado"].values)
plt.plot(x_data, y_data, 'ro')
plt.ylabel('fecha')
plt.xlabel('casos')
plt.show()

def sigmoid(x, Beta_1, Beta_2):
     y = 1 / (1 + np.exp(-Beta_1*(x-Beta_2)))
     return y

# Normalicemos nuestros datos
xdata =x_data/max(x_data)
ydata =y_data/max(y_data)

popt, pcov = curve_fit(sigmoid, xdata, ydata)
#imprimir los parámetros finales
print(" beta_1 = %f, beta_2 = %f" % (popt[0], popt[1]))

x = np.linspace(0, 107, 108)
x = x/max(x)
plt.figure(figsize=(8,5))
y = sigmoid(x, *popt)
plt.plot(xdata, ydata, 'ro', label='data')
plt.plot(x,y, linewidth=3.0, label='fit')
plt.legend(loc='best')
plt.ylabel('fecha')
plt.xlabel('casos')
plt.show()