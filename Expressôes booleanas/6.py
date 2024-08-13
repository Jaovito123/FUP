idade = int(input())
tempotrabalhado = int(input())

if idade >= 65 or tempotrabalhado >= 30 or (idade >= 60 and tempotrabalhado >= 25):
    print("Pode se aposentar")
else:
    print("Nao pode se aposentar") 