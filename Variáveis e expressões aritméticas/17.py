valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
premio = float(input())

total = valor1 + valor2 + valor3

porcentagem1 = (valor1 * 100 / total) / 100
porcentagem2 = (valor2 * 100 / total) / 100
porcentagem3 = (valor3 * 100 / total) / 100

valorreceber1 = premio * porcentagem1
valorreceber2 = premio * porcentagem2
valorreceber3 = premio * porcentagem3

print(f"{valorreceber1:.2f} \n{valorreceber2:.2f} \n{valorreceber3:.2f}")