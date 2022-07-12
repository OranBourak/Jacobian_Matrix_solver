from GeneralMethods import *
import csv

def successive_Over_Relaxation(matrix, epsilon, w=1.16):
    """
    SOR Algorithm that displayes the middle answers and solves the give matrix with the given epsilon for the error
    limit and the w value which is responsible for the relaxation(extrapolation) factor
    :param matrix: The matrix to solve
    :param epsilon: The error limit
    :param w: relaxation factor
    :return: Solution for the matrix
    """
    n, m = find_matrix_size(matrix)
    maxLoops = None
    if not rearangeDominantDiagonal(matrix):
        print("Matrix is not diagonally dominant")
        maxLoops = 100
    equations = buildEquationsList(matrix) # [[0,1,2,3],[4,0,5,6],[7,8,0,9]], values[0,0,0]
    values = [0 for x in range(m-1)]
    loops = 0
    while True:
        loops += 1
        if maxLoops != None:
            maxLoops -=1
        temp_list = list(values)
        for i in range(m - 1): # []
            values[i] = (sum([values[j]*equations[i][j] for j in range(m-1)]) + equations[i][-1]) * w + (1-w) * values[i]
            values[i]
        with open('data_SOR.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(values)
        print(values)
        for i in range(m-1):
            if abs(temp_list[i] - values[i]) <= epsilon:
                if maxLoops is not None:
                    print("Although there is no dominant diagonal the results are : ")
                else:
                    print(f'Num of iterations : {loops}')
                    print("Matrix solution: ")
                return values
        if maxLoops == 0:
            print("The system does not converge. ")
            return

