def funcao(frase1, frase2):
    tamanho1 = len(frase1)
    tamanho2 = len(frase2)
    result = True
    if tamanho1 >= tamanho2:
        maiorIgual = tamanho1
    elif tamanho1 < tamanho2:
        maiorIgual = tamanho2
    for i in range(maiorIgual):
        if frase1[i] == frase2[i]:
            result = True
        else:
            result = False
            break
    return result
