@profile
def matmult():
    # Program to multiply two matrices using nested loops
    import random

    def colum(matrix, col):
        return [r[col] for r in matrix]

    def dot(a,b):
        return sum([ea*eb for ea, eb in zip(a,b)])

    N = 250

    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])

    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])

    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    
    for row_index in range(len(X)):
        for col_index in range(len(Y[0])):
             result[row_index][col_index] = dot(X[row_index],colum(Y,col_index))
    
    print(result)

if __name__ == '__main__':
    matmult()