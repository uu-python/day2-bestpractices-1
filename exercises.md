# Exercises for Day 2
Organising, debugging and profiling Python code

## 1. Creating a Python package
Following the slides 19/20 from this morning's session, we will create an **animals** package.

> Please note that with Python 3, implicit relative imports are no longer supported [https://www.python.org/dev/peps/pep-0328/](https://www.python.org/dev/peps/pep-0328/)

#### a. Create a directory for package

#### b. Add the modules ```birds.py``` and ```mammals.py``` into your package directory

#### c. Add ```__init__.py``` module to your package
The ```__init__.py``` module should import the ```Birds``` and ```Mammals``` class from the two modules.

#### d. Test your animals package
Using a python script or an interactive python session outside the package, test your brand new package:

```
import animals

m = animals.Mammals()
m.printMembers()

b = animals.Birds()
b.printMembers()
```

#### e. Add another module called ```fish.py``` amd integrate it into your package

#### f. Reorganize your package such that you can use it like this:
```
import animals

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()
```

## 2. Debugging
Investigate buggy code using the *pdb* or *ipdb* debugger. Have a look at slides 27-41 of this mornings's session for help.

#### a. Find all the bugs in the dicegame
Clone this repo (if you have not already done so), go to ```buggy```  and run the ```main.py``` with a debug tracer added to the code. Once you have fixed all errors, the game should correctly add up the values of the dice for 6 consecutive turns.

#### b. If you cannot get enough of debugging
Ask your neighbour to introduce more bugs into the above (or any other) code examples and try to find the bug using the debugger. 

## 3. Profiling
In this section, you should get more familiar with code profiling, in particular with the tools ```cProfile```, ```line_profiler``` and ```memory_profiler```. Have a look at slides 44-52 from this morning's session to understand what they are doing and when you should use them. Try out profiling both from the command line and using interactive python (e.g. jupyter notebook).

#### a. Investigate the performance of the ```matmult.py``` script
In which line(s) of the script would you start optimizing for speed? Which line(s) create the most memory?

#### b. Investigate the performance of the ```euler72.py``` script
In which line(s) of the script would you start optimizing for speed? Which line(s) create the most memory?
(This is one problem from the euler project: [https://projecteuler.net/problem=72](https://projecteuler.net/problem=72))

#### c. Improve the performance of the ```matmult.py``` script
What is the best performance that you achieved with N=250?
