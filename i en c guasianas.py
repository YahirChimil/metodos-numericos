#INTEGRADOR EN CUADRANTES GAUSSIANAS
# modelo con varios tramos entre [a,b]
import numpy as np
import matplotlib.pyplot as plt
# cuadratura de Gauss
def integraCuadGauss2p(funcionx,a,b):
x0 = -1/np.sqrt(3)
x1 = -x0
xa = (b+a)/2 + (b-a)/2*(x0)
xb = (b+a)/2 + (b-a)/2*(x1)
area = ((b-a)/2)*(funcionx(xa) + funcionx(xb))
return(area)
#datos de ingreso
fx = lambda x: np.sqrt(x)*np.sin(x)
# intervalo de integración
a = 1
b = 3
tramos = 4
# procedimiento
muestras = tramos+1
xi = np.linspace(a,b,muestras)
area = 0
for i in range(0,muestras-1,1):
deltaA = integraCuadGauss2p(fx,xi[i],xi[i+1])
area = area + deltaA
#salida
print("Integral: ")
print(area)
