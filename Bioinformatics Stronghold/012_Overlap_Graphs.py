#!/usr/bin/env python3

from sys import exit, argv
import re

def main():
    if argv[1]:
        fileName = argv[1]
    else:
        exit("No file provided")

    seqs = readFasta(fileName)
    k = 3

    edges = getAdjList(seqs, k)

    for edge in edges:
        print('{} {}'.format(edge[0], edge[1]))


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

def getAdjList(seqs_dict, k):
    adjacency_list = []

    for id1, seq1 in seqs_dict.items():
        for id2, seq2 in seqs_dict.items():
            if id1 != id2:
                if seq1[-k:] == seq2[:k]:
                    adjacency_list.append((id1, id2))
    
    return(adjacency_list)


if __name__ == '__main__':
    main()