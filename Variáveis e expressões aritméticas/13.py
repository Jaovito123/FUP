numero = int(input())

num1 = numero % 10
numero = numero // 10

num2 = (numero % 10)
numero = numero // 10

num3 = (numero % 10) 
numero = numero // 10

print(f"{num1:.0f}{num2:.0f}{num3:.0f}")