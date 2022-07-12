from Gauss_Seidel_Matrix_Sovler import *
from SOR import *

if __name__ == '__main__':
    method = int(input("Hello ! in which method would you like to solve ? \n 1. Jacobi method \n 2. Gauss-Seidel method.\n"))
    matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    matrixB = [[4, 2, 0.0], [5, 4, 3], [13, 3, 15]]
    vectorB = [[2], [6], [5]]
    print(successive_Over_Relaxation(mergeMetrix(matrixA, vectorB), 0.000001))
    if method == 1:
        print(jacobian_solver(mergeMetrix(matrixA, vectorB), 0.000001))
    else:
        print(gauss_seidel_solver(mergeMetrix(matrixA, vectorB), 0.000001))


