#!/usr/bin/env python3

from sys import exit, argv
import requests
import re

def main():
    if argv[1]:
        fileName = argv[1]
    else:
        exit("No file provided")

    with open(argv[1], 'r') as F:
        ids = F.read().splitlines()

    for id in ids:
        url = 'http://www.uniprot.org/uniprot/' + id + '.fasta'
        req = requests.get(url).text.splitlines()
        seq = ''.join([line for line in req if not line.startswith('>')])
        matches = re.finditer(r'(?=(N[^P](S|T)[^P]))', seq)
        positions = [ str(m.start()+1) for m in matches ]
        if positions:
            print(id)
            print(' '.join(positions))

if __name__ == '__main__':
    main()