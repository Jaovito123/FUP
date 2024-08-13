n1 = int(input())
n2 = int(input())
n3 = int(input())
maior = 0
meio = 0
menor = 0

# n1 o menor número
if n1 < n2:
    if n1 < n3:
        if n2 < n3:
            menor = n1
            meio = n2
            maior = n3
        else:
            menor = n1
            meio = n3
            maior = n2

# n2 o menor número
if n2 < n1:
    if n2 < n3:
        if n1 < n3:
            menor = n2
            meio = n1
            maior = n3
        else:
            menor = n2
            meio = n3
            maior = n1
# n3 o menor número
if n3 < n1:
    if n3 < n2:
        if n1 < n2:
            menor = n3
            meio = n1
            maior = n2
        else:
            menor = n3
            meio = n2
            maior = n1

# Os trÊs números são iguais
if n1 == n2:
    if n1 == n3:
        menor = n1
        meio = n2
        maior = n3

# n1 e n2 são iguais
if n1 == n2:
    if n1 != n3:
        if n1 < n3:
            menor = n1
            meio = n2
            maior = n3
        else:
            menor = n3
            meio = n2
            maior = n1

# n1 e n3 são iguais
if n1 == n3:
    if n1 != n2:
        if n1 < n2:
            menor = n1
            meio = n3
            maior = n2
        else:
            menor = n2
            meio = n1
            maior = n3

# n2 e n3 são iguais
if n2 == n3:
    if n2 != n1:
        if n2 < n1:
            menor = n3
            meio = n2
            maior = n1
        else:
            menor = n1
            meio = n2
            maior = n3

print(f"{menor} \n{meio} \n{maior}")
