#!/usr/bin/env python3

from sys import exit, argv

def main():
    if argv[1]:
        fileName = argv[1]
    else:
        exit("No file provided")

    with open(argv[1], 'r') as F:
        seq, motif = F.read().split('\n')[:2]
    
    # Find motif locations (1-based position)
    positions = [i+1 for i in range(len(seq)) if motif == seq[i:i+len(motif)]]
    print(' '.join(map(str, positions)))


if __name__ == '__main__':
    main()