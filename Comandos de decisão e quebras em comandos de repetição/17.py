from math import sqrt
def funcao(n):
    quadrado = n ** 2
    cubo = n ** 3
    raiz = sqrt(n)
    return quadrado, cubo, raiz

teste = 0
while teste == 0:
    num = int(input())
    if num <= 0:
        teste = 1
    else:
        x1, x2, x3 = funcao(num)
        print(f"{x1:.2f} \n{x2:.2f} \n{x3:.2f}")
    