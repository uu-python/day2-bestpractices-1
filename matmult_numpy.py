# Program to multiply two matrices using nested loops
import random
import numpy as np

@profile
def main(N):
    # NxN matrix
    X = np.random.randint(0,100,size=(N,N))

    # Nx(N+1) matrix
    Y = np.random.randint(0,100,size=(N,N+1))
    
    # result is Nx(N+1)
    result = np.dot(X,Y)
    print(result)
    
if __name__ == '__main__':
    N = 250
    main(N)
