import random

def generate_matrix(dim):
    matrix = []
    for i in range(dim):
            row_generate = random.choices(range(101), k=dim)
            matrix.append(row_generate)
    return matrix
def matrix_determinant(mat, total = 0):
    ind = list(range(len(mat)))
    
    if len(mat) == 2 and len(mat[0]) == 2:
        deter_2 = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return deter_2
    
    for part in ind:
        mat1 = mat
        mat1 = mat1[1:]
        length = len(mat1) 
 
        for i in range(length): 
            mat1[i] = mat1[i][0:part] + mat1[i][part+1:] 
 
        
        recursive_determinant = matrix_determinant(mat1)
        total +=((-1) ** (part % 2)) * mat[0][part] * recursive_determinant
 
    return total

if __name__ == "__main__":
    
    #A = generate_matrix(3)
    A = [[3,1,1], [1,1,1], [3,1,3]]
    print(A)
    print(matrix_determinant(A))

