from submatrix import *
from transposition import *
from determinant import *
def adj(matrix):
    n=len(matrix)
    result=[]
    for i in range(n):
        result.append([])
        for j in range(n):
            result[i].append(((-1)**(i+j))*det(submatrix(i, j, matrix)))
    trans(result)
    return result