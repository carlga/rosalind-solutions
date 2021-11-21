#!/usr/bin/env python3

from sys import exit, argv
import re
import numpy as np

def main():
    if argv[1]:
        fileName = argv[1]
    else:
        exit("No file provided")

    seqs = readFasta(fileName)
    
    profile_mtx = getProfile(list(seqs.values()))
    cons_seq = getConsensus(profile_mtx)
    print(cons_seq)
    print2DMtx(profile_mtx, row_names=('A', 'C', 'G', 'T'))


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

def getProfile(seqs, nt_order = ('A', 'C', 'G', 'T')):
    pos_n = len(seqs[0])
    count_mtx = np.zeros(shape=[len(nt_order), pos_n], dtype=int)

    for j in range(pos_n):
        pos_nts = [seq[j] for seq in seqs]
        for i, nt in enumerate(nt_order):
            count_mtx[i][j] = pos_nts.count(nt)
    
    return(count_mtx)

def print2DMtx(mtx, row_names):
    for i in range(mtx.shape[0]):
        if row_names:
            print('{}: {}'.format(row_names[i], ' '.join(str(x) for x in mtx[i])))
        else:
            print(' '.join(str(x) for x in mtx[i]))

# Follows priority A>C>G>T when counts are the same for several nts
def getConsensus(profile, nt_order = ('A', 'C', 'G', 'T')):
    cons_seq = []

    for j in range(profile.shape[1]):
        pos_counts = [profile[i][j] for i in range(len(nt_order))]
        cons_nt = nt_order[pos_counts.index(max(pos_counts))]
        cons_seq.append(cons_nt)
    cons_seq = ''.join(cons_seq)

    return(cons_seq)


if __name__ == '__main__':
    main()