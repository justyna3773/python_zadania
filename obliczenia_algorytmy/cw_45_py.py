import random

def generate_matrix(dim):
    matrix = []
    for i in range(dim):
            row_generate = random.choices(range(101), k=dim)
            matrix.append(row_generate)
    return matrix

def multiply_matrices(mat1,mat2):
    M = 8
    N = 8
    multip_mat = [[0] * N for _ in range(M)]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                multip_mat[i][j] += mat1[i][k] * mat2[k][j]
    return multip_mat
if __name__ == "__main__":
    mat1 = generate_matrix(8)
    mat2 = generate_matrix(8)
    print(multiply_matrices(mat1,mat2))
    