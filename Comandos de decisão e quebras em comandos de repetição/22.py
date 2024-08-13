def funcao(nota1, nota2, nota3, letra):
    ponderacao = 0
    if letra == "A":
        return (nota1 + nota2 + nota3) / 3
    else:
        ponderacao = (nota1 * 5) + (nota2 * 3) + (nota3 * 2)
        return ponderacao / 10
