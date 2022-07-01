#METODO DE RUNGE/KUTTA
#y = 1.0.
import numpy as np
from run_kut4 import *
from printSoln import *
from math import exp
def F(x,y):
F = np.zeros(1)
F[0] = 3.0*y[0] - 4.0*exp(-x)
return F
#inicio de la ntegracion
x = 0.0
#fin de la itegracion
xStop = 10.0
y = np.array([1.0]) # valores iniciales de {y}
h = 0.1 #numero de pie
#Frecienca de impresion
freq = 20
X,Y = integrate(F,x,y,xStop,h)
#salida de la solucion
printSoln(X,Y,freq)
