from adjugate import *
from determinant import *
def inverse(matrix):
    if det(matrix)!=0:
        matrix_=adj(matrix)
        n=len(matrix_)
        d=det(matrix)
        for i in range(n):
            for j in range(n):
                matrix_[i][j]/=d
        return matrix_
    else:
        return "The given matrix is singular"