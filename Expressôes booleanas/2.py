nome = input()
tamanho = len(nome)
novonome = ""
for i in range(tamanho):
    letra = nome[i]
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        novonome += ""
    else:
        novonome += letra
print(novonome)
