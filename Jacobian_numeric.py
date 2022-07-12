import csv
from GeneralMethods import *

def jacobian_solver(matrix, epsilon):
    '''
    jacobinal_solver - takes matrix and precision point and iterates with starting guess of 0's in all variables and uses the answer as the next guess
    uses rearageDominantDiagonal, buildEquationList
    Set maxLoops to 100 incase matrix is not diagonally dominant.
    :param matrix:(A|b) matrix
    :param epsilon: Result precision
    :return:
    '''
    n, m = find_matrix_size(matrix)
    maxLoops = None

    if not rearangeDominantDiagonal(matrix):  # Indicator for diagonally dominant matrix
        print("Warning: Matrix is no diagonally dominant.")
        maxLoops = 100
        print(f"Setting max iterations to: {maxLoops}")
    values = [0 for x in range(m)]

    equations = buildEquationsList(matrix)  # Build equations form matrix

    while True:
        if maxLoops is not None:  # maxLoop== None --> the matrix have dominant diagonal
            maxLoops -= 1
        j = 0
        values2 = list(values)
        for equation in equations:
            values2[j] = 0
            for i in range(len(equation) - 1):
                values2[j] += equation[i] * values[i]
            values2[j] += equation[-1]  # Adds the b vector element
            j += 1
        with open('data_jacobi.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(values2[:-1])
        for i in range(n):
            if abs(values[i] - values2[i]) <= epsilon:
                if maxLoops is not None:
                    print("Although there is no dominant diagonal the results are : ")
                else:
                    print("Matrix solution: ")
                return values2[0:-1]
        values = list(values2)  # Update X_r to X_r1
        print(values2[:-1])
        if maxLoops == 0:
            print("The system does not converge.")
            return
