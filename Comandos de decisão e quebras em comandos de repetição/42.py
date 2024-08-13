frase = input()
tamanho = len(frase)
cont = 0
for i in range(tamanho):
    if frase[i] == " ":
        cont += 1
print(cont)