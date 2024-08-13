# Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. 
# O programa tem que retornar o maior e o menor número lido.

maior = 1
menor = 1
cont = 0
while True:  
    num = int(input())
    if num >= 0:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        cont += 1
    else:
        break
if cont >= 2:
    print(f"{maior} \n{menor}")
elif cont == 1:
    print(f"{maior} \n{maior}")
else:
    print()

# REFAZER