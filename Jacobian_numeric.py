def jacobian_solver(matrix, epsilon):
    '''
    jacobinal_solver - takes matrix and precision point and iterates with starting guess of 0's in all variables and uses the answer as the next guess
    uses rearageDominantDiagonal, buildEquationList
    Set maxLoops to 100 incase matrix is not diagonally dominant.
    :param matrix:
    :param epsilon:
    :return:
    '''
    n, m = find_matrix_size(matrix)
    maxLoops = None

    if not rearangeDominantDiagonal(matrix):  # Indicator for diagonally dominant matrix
        print("Matrix is no diagonally dominant.")
        maxLoops = 100
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
        for i in range(n):
            if abs(values[i] - values2[i]) <= epsilon:
                return values2[0:-1]
        values = list(values2)  # Update X_r to X_r1
        print(values2[:-1])
        if maxLoops == 0:
            print("The matrix ....")
            return


def buildEquationsList(matrix):
    '''
        -------M------
    | (  1   2   3 | 5   )
    N (  5   8   4 | 1   )   = >  [[0,-2,-3,5], [-5/8,0,-4/8,1/8], [-8/6,-9/6,0,6/6]]  =>  Example: x_r1 = -2y_r-3z_r+5
    | (  8   9   6 | 6   )

    :param matrix: (A|b) matrix from which the equations are extracted
    :return: Equations List
    '''
    i = 0  # pivot
    equation_list = list()
    for row in matrix:
        equation = [0 if x == i else -(row[x] / row[i]) for x in range(len(row))]
        equation[-1] *= -1
        equation_list.append(equation)
        i += 1
    return equation_list


def rearangeDominantDiagonal(matrix):
    '''
    rearangeDominantDiagonal - defines check_row function which takes pivot and row and checks if pivot in the same row equal or bigger than all elements
    in the same row for every row
    if check_row fails for a row, we check the next row and switch if the condition is met.
    if we reach last row and the condition is not met returns.
    :param matrix: matrix of size nXm where m = n+1 of the form (A|b)
    :return: true if diagonal dominant, false otherwise.
    '''
    n, m = find_matrix_size(matrix)
    check_row = lambda pivot, row: abs(pivot) >= sum(map(abs, matrix[row])) - abs(pivot) - abs(matrix[row][m - 1])
    for row in range(n):
        if check_row(matrix[row][row], row):
            continue
        else:
            for row2 in range(row + 1, n):
                if check_row(matrix[row2][row], row2):
                    exchange(matrix, row, row2)
                    break
                if row2 + 1 == n:
                    return False
    return True


def check_Dominant_Diagonal(matrix):
    '''
    :return: if matrix is Diagonal dominant returns true, else returns false.
    '''
    n, m = find_matrix_size(matrix)
    for row in range(n):
        if abs(sum(matrix[row][:-1]) - matrix[row][row]) > matrix[row][row]:
            return False
    return True


def find_matrix_size(mat):
    """
    Finds the matrix size
      -------M------
    | (           )
    N (           )
    | (           )
    :param mat: Given matrix
    :return: Size of the matrix in width, height
    """
    return len(mat), len(mat[0])  # n , m


def exchange(matrix, row, row2):
    """
    Exchanges two rows in the matrix and returns new matrix
    :param matrix: matrix in form of (A|b)
    :param row: pointer to row
    :param row2: pointer to row
    :return: e_matrix that changes the lines
    """
    matrix[row], matrix[row2] = matrix[row2], matrix[row]
    return matrix


# print(jacobian_solver([[4, 2, 0, 2], [2, 10, 4, 6], [0, 4, 5, 5]], 0.000001))
# print(jacobian_solver([[-1, 2, 4, 0], [1, -3, 2, 0], [3, -2, 1, 0]], 0.000001))
print(jacobian_solver([[7, -3, 1, 10], [2, 8, 3, 12], [4, 5, -9, 20]], 0.000001))


def mergeMetrix(matrix, vector):
    """
    Combines the matrix and the vector into one single matrix with free values
    (   4   2   0   )   (   2   )       (   4   2   0   |   2   )
    (   2   10  4   ) + (   6   )   =   (   2   10  4   |   6   )
    (   0   4   5   )   (   5   )       (   0   4   5   |   5   )
    :param matrix: n * n matrix
    :param vector: vector n * 1
    :return: n * n + 1 matrix
    """
    mat = []
    for i in range(len(vector)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][j])
        row.append(vector[i][0])
        mat.append(row)
    return mat


if __name__ == '__main__':
    matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    vectorB = [[2], [6], [5]]
    print(jacobian_solver(mergeMetrix(matrixA, vectorB), 0.000001))
