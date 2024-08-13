soma = 0
dividendo = 1
for i in range(1, 51):
    soma = soma + dividendo / i
    dividendo += 2
print(f"{soma:.10f}")
