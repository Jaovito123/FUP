from math import factorial


def funcao(x, n):
    teste = 0
    for i in range(0, n+1):
        final = (-1)**i * (x**(2 * i + 1)) / factorial(2 * i + 1)
        teste += final
    return teste
