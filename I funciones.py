import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
def f(x):
return x**2
def g(x):
return x**(1/2)
x = sy.Symbol("x")
print(sy.integrate(f(x)-g(x), (x, 0, 2)))
yprime = y.diff(x)
print(yprime)