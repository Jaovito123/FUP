# esperado: 233168

soma = 0
for i in range(1000):
    valor = i * 3
    valor2 = i * 5
    valor3 = i * 15

    if valor < 1000:
        soma += valor
    if valor2 < 1000:
        soma += valor2
    if valor3 < 1000:
        soma -= valor3

print(soma)
