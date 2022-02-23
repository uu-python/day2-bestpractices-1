# Program to multiply two matrices using nested loops
import random

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

    
# lX, lY0, lY = len(X), len(Y[0]), len(Y)
# # iterate through rows of X
# for i in range(lX):
#     # iterate through columns of Y
#     xi = X[i]
#     for j in range(lY0):
#         # iterate through rows of Y
#         for k in range(lY):
#             result[i][j] += xi[k] * Y[k][j]

# lY0, lY = len(Y[0]), len(Y)
# # iterate through rows of X
# for i, xi in enumerate(X):
#     # iterate through columns of Y
#     for j in range(lY0):
#         # iterate through rows of Y
#         for k, yk in enumerate(Y):
#             result[i][j] += xi[k] * yk[j]

lX, lY0, lY = len(X), len(Y[0]), len(Y)
# iterate through rows of X
for i in range(lX):
    # iterate through columns of Y
    xi = X[i]
    for j in range(lY0):
        # iterate through rows of Y
        for k in range(lY):
            result[i][j] += xi[k] * Y[k][j]

#for r in result:
    #print(r)
