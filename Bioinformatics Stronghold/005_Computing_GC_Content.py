#!/usr/bin/env python3

import re
from sys import exit, argv

def main():
    if argv[1]:
        fileName = argv[1]
    else:
        exit("No file provided")
    
    # Read sequences from fasta file
    sequences = readFasta(fileName)

    # Retrieve sequence with highest GC%
    topGC = 0
    for key in sequences.keys():
        GC = contentGC(sequences[key], 1, 1)
        if GC > topGC:
            topHeader = key
            topGC = GC

    print("{}\n{:.6f}".format(topHeader, topGC))


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

def contentGC(seq, step, window):
    if step > window:
        exit("Step size cannot be greater than window")
    
    # Whole sequence %GC with step = 1 & window = 1
    if step == 1 & window == 1:
        return(len(re.findall(r'[GC]', seq)) / len(seq) * 100)
    
    # Otherwise returns array with sliding window GC%
    else:
        GC = []
        for i in range(0, len(seq), step):
            frag = seq[i:i+step]
            GC.append(len(re.findall(r'[GC]', seq)) / len(seq) * 100)
        return(GC)
        

if __name__ == '__main__':
    main()