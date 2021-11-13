#!/usr/bin/env python3

from sys import argv
from functools import reduce

def main():
    with open(argv[1], 'r') as F:
        data = F.readline().strip().split(sep=" ")

    # Convert strings to ints
    data = [int(x) for x in data]

    print(fib1(data[0], data[1]))
    print(fib2(data[0], data[1]))

# Alter fibonacci to Fn = Fn-1 + Fn-2*k
def fib1(n,k):
    if n <= 1:
        return n
    else:
        return fib1(n-1,k) + fib1(n-2,k)*k

def fib2(n,k):
    return reduce(lambda x,n: [x[1], x[1] + x[0]*k], range(n), [0, 1])[0]

if __name__ == '__main__':
    main()