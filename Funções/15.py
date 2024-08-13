def separa(num):
    n1 = num % 10
    resto = num // 10

    n2 = resto % 10
    resto = resto // 10

    n3 = resto % 10
    resto = resto // 10

    n4 = resto % 10

    return n1, n2, n3, n4
