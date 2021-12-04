#!/usr/bin/env python3

from sys import exit, argv
import re

def main():
    if argv[1]:
        fileName = argv[1]
    else:
        exit("No file provided")

    seqs = readFasta(fileName)

    # Find all shared motifs
    shared_motifs = findCommonSubstring(list(seqs.values()))
    # print('\n'.join(shared_motifs))
    print(shared_motifs[0])


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

def findCommonSubstring(seqs):
    common_substrings = []

    # Sort sequences in ascending order
    seqs.sort(key=len, reverse=False)

    # Get all substrings in shortest sequence
    n = len(seqs[0])
    substrings = [seqs[0][i:j] for i in range(n) for j in range(i+1, n+1)]
    substrings = sorted(set(substrings), key=len, reverse=True)

    # Find shared substrings
    for substring in substrings:
        common = True
        for seq in seqs[1:]:
            if substring not in seq:
                common = False
                break
        if common:
            common_substrings.append(substring)
    
    return(common_substrings)


if __name__ == '__main__':
    main()