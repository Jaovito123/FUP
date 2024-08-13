indice = 1
menor = 1
maior = 1
while indice < 11:
    num = float(input())
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    indice += 1
print(f"{menor:.2f} \n{maior:.2f}")