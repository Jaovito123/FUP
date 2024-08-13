def funcao(n):
    cont = 0
    maior = 0
    for i in range(1, n+1):
        cont = 0
        for j in range(1, i+1):
            if i % j == 0:
                cont +=1
        if cont < 3:
            if n % i == 0:
                maior = i
    return maior