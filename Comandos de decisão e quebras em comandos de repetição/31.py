n1 = int(input())
n2 = int(input())
soma = 0
mult = 1
inicio = 0
fim = 0
if n1 < n2:
    inicio = n1
    fim = n2
else: 
    inicio = n2
    fim = n1
cont = inicio
while cont <= fim:
    if cont % 2 == 0:
        soma += cont
    else:
        mult *= cont
    cont += 1
print(f"{soma} \n{mult}")