indice = int(input())
cont = 0
maior = 0
i = indice
while indice > 0:
    num = int(input())
    if i == indice:
        maior = num
    if num > maior:
        maior = num
        cont = 0
    if num == maior:
        cont += 1
    indice -= 1
print(f"{maior} \n{cont}")
