import copy

from determinant import *
def cramer(coefficients, values):
    d=det(coefficients)
    solutions=[]
    n=len(coefficients)

    for i in range(n):
        d_i=copy.deepcopy(coefficients)
        for j in range(n):
            d_i[j][i]=values[j][0]
        if det(d_i)/d!=0:
            solutions.append(det(d_i)/d)
        else:
            solutions.append(0.0)
    return tuple(solutions)