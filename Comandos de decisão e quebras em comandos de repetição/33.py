num = int(input())
soma = 0
indice = 1
while indice < num:
    if num % indice == 0:
        soma += indice
    indice += 1
if soma == num:
    print("Perfeito")
else:
    print("Nao perfeito")
