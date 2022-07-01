#METODO DE EULER
#librerias
import numpy as np
import matplotlib.pyplot as plt
import math
def funcion(x,y):
ec=x+2*y
return ec
def solucion(x,y):
sol=.25*math.exp(2*x)-.5*x-.25
return sol
h=float(input("Tamaño de paso: "))
s=float(input("¿Hasta que valor?"))
n=(s/h)+1
x=np.zeros(n)
y=np.zeros(n)
ys=np.zeros(n)
#x[0]=1
#y[0]=.5
print(x[0],y[0])
for i in np.arange(1,n):
y[i]=y[i-1]+(funcion(x[i-1],y[i-1]))*h
x[i]=x[i-1]+h
ys[i]=solucion(x[i+1],y[i+1])
print(x[i],y[i])
plt.scatter(x,y)
plt.scatter(x,ys,color='blue')