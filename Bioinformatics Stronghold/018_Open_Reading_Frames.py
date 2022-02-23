#!/usr/bin/env python3

import os
import re
from sys import exit, argv

def main():
    if argv[1]:
        fileName = argv[1]
    else:
        exit("No file provided")
    
    # Read sequences from fasta file
    sequences = readFasta(fileName)

    # Load genetic code (with Us)
    path = os.getcwd()  # or os.path.dirname('__file__')
    path = os.path.join(path, 'Resources', 'codon_table.txt')
    path = os.path.abspath(path)
    codon_table = readDict(path)

    # find open reading frames
    for seq in sequences.values():
        proteins = findORFs(seq, genetic_code=codon_table)

    # output uniqued translated ORFs
    print('\n'.join(set(proteins)))


def readFasta(fileName):
    sequences = {}

    with open(fileName, 'r') as F:
        seq = []
        for line in F:

            if re.match(r'^\s*$', line):
                continue

            if line.startswith('>'):
                if seq:
                    sequences[header] = ''.join(seq)
                seq = []
                header = line.strip()[1:]
                if header in sequences:
                    exit("Duplicated entries in file: {}".format(header))
            else:
                if not header:
                    continue
                seq.append(line.strip().upper())
        
        # Store last sequence in file
        sequences[header] = ''.join(seq)
    
    return(sequences)

def readDict(path):  
    with open(path, 'r') as F:
        codon_list = F.read().replace('\n', '\t').split('\t')

    codon_dict = dict(codon.split(' ') for codon in codon_list)
    return(codon_dict)

def findORFs(seq, frames=['+1','+2','+3','-1','-2','-3'], minimum_length=0, genetic_code={}):
    if not genetic_code:
        exit("Please provide genetic code as input to findORFs.")
    start_codons = ('AUG')
    stop_codons = ('UAG', 'UGA', 'UAA')
    proteins = []

    # search ORFs in different frames
    for frame in frames:
        dna = seq
        start = None
        aa_list = []

        # reverse complement sequence for negative frames
        if frame.startswith('-'):
            dna = reverse_complement(dna)
        
        # set Ts to Us
        dna = dna.translate(str.maketrans('T','U'))
        
        i = int(frame[1])-1
        while i < len(seq)-2:
            codon = dna[i:i+3]

            # start
            if codon in start_codons and start == None:
                start = i
                aa_list.append(genetic_code[codon])

            # extend
            elif codon not in stop_codons and start != None:
                aa_list.append(genetic_code[codon])

            # stop
            elif codon in stop_codons and start != None:          
                # check ORF length
                stop = i + 2
                orf_length = stop - start + 1
                if orf_length > minimum_length:             
                    proteins.append(''.join(aa_list))
                # reset
                i = start # considers nested ORFs
                start = None
                aa_list = []
            
            i += 3

    return(proteins)

def reverse_complement(string):
    return(string[::-1].translate(str.maketrans('ATGC','TACG')))


if __name__ == '__main__':
    main()