peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
divisor = altura * altura
imc = peso / divisor
print(f"Seu IMC é {imc:.2f}")
if imc < 18.5 :
    print("Você está abixo do peso! ")
elif imc >= 18.5 and imc < 25:
    print("Você está no peso normal! ")
elif imc >= 25 and imc < 30:
    print("voce está no soobrepeso! ")
else:
    print("Você está na obesidade classe I!")