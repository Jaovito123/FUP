from math import sqrt
num = float(input())
if num <= 0:
    print("Numero invalido")
else:
    raiz = sqrt(num)
    print(f"{raiz:.2f}")
    