"""
1000 até o 9999 que faça isso

teste = 2025
novo = teste % 100
teste = teste // 100
print(novo, teste)
soma = teste + novo
elevar = soma ** 2
print(elevar)

vou criar um laço que percorra do 1000 até 9999, e toda vez que ele troca o valor em 1, eu faço 
a formula que está acima, segundo essa lógica, posso criar esse algoritmo com um for,
criando 3 variaveis especificas, 1 para armazenar o resto da divisão, 1 para armazenar a divisão inteira
e a outra podendo tanto fazer a soma dessas variaveis quanto elevar a soma delas ao quadrado.
por ultimo eu faço uma comparação para verificar se o resultado final é igual ao numero inicial(indice)
"""

for i in range(1000, 9999):
    final_do_numero = i % 100
    inicio_do_numero = i // 100
    resultado = inicio_do_numero + final_do_numero
    resultado **= 2
    if resultado == i:
        print(i)
