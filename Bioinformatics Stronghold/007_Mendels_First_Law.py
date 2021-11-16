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

    # Calculate probability of F1 with dominant phenotype
    probs = inheritProb(data[0], data[1], data[2])
    print('{:.5f}'.format(probs[0] + probs[1]))


def inheritProb(k,n,m):
    pop_n = k + n + m

    # Offspring n for F1 = C(P,2) * 4 (matings x F1 genotypes)
    f1_n = comb(pop_n, 2) * 4

    # Homozygous dominiant (AA) F1 offspring n
    AA_f1_n = 4*comb(k,2) + 2*k*n + comb(n,2)

    # Homozygous recessive (aa) F1 offspring n
    aa_f1_n = 4*comb(m,2) + 2*m*n + comb(n,2)

    # Heterozygous (Aa) F1 offspring n
    Aa_f1_n = f1_n - AA_f1_n - aa_f1_n
    # Aa_f1_n = 4*k*m + 2*comb(n,2) + 2*k*n + 2*n*m

    return([AA_f1_n/f1_n, Aa_f1_n/f1_n, aa_f1_n/f1_n])

if __name__ == '__main__':
    main()