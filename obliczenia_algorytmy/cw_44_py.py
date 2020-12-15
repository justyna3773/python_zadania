import random

def generate_matrix(dim):
    matrix = []
    for i in range(dim):
            row_generate = random.choices(range(101), k=dim)
            matrix.append(row_generate)
    return matrix

def sum_matrices(mat1, mat2):
    M = 128
    N = 128
    sum_mat = [[0] * N for _ in range(M)]
    for i in range(len(mat1)):
        # for j,k in zip(mat1[i], mat2[i]):
        #     sum_mat[i][j] = 
        for j in range(len(mat1)):
            sum_mat[i][j] = mat1[i][j]+mat2[i][j]
    return sum_mat

if __name__ == "__main__":
    mat1 = generate_matrix(128)
    mat2 = generate_matrix(128)
    mat3 = sum_matrices(mat1, mat2)
    print(mat1[0][0])
    print(mat2[0][0])
    print(mat3[0][0])
    
