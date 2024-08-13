soma = 0
media = 0
for i in range(0, 3):
    nota = float(input())
    if nota >=0:
        if nota<=10:
            soma += nota
        else:
            print("Nota invalida")
            break
    else:
        print("Nota invalida")
        break
    if i == 2:
        media = soma/3
        print(f"{media:.2f}")
 