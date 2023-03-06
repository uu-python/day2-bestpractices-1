#!/usr/bin/python

def fact(x): return (1 if x==0 else x * fact(x-1))

def is_curious(n):
    s = str(n)
    sum = 0;
    for c in s:
        sum += fact(int(c))
    if(sum == n):
        return True
    return False

for a in range(10,1000000):
    import ipdb; ipdb.set_trace() # add pdb here
    if(is_curious(a)):
        print(a)
