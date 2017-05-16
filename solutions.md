# Exercises: Best practices I
Organising, debugging and profiling Python code

## 1. Creating a Python package
Following the slides 20/21 from this morning's session, we will create an **animals** package.

#### a-f. Create an animals package with submodules harmless and dangerous
The file structure of the package should look like this:
```
animals/
|
|___ __init__.py
|___ harmless/
     |
     |___ __init__.py
     |___ birds.py
     |___ mammals.py
     |___ fish.py
|___ dangerous/
     |
     |___ __init__.py
     |___ birds.py
     |___ mammals.py
     |___ fish.py
```

In the top level, we need to import the ```harmless``` and ```dangerous``` sub-directories into the top-level namespace of the ```animals``` package, so the content of the top-level ```__init__.py``` is:
```
from . import harmless
from . import dangerous
```

Inside the sub-directories, we import the different animals Classes into the namespace of ```harmless``` and ```dangerous```, so both the the sub-level ```__init__.py``` look like:
```
from .birds import Birds
from .mammals import Mammals
from .fish import Fish
```

Now, if we test our new ```animals``` package, executing the following
```
import animals

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()
```
outside the package, we get:
```bash
Printing members of the harmless Birds class
    Sparrow 
    Robin 
    Duck 
Printing members of the dangerous Fish class
    Shark 
    Fugu
```

## 2. Debugging
Investigate buggy code using the *pdb* or *ipdb* debugger. Have a look at slides 27-41 of this mornings's session for help.

#### a. Find all the bugs in the dicegame
This debugging example has been taken from [https://github.com/spiside/pdb-tutorial](https://github.com/spiside/pdb-tutorial). There you can find the official solution from the author of the dicegame. 

I've also provided my solution with annotations to all the fixes I made. You can find it in ```dicegame``` (in this repository).

## 3. Profiling
I decided to use the ```line_profiler``` via the command line, which I installed using ```pip install --user line_profiler```. 

#### a. Investigate the performance of the ```matmult.py``` script
The ```line_profiler``` needs a decorated function, therefore we need to put all the code of this script inside a function and decorate it with @profile:
```
# Program to multiply two matrices using nested loops
import random

def main(N):
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
    
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    for r in result:
        print(r)
        
if __name__ == '__main__':
    N = 250
    main(N)
```

Running this script with ```kernprof -l -v python matmult.py``` gives:

```bash
Wrote profile results to matmult.py.lprof
Timer unit: 1e-06 s

Total time: 17.2013 s
File: matmult.py
Function: main at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def main(N):
     6                                               # NxN matrix
     7         1            1      1.0      0.0      X = []
     8       251          102      0.4      0.0      for i in range(N):
     9     62750       302275      4.8      1.8          X.append([random.randint(0,100) for r in range(N)])
    10                                           
    11                                               # Nx(N+1) matrix
    12         1            1      1.0      0.0      Y = []
    13       251           86      0.3      0.0      for i in range(N):
    14     63000       305028      4.8      1.8          Y.append([random.randint(0,100) for r in range(N+1)])
    15                                               
    16                                               # result is Nx(N+1)
    17         1            0      0.0      0.0      result = []
    18       251          105      0.4      0.0      for i in range(N):
    19       250          536      2.1      0.0          result.append([0] * (N+1))
    20                                               
    21                                               # iterate through rows of X
    22       251          106      0.4      0.0      for i in range(len(X)):
    23                                                   # iterate through columns of Y
    24     63000        25756      0.4      0.1          for j in range(len(Y[0])):
    25                                                       # iterate through rows of Y
    26  15750250      6450858      0.4     37.5              for k in range(len(Y)):
    27  15687500     10090109      0.6     58.7                  result[i][j] += X[i][k] * Y[k][j]
    28                                           
    29       251          232      0.9      0.0      for r in result:
    30       250        26076    104.3      0.2          print(r)
```

which shows that most of our time is spend on the nested for loop. We should start optimizing for speed by thinking about alternative solutions instead of these loops.

For the memory profiling, we reduce N to 100 (otherwise it takes very long) and run ```python -m memory_profiler matmult.py```, which gives:

```bash
Line #    Mem usage    Increment   Line Contents
================================================
     4    9.148 MiB    0.000 MiB   @profile
     5                             def main(N):
     6                                 # NxN matrix
     7    9.148 MiB    0.000 MiB       X = []
     8    9.238 MiB    0.090 MiB       for i in range(N):
     9    9.238 MiB    0.000 MiB           X.append([random.randint(0,100) for r in range(N)])
    10                             
    11                                 # Nx(N+1) matrix
    12    9.238 MiB    0.000 MiB       Y = []
    13    9.328 MiB    0.090 MiB       for i in range(N):
    14    9.328 MiB    0.000 MiB           Y.append([random.randint(0,100) for r in range(N+1)])
    15                                 
    16                                 # result is Nx(N+1)
    17    9.328 MiB    0.000 MiB       result = []
    18    9.414 MiB    0.086 MiB       for i in range(N):
    19    9.414 MiB    0.000 MiB           result.append([0] * (N+1))
    20                                 
    21                                 # iterate through rows of X
    22    9.715 MiB    0.301 MiB       for i in range(len(X)):
    23                                     # iterate through columns of Y
    24    9.715 MiB    0.000 MiB           for j in range(len(Y[0])):
    25                                         # iterate through rows of Y
    26    9.715 MiB    0.000 MiB               for k in range(len(Y)):
    27    9.715 MiB    0.000 MiB                   result[i][j] += X[i][k] * Y[k][j]
    28                             
    29    9.719 MiB    0.004 MiB       for r in result:
    30    9.719 MiB    0.000 MiB           print(r)
```

Here we can see that range in line 22 makes up for most of the memory. Overall, this program is not very heavy on memory usage, surprise ;-) ...so nothing to improve there.

#### b. Investigate the performance of the ```euler72.py``` script
Running the line_profiler on this script, shows that the slowest part is the factorize function. So that is where we should start improving. The memory profiling did not reveal any substantial problems with memory. 

#### c. Improve the performance of the ```matmult.py``` script
Using numpy arrays instead of lists allows for in-place matrix multiplication and thus we avoid the nested for loops. Profile our improved script gives:

```bash
Wrote profile results to matmult_numpy.py.lprof
Timer unit: 1e-06 s

Total time: 0.011343 s
File: matmult_numpy.py
Function: main at line 5

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     5                                           @profile
     6                                           def main(N):
     7                                               # NxN matrix
     8         1          178    178.0      1.6      X = np.random.randint(0,100,size=(N,N))
     9                                           
    10                                               # Nx(N+1) matrix
    11         1          148    148.0      1.3      Y = np.random.randint(0,100,size=(N,N+1))
    12                                               
    13                                               # result is Nx(N+1)
    14         1          843    843.0      7.4      result = np.dot(X,Y)
    15         1        10174  10174.0     89.7      print(result)
```

This shows that using numpy substantiall increases the performance when dealing with arrays (matrices) and also, our script is much more simple and clean!

