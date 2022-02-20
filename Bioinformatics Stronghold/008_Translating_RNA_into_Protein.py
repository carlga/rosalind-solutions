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
    path = os.path.join(path, os.pardir, 'Resources', 'codon_table.txt')
    path = os.path.abspath(path)
    codon_table = readDict(path)
    
    # Translate sequence
    print(translate(seq, codon_table))

def readDict(path):  
    with open(path, 'r') as F:
        codon_list = F.read().replace('\n', '\t').split('\t')

    codon_dict = dict(codon.split(' ') for codon in codon_list)
    return(codon_dict)

def translate(seq, codon_table):
    seq_list = [seq[i:i+3] for i in range(0, len(seq)-3, 3)]
    prot_list = [codon_table[codon] for codon in seq_list]
    prot_seq = ''.join(prot_list)
    return(prot_seq)

if __name__ == '__main__':
    main()