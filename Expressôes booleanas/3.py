palavra = input()
caractere = input()
cont = 0
tamanho = len(palavra)
novapalavra = ""

for i in range(tamanho):
    letra = palavra[i]
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        cont += 1
        novapalavra += caractere
    else:
        novapalavra += letra
print(f"{cont} \n{novapalavra}")
