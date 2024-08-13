indice = 1
soma = 0
while indice < 11:
    num = int(input())
    if num > 0:
        soma += num
        indice += 1
media = soma / 10
print(f"{media:.2f}")