num1 = float(input())
num2 = float(input())
indice = int(input())

if indice == 1:
    media = (num1 + num2 ) / 2
    print(f"{media:.2f}")
elif indice == 2:
    if num1 > num2:
        diferenca = num1 - num2
        print(f"{diferenca:.2f}")
    else:
        diferenca = num2 - num1
        print(f"{diferenca:.2f}")
elif indice == 3: 
    produto = num1 * num2
    print(f"{produto:.2f}")
elif indice == 4:
    if num2 != 0:
        divisao = num1 / num2
        print(f"{divisao:.2f}")
    else:
        print("Erro")
else:
    print("Erro")
