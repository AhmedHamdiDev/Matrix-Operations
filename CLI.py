from submatrix import *
from determinant import *
from transposition import *
from adjugate import *
from inverse import *
from equation import *

while True:
    #Choosing the operation
    print("1)Submatrix 2)Determinant 3)Transpose 4)Adjugate 5)Inverse 6)Solve Equation Using Cramer's Rule 7)Exit")
    cmd=int(input("Choose your operation: "))
    #Submatrix Calculation
    if cmd==1:
        while True:
            try:
                #The given dimensions must resemble a square matrix, otherwise the algorithm won't work
                m=input("Type in the dimensions of your matrix with spacing in between: ")
                dim=m.split(sep=" ")
                dim[0]=int(dim[0])
                dim[1]=int(dim[1])
                matrix=[]
            except:
                print("Enter a valid size")
            if len(m)>=5 or dim[0]!=dim[1]:
                print("Please enter a valid size")
            else:
                break
        #Taking in matrix entries. Those entries must be integers. Otherwise, the algorithm won't work
        for i in range(dim[0]):
            matrix.append([])
            for j in range(dim[1]):
                while True:
                    try:
                        a_ij=float(input(f"Enter a{i+1}{j+1}: "))
                        matrix[i].append(a_ij)
                    except (ValueError, TypeError):
                        print("Please enter a valid value")
                    else:
                        break
        #When finding a submatrix two axes must be chosen. Those need to be integers. Otherwise, the algorithm won't work.
        while True:
            try:
                i=int(input("Choose i: "))
            except (ValueError, TypeError):
                print("Please Enter a valid i")
            else:
                break
        while True:
            try:
                j = int(input("Choose j: "))
            except (ValueError, TypeError):
                print("Please Enter a valid j")
            else:
                break
        print(submatrix(i-1, j-1, matrix))

    elif cmd ==2:
        while True:
            try:
                # The given dimensions must resemble a square matrix, otherwise the algorithm won't work
                m = input("Type in the dimensions of your matrix with spacing in between: ")
                dim = m.split(sep=" ")
                dim[0] = int(dim[0])
                dim[1] = int(dim[1])
                matrix = []
            except:
                print("Please enter a valid size")
            if len(m)>=5 or dim[0]!=dim[1]:
                print("Please enter a valid size")
            else:
                break
        for i in range(dim[0]):
            matrix.append([])
            for j in range(dim[1]):
                while True:
                    try:
                        a_ij = float(input(f"Enter a{i + 1}{j + 1}: "))
                        matrix[i].append(a_ij)
                    except (ValueError, TypeError):
                        print("Enter a valid value")
                    else:
                        break
        print(det(matrix))
    elif cmd==3:
        while True:
            try:
                m=input("Type in the dimensions of your matrix with spacing in between: ")
                dim=m.split(sep=" ")
                dim[0]=int(dim[0])
                dim[1]=int(dim[1])
                matrix=[]
            except:
                print("Enter a valid size")
            if len(m)>=5 or dim[0]!=dim[1]:
                print("Please enter a valid size")
            else:
                break
        for i in range(dim[0]):
            matrix.append([])
            for j in range(dim[1]):
                while True:
                    try:
                        a_ij=float(input(f"Enter a{i+1}{j+1}: "))
                        matrix[i].append(a_ij)
                    except (ValueError, TypeError):
                        print("Please enter a valid value")
                    else:
                        break
        print(trans(matrix))
    elif cmd==4:
        while True:
            try:
                m = input("Type in the dimensions of your matrix with spacing in between: ")
                dim = m.split(sep=" ")
                dim[0] = int(dim[0])
                dim[1] = int(dim[1])
                matrix = []
            except:
                print("Enter a valid size")
            if len(m) >= 5 or dim[0] != dim[1]:
                print("Please enter a valid size")
            else:
                break
        for i in range(dim[0]):
            matrix.append([])
            for j in range(dim[1]):
                while True:
                    try:
                        a_ij = float(input(f"Enter a{i + 1}{j + 1}: "))
                        matrix[i].append(a_ij)
                    except (ValueError, TypeError):
                        print("Please enter a valid value")
                    else:
                        break
        print(adj(matrix))
    elif cmd==5:
        while True:
            try:
                m=input("Type in the dimensions of your matrix with spacing in between: ")
                dim=m.split(sep=" ")
                dim[0]=int(dim[0])
                dim[1]=int(dim[1])
                matrix=[]
            except:
                print("Enter a valid size")
            if len(m)>=5 or dim[0]!=dim[1]:
                print("Please enter a valid size")
            else:
                break
        for i in range(dim[0]):
            matrix.append([])
            for j in range(dim[1]):
                while True:
                    try:
                        a_ij=float(input(f"Enter a{i+1}{j+1}: "))
                        matrix[i].append(a_ij)
                    except (ValueError, TypeError):
                        print("Please enter a valid value")
                    else:
                        break
        print(inverse(matrix))
    elif cmd==6:
        while True:
            try:
                n=int(input("Enter the number of equations: "))
            except (TypeError, ValueError):
                print("Please enter a valid number")
            else:
                break
        coefficients=[]
        for i in range(n):
            coefficients.append([])
            for j in range(n):
                while True:
                    try:
                        a_ij = float(input(f"Enter a{i + 1}{j + 1}: "))
                        coefficients[i].append(a_ij)
                    except (ValueError, TypeError):
                        print("Please enter a valid value")
                    else:
                        break
        values = []
        for i in range(n):
            values.append([])
            while True:
                try:
                    b_i = float(input(f"Enter b{i + 1}: "))
                    values[i].append(b_i)
                except (ValueError, TypeError):
                    print("Please enter a valid value")
                else:
                    break
        print(cramer(coefficients, values))


    elif cmd==7:
        exit(0)
    else:
        print("Please choose a valid operation")