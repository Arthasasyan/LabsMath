
import matplotlib.pyplot as plt
import numpy
from math import *

def f(x):
    return 3 - 0.5*sqrt(x) - exp(-0.5*x*x)

def f_der(x):
    return exp(-0.5*x*x)*x-0.25/sqrt(x)

def draw(foo):
    X = range(0,100)
    Y=[foo(x) for x in X]
    plt.scatter(X,Y)
    plt.show()

def newtone(foo, foo_der, start, eps):
    x, x_prev, i = start, start + 2*eps, 0
    while abs(x-x_prev)>=eps:
        x_prev=x
        x=x-foo(x)/foo_der(x)
        i=i+1
    print(i)
    return x

def secant(foo, start, eps):
    x, x_prev, x_next,i = start, start+2*eps , start,0
    while abs(x-x_prev)>=eps:
        x_next= x_prev-foo(x_prev)/(foo(x)-foo(x_prev))*(x-x_prev)
        x_prev=x
        x=x_next
        i=i+1
    print(i)
    return x

#draw(f)
print(newtone(f,f_der,35,1e-3))
print(secant(f,35, 1e-3))
