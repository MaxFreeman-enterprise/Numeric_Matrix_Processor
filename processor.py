import math

def print_matrix(matrix):
    print("The result is:")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]:.3f}"[:-1], end=" ")
        print()


def input_matrix():
    r_matrix, c_matrix = [int(s) for s in input("Enter matrix size: ").split()]
    print("Enter matrix:")
    matrix = [[float(item) for item in
               input().split(' ')] for i in range(r_matrix)]

    return r_matrix, c_matrix, matrix


def multiply_matrices(r_matrix1, c_matrix1, matrix_1, r_matrix2, c_matrix2, matrix_2):

    if not c_matrix1 == r_matrix2:
        print("ERROR")

    else:

        final_matrix = [[0 for j in range(c_matrix2)] for i in range(r_matrix1)]
        for i in range(r_matrix1):
            for j in range(c_matrix2):
                matrix_1_row_i = matrix_1[i]
                matrix_2_column_j = [row[j] for row in matrix_2]
                final_matrix[i][j] = sum([matrix_1_row_i[k] * matrix_2_column_j[k] for k in range(c_matrix1)])

        return final_matrix


def const_mult_matrix(r_matrix, c_matrix, matrix, constant):

    for i in range(r_matrix):
        for j in range(c_matrix):
            matrix[i][j] *= constant

    return matrix


def add_matrices(r_matrix1, c_matrix1, matrix_1, r_matrix2, c_matrix2, matrix_2):

    if not (r_matrix1 == r_matrix2 and c_matrix1 == c_matrix2):
        print("ERROR")

    else:

        final_matrix = [[0.0 for j in range(c_matrix1)] for i in range(r_matrix1)]

        # final_matrix = [[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]

        for i in range(len(matrix_1)):
            for j in range(len(matrix_1[0])):
                final_matrix[i][j] = matrix_1[i][j] + matrix_2[i][j]

        return final_matrix


def main_diagonal_transpose(r_matrix, c_matrix, matrix):
    final_matrix = [[0 for j in range(c_matrix)] for i in range(r_matrix)]
    for i in range(c_matrix):
        # final_matrix[i] = [row[i] for row in matrix]
        col_i = []
        for row in matrix:
            col_i.append(row[i])
        final_matrix[i] = col_i
    return final_matrix


def side_diagonal_transpose(r_matrix, c_matrix, matrix):
    final_matrix = [[0 for j in range(c_matrix)] for i in range(r_matrix)]
    for i in range(c_matrix):
        col_i = []
        for row in matrix:
            col_i.append(row[-i - 1])
        final_matrix[i] = col_i[::-1]
    return final_matrix


# def side_diagonal_transpose(r_matrix, c_matrix, matrix):
#     final_matrix = [[0 for j in range(c_matrix)] for i in range(r_matrix)]
#     for i in range(c_matrix):
#         for j in range(r_matrix):
#             final_matrix[i][j] = matrix[-j-1][-i-1]
#     return final_matrix


# def side_diagonal_transpose(r_matrix, c_matrix, matrix):
#     return [[row[-i-1] for row in matrix][::-1] for i in range(r_matrix)]


def vertical_line_transpose(r_matrix, c_matrix, matrix):
    final_matrix = [[0 for j in range(c_matrix)] for i in range(r_matrix)]
    for i in range(r_matrix):
        final_matrix[i] = matrix[i][::-1]

    return final_matrix


# def horizontal_line_transpose(r_matrix, c_matrix, matrix):
#     final_matrix = []
#     column_matrix_representation = main_diagonal_transpose(r_matrix,c_matrix,matrix)
#     for i in range(c_matrix):
#         final_matrix.append(column_matrix_representation[i][::-1])
#     return main_diagonal_transpose(c_matrix,r_matrix,final_matrix)


def horizontal_line_transpose(r_matrix, c_matrix, matrix):
    return [row[:] for row in matrix][::-1]


def matrix_minor(i, j, matrix):
    minor_matrix = [row[:] for row in matrix]
    del minor_matrix[i]
    for row in minor_matrix:
        del row[j]

    return minor_matrix


def determinant(r_matrix, c_matrix, matrix):
    if r_matrix == 1 and c_matrix == 1:
        return matrix[0][0]

    elif r_matrix == 2 and c_matrix == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    else:
        res = 0

        # r and c come from this math formula for calculating determinant;
        # detA = sum(A[i,j] * X[i,j]) for j=0 to len(A[0])
        # X[i,j]=((−1)**(i+j))*detM[i,j]

        r = 0
        for c in range(len(matrix[r])):  # expand by row r
            res += ((-1) ** (r + c)) * matrix[r][c] * determinant(r_matrix - 1, c_matrix - 1,
                                                                  matrix_minor(r, c, matrix))

        return res


def is_invertible(r_matrix, c_matrix, matrix):
    if r_matrix != c_matrix or determinant(r_matrix, c_matrix ,matrix) == 0:
        return False
    else:
        return True


def inverse(r_matrix, c_matrix, matrix):

    det = determinant(r_matrix, c_matrix, matrix)

    cofactor_matrix = [[0 for j in range(c_matrix)] for i in range(r_matrix)]

    for i in range(r_matrix):
        for j in range(c_matrix):
           cofactor_matrix[i][j] = ((-1) ** (i + j)) * determinant(r_matrix - 1, c_matrix - 1,
                                                           matrix_minor(i, j, matrix))
    cofactor_matrix = main_diagonal_transpose(r_matrix, c_matrix, cofactor_matrix)

    return const_mult_matrix(r_matrix, c_matrix, cofactor_matrix, 1 / det)


while True:
    print("""
    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    6. Inverse matrix
    0. Exit""")

    user_choice = int(input("Your choice: "))

    if user_choice == 1:
        print_matrix(add_matrices(*input_matrix(), *input_matrix()))

    elif user_choice == 2:
        print_matrix(const_mult_matrix(*input_matrix(), float(input())))

    elif user_choice == 3:
        print_matrix(multiply_matrices(*input_matrix(), *input_matrix()))

    elif user_choice == 4:
        print("""
        1. Main diagonal
        2. Side diagonal
        3. Vertical line
        4. Horizontal line""")

        user_choice = int(input("Your choice: "))

        if user_choice == 1:
            print_matrix(main_diagonal_transpose(*input_matrix()))

        elif user_choice == 2:
            print_matrix(side_diagonal_transpose(*input_matrix()))

        elif user_choice == 3:
            print_matrix(vertical_line_transpose(*input_matrix()))

        elif user_choice == 4:
            print_matrix(horizontal_line_transpose(*input_matrix()))

    elif user_choice == 5:
        r_matrix, c_matrix, matrix = input_matrix()
        if r_matrix != c_matrix:  # square matrix required for determinant
            print("ERROR")
        else:
            print(determinant(r_matrix, c_matrix, matrix))

    elif user_choice == 6:
        r_matrix, c_matrix, matrix = input_matrix()

        if not is_invertible(r_matrix, c_matrix, matrix):
            print("Warning: this matrix is not invertible.")

        else:
            print_matrix(inverse(r_matrix, c_matrix, matrix))

    elif user_choice == 0:
        exit()

# mm = [[1,2,3],[4,5,7],[10,22,23]]
# print(determinant(3,3,mm))

# mm = [[2,-1,0],[0,1,2],[1,1,0]]
# print_matrix(inverse(3,3,mm))
