#!/usr/bin/env python3

from sys import argv

with open(argv[1], 'r') as F:
    seq = F.readline().strip().upper()

seq = seq[::-1].translate(str.maketrans('ATGC','TACG'))

print(seq)