from Jacobian_numeric import *
from SOR import *
from Gauss_Seidel_Matrix_Sovler import *

if __name__ == '__main__':
    method = int(input(
        "Hello ! in which method would you like to solve ? \n 1. Jacobi method \n 2. SOR method. \n 3. Gauss-Seidel method.\n"))
    # matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    matrixA = [[4, 2, 0, 2], [2, 10, 4, 6], [0, 4, 5, 5]]
    matrixB = [[4, 2, 0.0], [5, 4, 3], [13, 3, 15]]
    # vectorB = [[2], [6], [5]]

    if method == 1:
        print(jacobian_solver(matrixA, 0.000001))
    elif method == 2:
        print(successive_Over_Relaxation(matrixA, 0.000001, 1.16))
    elif method == 3:
        print(gauss_seidel_solver(matrixA, 0.000001))
