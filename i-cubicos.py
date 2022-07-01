#INTERPOLACION CUBICA
import numpy as np
F1 =[-8, 4, -2, 1, 0, 0, 0, 0, 0, 0, 0, 0 ];
F2 =[-1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ];
F3 =[0, 0, 0, 0, -1, 1, -1, 1, 0, 0, 0, 0 ];
F4 =[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0 ];
F5 =[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ];
F6 =[0, 0, 0, 0, 0, 0, 0, 0, 27, 9, 3, 1 ];
F7 =[3, -2, 1, 0, -3, 2, -1, 0, 0, 0, 0, 0];
F8 =[0, 0, 0, 0, 3, 2, 1, 0, -3, -2, -1, 0 ];
F9 =[-6, 2, 0, 0, 6, -2, 0, 0, 0, 0, 0, 0 ];
F10 =[0, 0, 0, 0, 6, 2, 0, 0, -6, -2, 0, 0 ];
F11=[-12, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ];
F12=[0, 0, 0, 0, 0, 0, 0, 0, 18, 2, 0, 0 ]
b =[3,1,1,2,2,-1,0,0,0,0,0,0];
A=np.array([F1, F2, F3,F4,F5,F6,F7,F8,F9,F10,F11,F12])
x=np.linalg.solve(A,b)
print('Los coeficientes son ')
print(x)
val=x[8]*pow(2, 3)+x[9]*2**2+x[10]*2+x[11]
print('El valor interpolado para x=2 es ', val)