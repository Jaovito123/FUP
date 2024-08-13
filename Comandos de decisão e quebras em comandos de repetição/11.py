n1 = float(input())
sinal = input()
n2 = float(input())
result = 0

if sinal == "+":
    result = n1 + n2
elif sinal == "-":
    result = n1 - n2
elif sinal == "*":
    result = n1 * n2
elif sinal == "/":
    result = n1 / n2
else:
    print("Erro")

print(f"{result:.2f}")
