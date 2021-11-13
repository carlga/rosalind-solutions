#!/usr/bin/env python3

from sys import exit, argv

def main():
    if argv[1]:
        fileName = argv[1]
    else:
        exit("No file provided")

    with open(argv[1], 'r') as F:
        sequences = F.read().upper().split('\n')

    print(hammingDist(sequences[0], sequences[1]))


def hammingDist(seq1, seq2):
    diff = 0
    for nt1, nt2 in zip(seq1, seq2):
        if nt1 != nt2:
            diff += 1
    return(diff)


if __name__ == '__main__':
    main()