frase = input()
tamanho = len(frase)
novaFrase = ""
for i in range(tamanho - 1, -1, -1):
    if frase[i] != "a":
        if frase[i] != "A":
            novaFrase += frase[i]
        else:
            novaFrase += "*"
    else:
        novaFrase += "*"
print(novaFrase)