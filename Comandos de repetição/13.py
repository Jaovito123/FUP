def funcao(n):
    n1 = 1
    n2 = 1
    n3 = 1
    for i in range(1, n-1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n3
