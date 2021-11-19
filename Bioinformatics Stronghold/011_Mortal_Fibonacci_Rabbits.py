#!/usr/bin/env python3

from sys import exit, argv

def main():
    with open(argv[1], 'r') as F:
        n,m = map(int, F.readline().strip().split(sep=" "))

    # print(fib1(n, m, 1, 2))
    print(fib2(n, m, 1, 2)[-1])


# Recursive approach is quite slow for large numbers
def fib1(n, m, k, g):
    if n == 0:
        return 0

    elif n < g:
        return 1
    
    # Fn = Fn-1 + F(n-g)*k before F0 dies
    elif n <= m:
        return fib1(n-1,m,k,g) + fib1(n-g,m,k,g)*k
    
    # Fn = Fn-1 + F(n-g)*k - 1 when F0 dies
    elif n == m+1:
        return fib1(n-1,m,k,g) + fib1(n-g,m,k,g)*k - 1
    
    # Fn = Fn-1 + F(n-g)*k - Fn-(n-m-1) after F0 dies
    else:
        return fib1(n-1,m,k,g) + fib1(n-g,m,k,g)*k - fib1(n-m-1,m,k,g)

# Faster alternative
def fib2(n, m, k, g):
    generations = []
    i = 0
    while i < n:
        if i < g:
            generations.append(1)
        elif i < m:
            generations.append(generations[i-1] + generations[i-g]*k)
        elif i <= m+1:
            generations.append(generations[i-1] + generations[i-g]*k - 1)
        else:
            generations.append(generations[i-1] + generations[i-g]*k - generations[i-m-1])
        i += 1
    return generations

if __name__ == '__main__':
    main()