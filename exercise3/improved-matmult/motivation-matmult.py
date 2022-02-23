# This code was modified inspired by this solution:
# https://stackoverflow.com/a/61583971/10172674

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

# # result is Nx(N+1)
# result = []
# for i in range(N):
#     result.append([0] * (N+1))
    
result=[]

def multiplicationLineColumn(line,column):
    try:
        sizeLine=len(line)
        sizeColumn=len(column)
        if(sizeLine!=sizeColumn):
            raise ValueError("Exception")
        res = sum([line[i] * column[i] for i in range(sizeLine)])
        return res
    except ValueError:
        print("sould have the same len line & column")

def  getColumn(result,numColumn):
    size=len(result)
    column= [result[i][numColumn] for i in range(size)]
    return column

def getLine(result,numLine):
    line = result[numLine]
    return line

for i in range(len(X)):
    result.append([])
    for j in range(len(Y)):
        result[i].append(multiplicationLineColumn(getLine(X,i),getColumn(Y,j)))

for r in result:
    print(r)