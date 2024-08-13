while True:
    print("1 - Adicao \n2 - Subtracao \n3 - Multiplicacao \n4 - Divisao \n5 - Saida ")
    indice = int(input())
    result = 0
    if indice == 1:
        n1 = float(input())
        n2 = float(input())
        result = n1 + n2
        print(f"{result:.2f}")
    elif indice == 2:
        n1 = float(input())
        n2 = float(input())
        result = n1 - n2
        print(f"{result:.2f}")
    elif indice == 3:
        n1 = float(input())
        n2 = float(input())
        result = n1 * n2
        print(f"{result:.2f}")
    elif indice == 4:
        n1 = float(input())
        n2 = float(input())
        result = n1 / n2
        print(f"{result:.2f}")
    elif indice == 5:
        break