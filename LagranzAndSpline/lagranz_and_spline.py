import numpy
import matplotlib.pyplot as plt
import matplotlib.lines as lines

def lagranz(x, y, val):
    res = 0
    for i in range(len(y)):
        numerator = 1
        denomerator = 1
        for j in range(len(x)):
            if i != j:
                numerator = numerator*(val-x[j])
                denomerator = denomerator*(x[i]-x[j])
        res = res + y[i]*numerator/denomerator
    return res

def linear(x1,x2,y1,y2,val):
    return (-(x1*y2-x2*y1)-(y1-y2)*val)/(x2-x1)

def linear_spline(x,y):
    res = []
    for i in range(1, len(x)):
        x_linspace = numpy.linspace(x[i-1],x[i],100)
   #     y_linspace = [linear(x[i-1],x[i],y[i-1],y[i],j) for j in x_linspace]
        for j in range(len(x_linspace)):
            res.append(linear(x[i-1],x[i],y[i-1],y[i],x_linspace[j]))
       # res = numpy.append(res, y_linspace)
    return numpy.array(res)


if __name__ == "__main__":
    x=numpy.array([0.235,0.672,1.385,2.108,2.938], dtype=float)
    y=numpy.array([1.082,1.805,4.280,5.011,7.082], dtype=float)
    x_linspace = numpy.linspace(numpy.min(x),numpy.max(x),100)
    y_linspace=[lagranz(x,y,i) for i in x_linspace]
    plt.plot(x,y,'o',x_linspace, y_linspace)
    plt.grid(True)
    plt.show()
    y_linspace=linear_spline(x,y)
    x_linspace = numpy.linspace(numpy.min(x), numpy.max(x), len(y_linspace))
    plt.plot(x_linspace,y_linspace)
    plt.grid(True)
    plt.show()
