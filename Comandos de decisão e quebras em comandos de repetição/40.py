frase = input()
tamanho = len(frase)
cont = 0
for i in range(tamanho):
    if frase[i] == "1":
        cont += 1
print(cont)