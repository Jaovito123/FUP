def inverter(num):
    n1 = num % 10
    resto = num // 10

    n2 = resto % 10
    resto = resto // 10

    n3 = resto % 10

    numero_final = n1 * 100 + n2 * 10 + n3

    return numero_final
