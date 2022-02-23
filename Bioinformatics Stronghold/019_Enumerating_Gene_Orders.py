#!/usr/bin/env python3

from itertools import permutations
from sys import exit, argv

def main():
    if argv[1]:
        fileName = argv[1]
    else:
        exit("No file provided")

    with open(argv[1], 'r') as F:
        n = F.readline().strip()
    
    values = range(1, int(n)+1)
    
    perm = list(permutations(values))
    
    print(len(perm))
    print('\n'.join([' '.join([str(i) for i in p]) for p in perm]))

if __name__ == '__main__':
    main()