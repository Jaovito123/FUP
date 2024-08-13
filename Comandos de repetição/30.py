nome = input()
tamanho = len(nome)
for i in range(tamanho, 0, -1):
    print(nome[i-1], end="")
