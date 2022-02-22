#!/bin/env python
# Program to multiply two matrices using nested loops
import random
import numpy as np
from memory_profiler import profile


N = 250

@profile
def matmult(N):
    #NxN matrix
    X = np.random.randint(100, size=(N, N))

    #Nx(N+1) matrix
    Y = np.random.randint(100, size=(N, N+1))

    # result is Nx(N+1) matrix
    result = np.matmul(X,Y)
    return result

print(matmult(N))
