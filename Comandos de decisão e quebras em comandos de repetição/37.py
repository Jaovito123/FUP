# Faça uma função chamada de simplificada que receba como parâmetro o numerador e o denominador de uma fração.
# Esta função deve simplificar a fração recebida dividindo o numerador e denominador pelo maior fator
# possível. Por exemplo, a fração 36/60 simplificada para 3/5 dividindo o numerador e denominador por 12.

def simplificar(n, d):
    cont_n = 0
    maior_n = 0
    for i in range(1, n+1):
        cont_n = 0
        for j in range(1, i+1):
            if i % j == 0:
                cont_n += 1
        if cont_n < 3:
            if n % i == 0:
                maior_n = i

    cont_m = 0
    maior_m = 0
    for i in range(1, d+1):
        cont_m = 0
        for j in range(1, i+1):
            if i % j == 0:
                cont_m += 1
        if cont_m < 3:
            if d % i == 0:
                maior_m = i

    return maior_n, maior_m



print(simplificar(36, 60))
 