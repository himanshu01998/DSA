import numpy as np

# Question 7 - Rotate a matrix 90 degrees clockwise of NxN matrix with depth print statements

def rotate_matrix(matrix):

    n = len(matrix)

    for layer in range(n // 2):
        print("Layer", layer)
        first, last = layer, n - layer - 1
        print("First", first, " Last", last)

        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            print(-i-1)
            print(matrix[layer][i], "=", matrix[-i - 1][layer])
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            print(matrix[-i - 1][layer], "=", matrix[-layer - 1][-i - 1])
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            print(matrix[-layer - 1][-i - 1], "=", matrix[i][- layer - 1])
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            print(matrix[i][- layer - 1], "=", top)
            matrix[i][- layer - 1] = top
            print()

    return matrix

# matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
matrix = np.array([[1,2,3,10], [4,5,6,11], [7,8,9,12], [13,14,15,16]])
print(matrix, "\n")

print(rotate_matrix(matrix))
