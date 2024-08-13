from math import factorial
from math import log10


def funcao(p):
    fatorial = factorial(p)
    indice = log10(fatorial)
    indice = int(indice // 1)
    soma = 0
    for i in range(0, indice+1):
        n1 = fatorial % 10
        soma += n1
        fatorial //= 10
    return soma
