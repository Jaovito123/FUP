palavra = input()
nova_palavra = ""

for i, letra in enumerate(palavra):
    letra = ord(letra)
    letra += 1
    palavraFinal = chr(letra)
    nova_palavra += palavraFinal


print(nova_palavra)
