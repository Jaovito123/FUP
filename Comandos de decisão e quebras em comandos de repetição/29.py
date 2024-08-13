num =int(input())
cont = 0
indice = 1
while indice < num +1:
    if num % indice == 0: 
        cont = cont + 1
    indice += 1
if num != 1:
    if cont > 2:
        print("Nao primo")
    else: 
        print("Primo")
else:
    print("Nao primo")