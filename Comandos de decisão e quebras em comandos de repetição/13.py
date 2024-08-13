from math import sqrt
a = float(input())
b = float(input())
c = float(input())
if a != 0:
    delta = b ** 2 - 4 * a * c 
    if delta < 0:
        print("Nao existe raiz real")
    elif delta == 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        if x1 > 0:
            print(f"{x1:.2f} \nRaiz unica")
        else: 
            print(f"{x2:.2f} \n Raiz unica")
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(f"{x1:.2f} \n{x2:.2f}")
else:
    print("Nao eh equacao do 2o grau")