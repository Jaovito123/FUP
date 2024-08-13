quantidade = int(input())
indice = 1
num0 = float(input())
menor = num0
maior = num0
while indice < quantidade:
    num = float(input())
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    indice += 1
print(f"{menor:.2f} \n{maior:.2f}")