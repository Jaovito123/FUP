nome1 = input("Informe o primeiro nome: ")
nome2 = input("Informe o segundo nome: ")

tamanho1 = len(nome1)
tamanho2 = len(nome2)

diferenca = tamanho1 - tamanho2


dentro = nome1[diferenca:] 
print(nome2 in dentro)