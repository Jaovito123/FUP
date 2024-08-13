num = int(input())
indice = 1
while indice < num + 1:
    if num % indice == 0:
        print(indice)
    indice += 1