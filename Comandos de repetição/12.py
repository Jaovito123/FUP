from math import factorial


def funcao(n, k):
    fatorial_n = factorial(n)
    fatorial_k = factorial(k)
    nk = n - k
    fatorial_nk = factorial(nk)

    c = fatorial_n / (fatorial_k * fatorial_nk)
    return c
