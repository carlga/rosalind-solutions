#!/usr/bin/env python3

import os
from sys import exit, argv

def main():
    if argv[1]:
        fileName = argv[1]
    else:
        exit("No file provided")

    with open(argv[1], 'r') as F:
        seq = F.readline().strip().upper()

    # Load genetic code (with Us)
    path = os.getcwd()  # or os.path.dirname('__file__')
    path = os.path.join(path, 'Resources', 'codon_table.txt')
    path = os.path.abspath(path)
    codon_table = readDict(path)
    
    # Count codons per amino acid
    codon_counts = {}
    for aa in codon_table.values():
        if not aa in codon_counts:
            codon_counts[aa] = 1
        else:
            codon_counts[aa] += 1
    
    # Total RNA strings % 1e6
    total = 1
    for aa in  seq:
        total *= codon_counts[aa]
    total *= 3 # stop codons

    print(total % 1000000)

def readDict(path):  
    with open(path, 'r') as F:
        codon_list = F.read().replace('\n', '\t').split('\t')

    codon_dict = dict(codon.split(' ') for codon in codon_list)
    return(codon_dict)


if __name__ == '__main__':
    main()