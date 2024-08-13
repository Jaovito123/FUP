def proporcao(valor1, valor2, valor3, premio):
    total = valor1 + valor2 + valor3

    porcentagem1 = (valor1 * 100 / total) / 100
    porcentagem2 = (valor2 * 100 / total) / 100
    porcentagem3 = (valor3 * 100 / total) / 100

    valorreceber1 = premio * porcentagem1
    valorreceber2 = premio * porcentagem2
    valorreceber3 = premio * porcentagem3

    return valorreceber1, valorreceber2, valorreceber3
