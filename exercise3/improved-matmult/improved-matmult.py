# By seeing how powerful sum() can be I decided to test how it would perform in a setup closer to the initial one, with the result matrix being initizalized outside the loops

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

lenY = len(Y) # Save this value to avoid repetition
# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # Instead of iterating again we use the sum method, which is faster
        result[i][j] = sum([X[i][k] * Y[k][j] for k in range(len(Y))])

for r in result:
    print(r)