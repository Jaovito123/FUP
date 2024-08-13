saque = int(input())
resto = 0

nota100 = saque // 100
resto = saque % 100

nota50 = resto // 50
resto = resto % 50

nota20 = resto // 20
resto = resto % 20

nota10 = resto // 10
resto = resto % 10

nota5 = resto // 5
resto = resto % 5

nota2 = resto // 2
resto = resto % 2

moeda1 = resto // 1

print(f"{nota100} \n{nota50} \n{nota20}")
print(f"{nota10} \n{nota5} \n{nota2} \n{moeda1}")