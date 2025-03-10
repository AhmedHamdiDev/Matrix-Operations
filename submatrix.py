def submatrix(i, j, matrix):
    result=[]
    for n in range(len(matrix)):
        if n != i:
            result.append(matrix[n].copy())
    for row in result:
        del row[j]
    return result

