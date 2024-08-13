def funcao(x):
    resultado = ""
    a = x - 1
    for i in range(1, x+1):
        resultado += a * " " + "*" * (i*2-1) + a * " " + "\n"
        a -= 1
    return resultado
print(funcao(5))