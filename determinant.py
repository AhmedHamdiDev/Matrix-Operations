from submatrix import *
def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    determinant = 0
    for j in range(0, n):
        sign = (-1) ** j
        minor = det(submatrix(0, j, matrix))
        determinant += sign * matrix[0][j] * minor
    return determinant