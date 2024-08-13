def funcao(n):
    soma = 0
    for i in range(1, n + 1):
        num = i ** 2 + 1
        den = i + 3
        termo = num / den
        soma += termo
    return soma
