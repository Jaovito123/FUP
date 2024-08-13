while True:
    num = int(input("Informe um número: "))
    if num % 2 == 1:
        print(f"O número {num} é impar.")
    else:
        print(f"O número {num} é par.")
    continuar = input("Deseja continuar? (sim/não) ").lower().strip()
    if continuar == "não" or continuar == "nao":
        print("FIM DO PROGRAMA.")
        break
