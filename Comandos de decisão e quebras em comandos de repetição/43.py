nomeVelho = input()
idadeVelha = int(input())
nomeNovo = nomeVelho
idadeNova = idadeVelha

while True:
    nome = input()
    idade = int(input())
    if idade < 0:
        break
    if idade < idadeNova:
        idadeNova = idade
        nomeNovo = nome
    if idade > idadeVelha:
        idadeVelha = idade
        nomeVelho = nome
print(f"{nomeNovo} \n{idadeNova} \n{nomeVelho} \n{idadeVelha}")
