def funcao(x):
    resultado = ""
    for i in range(1, x+1):
        resultado += "*" * i + "\n"
    for i in range(x-1, 0, -1):
        resultado += "*" * i + "\n"
    return print(resultado)
