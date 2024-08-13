def funcao(frase, qnt):
    tamanho = len(frase)
    novafrase = ""
    for i in range(0, tamanho):
        letra = frase[i]
        if letra != " ":
            indiceletra = ord(letra)
            cont = indiceletra + qnt
            if cont > 90:
                conta = indiceletra + qnt - 90 + 64
                indiceletra = conta
            else:
                indiceletra += qnt
            novafrase += chr(indiceletra)
        else:
            novafrase += " "
    return (novafrase)
