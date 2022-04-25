from Jacobian_numeric import *


def gauss_seidel_solver(matrix,epsilon):
    n, m = find_matrix_size(matrix)
    maxLoops = None
    if not rearangeDominantDiagonal(matrix):
        print("Matrix is not diagonally dominant")
        maxLoops = 100
    equations = buildEquationsList(matrix) # [[0,1,2,3],[4,0,5,6],[7,8,0,9]], values[0,0,0]
    values = [0 for x in range(m-1)]

    while True:
        if maxLoops != None:
            maxLoops -=1
        temp_list = list(values)
        for i in range(m - 1): # []
            values[i] = sum([values[j]*equations[i][j] for j in range(m-1)])
            values[i] += equations[i][-1]

        print(values)
        for i in range(m-1):
            if abs(temp_list[i] - values[i]) <= epsilon:
                if maxLoops is not None:
                    print("Although there is no dominant diagonal the results are : ")
                else:
                    print("Matrix solution: ")
                return values
        if maxLoops == 0:
            print("The system does not converge. ")
            return




