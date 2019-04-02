import numpy
import matplotlib.pyplot as plt
from numpy import exp
#y=a/x+b*exp(x)+c
#dy/da=0 -> 2*a/(x^2) + 2*b*exp(x)/x + 2*c/x = 2*y/x
#dy/db=0 -> 2*a*exp(x)/x + 2*b*exp(2*x) + 2*c*exp(x) = 2*y*exp(x)
#dy/dc=0 -> 2*a/x + 2*b*exp(x) + 2*c = 2*y

if __name__ == "__main__":
    x_start = numpy.array([0.324, 0.645, 0.966, 1.287, 1.609, 1.930, 2.251, 2.572, 2.893], dtype=float)
    y_start = numpy.array([-2.052,-1.756, -1.076, -0.284, 0.982, 2.209, 4.013, 5.796, 8.011], dtype=float)
    x_linspace = numpy.linspace(numpy.min(x_start), numpy.max(x_start), 100)
    func = lambda x, a, b, c: a/x + b*numpy.exp(x) + c
    abc_matrix = numpy.array([
        [sum([2/(x**2) for x in x_start]), sum([2*exp(x)/x for x in x_start]), sum([2/x for x in x_start])],
        [sum([2*exp(x)/x for x in x_start]), sum([2*exp(2*x) for x in x_start]), sum([2*exp(x) for x in x_start])],
        [sum([2/x for x in x_start]), sum([2*exp(x) for x in x_start]), 2]
    ])
    y_matrix = numpy.array([sum([2*y_start[i]/x_start[i] for i in range(len(y_start))]), sum([2*y_start[i]*exp(x_start[i]) for i in range(len(x_start))]), sum([2*y for y in y_start])])

    abc_coef = numpy.linalg.solve(abc_matrix, y_matrix)
    y_ans = [func(x, abc_coef[0], abc_coef[1], abc_coef[2]) for x in x_linspace]
    plt.plot(x_start,y_start,'o', x_linspace, y_ans)
    plt.grid(True)
    plt.show()