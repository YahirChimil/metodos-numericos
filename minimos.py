#MINIMOS CUADRADOS
import numpy as np
import matplotlib.pyplot as plt
#Ingreso
xi = [1, 2, 3, 4, 5, 6, 7]
yi = [0.5,2.5,2. ,4., 3.5,6, 5.5]
#PROCEDIMIENTO
xi = np.array(xi)
yi = np.array(yi)
xm = np.mean(xi)
ym = np.mean(yi)
# SALIDA
print('ymedia = ',ym)
#Grafica
plt.plot(xi,yi,'o',label='(xi,yi)')
plt.stem(xi,yi, bottom=ym)
plt.xlabel('xi')
plt.ylabel('yi')
plt.legend()
