#!/usr/bin/env python3

from sys import exit, argv

def main():
    if argv[1]:
        fileName = argv[1]
    else:
        exit("No file provided")

    with open(argv[1], 'r') as F:
        data = F.readline().strip().split(sep=" ")

    # Convert strings to ints
    data = [int(x) for x in data]

    # Set probabilities of dominiant offspring for genotype pairs
    # [AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa]
    probs = [1, 1, 1, 3/4, 1/2, 0]

    # Calculate expected value
    print(getExpectedValue(data, probs) * 2)


def getExpectedValue(values, probabilities):
    expected_value = sum([x*p for x,p in zip(values,probabilities)])

    return(expected_value)

if __name__ == '__main__':
    main()