frase = input()
nova_frase = ""
tamanho = len(frase)
for i in range(tamanho):
    if frase[i] == "0":
        nova_frase += "1"
    else:
        nova_frase += frase[i]
print(nova_frase)