pessoas = int(input("Quantas pessoas deseja calcular o imc? "))
dados = []
dados2 = []
calculo = 0
for i in range(0, pessoas):
    altura = float(input("Informe sua altura: "))
    peso = float(input("Informe seu peso: "))
    calculo = altura ** 2
    calculo = peso / calculo
    dados.append(calculo)

    if dados[i] < 18.5:
        dados2.append("Abaixo do peso! ")
    elif dados[i] >= 18.5 and dados[i] < 25:
        dados2.append("Peso normal! ")
    elif dados[i] >= 25 and dados[i] < 30:
        dados2.append("Sobrepeso! ")
    elif dados[i] >= 30 and dados[i] < 35:
        dados2.append("Obesidade grau I! ")
    elif dados[i] >= 35 and dados[i] < 40:
        dados2.append("Obesidade grau II (Severa)! ")
    else:
        dados2.append("Obesidade grau III (Morbida)! ")
tam = len(dados)
for i in range(tam):
    pessoa = i + 1
    print(f"Pessoa {pessoa} tem o IMC de {
        dados[i]:.2f} e está com {dados2[i]}")
