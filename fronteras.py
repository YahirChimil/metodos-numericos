import numpy as np
n=input("Digite en numero de puntos interiores ")
n=int(n)
x0=0
xf=20
y0=1
yf=10
h=(xf-x0)/(n+1)
x=np.linspace(x0,xf,n+2)
b=np.zeros(n)
A=np.eye(n)*(h**2-8)
for k in range(0,n-1):
A[k][k+1]=-h+4
A[k+1][k]=h+4
b[k]=-h**2*x[k+1]
b[0]=-h**2*x[1]-9*y0
b[n-1]=-h**2*x[n]+yf
y=np.linalg.inv(A).dot
y=np.insert(y,0,y0)
y=np.insert(y,len(y),yf)
for k in range(len(y)):
print("y(",round(x[k],4),")",y[k])