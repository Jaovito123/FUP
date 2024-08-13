from math import factorial


def funcao(n):
    n1 = 1
    for i in range(1, n+1):
        fatorial_i = factorial(i)
        n1 = n1 + 1 / fatorial_i
    return n1
