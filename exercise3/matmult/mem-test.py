import numpy as np

@profile
def basic():
    x = 1
    y = 1

@profile
def test():
    x = np.ones(10000)
    y = x**2
    
@profile
def part1():
    test()
@profile
def part2():
    for i in range(50):
        test()

# basic()
# basic()
basic()
part1()
part2()
basic()