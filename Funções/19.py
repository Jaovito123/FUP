def cedulas(saque):
    nota100 = saque // 100
    resto = saque % 100

    nota50 = resto // 50
    resto = resto % 50

    nota20 = resto // 20
    resto = resto % 20

    nota10 = resto // 10
    resto = resto % 10

    nota5 = resto // 5
    resto = resto % 5

    nota2 = resto // 2
    resto = resto % 2

    moeda1 = resto // 1

    return nota100, nota50, nota20, nota10, nota5, nota2, moeda1
