#!/usr/bin/env python3

from sys import argv

with open(argv[1], 'r') as F:
    seq = F.readline().strip().upper()

counts = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}

for nt in seq:
    counts[nt] = counts[nt] + 1

print(counts['A'], counts['C'], counts['G'], counts['T'])

# Alternatively
A = seq.count('A');
C = seq.count('C');
G = seq.count('G');
T = seq.count('T');
print(A,C,G,T);