#!/usr/bin/env python3

from sys import exit, argv
from math import comb

def main():
    if argv[1]:
        fileName = argv[1]
    else:
        exit("No file provided")

    with open(argv[1], 'r') as F:
        data = F.readline().strip().split(sep=" ")

    # Convert strings to ints
    data = [int(x) for x in data]

    # Calculate probability
    prob = binomCDF(data[1]-1, 2**data[0], 0.25)
    print('{:.3f}'.format(1-prob))

# Probability mass function for binomial distribution
def binomPMF(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

# Cumulative density function for binomial distribution
def binomCDF(x, n, p):
    return sum([binomPMF(x, n, p) for x in range(0,x+1)])

if __name__ == '__main__':
    main()