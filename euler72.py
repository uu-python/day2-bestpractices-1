#!/usr/bin/python

from math import ceil,sqrt
@profile
def gen_primes(n):
    l = range(2,n)
    primes = []
    for j in range(0,len(l)):
        p = True
        for d in primes:
            if(d > sqrt(l[j])):
                break
            if(l[j] % d == 0):
                p = False
                break;
        if(p):
            primes.append(l[j])

    return primes

@profile
def factorize(n,primes):
    factors = []
    init_n = n
    for p in primes:
        while(n%p == 0):
            n = n/p
            factors.append(p)
        if(p > sqrt(n)):
            break
    if(n > 1):
        factors.append(n)
    return factors

    
def phi(n,primes):
    factors = factorize(n,primes)
    p = 1

    for i in range(2,n):
        flag = True
        for f in factors:
            if i%f == 0:
                flag = False
                break
        if flag:
            p+=1
    return p

@profile
def fast_phi(n,primes):
    factors = factorize(n,primes)
    phi = factors[0]-1
    for i in range(1,len(factors)):
        if(factors[i] == factors[i-1]):
            phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
        else:
            phi *= (factors[i]-1)
    return phi

primes = gen_primes(1000)
m = 10000
#m = 8
fraq = 0
for i in range(2,m+1):
    fraq += fast_phi(i,primes)

print(fraq)
