import cmath
x = float(input())
y = float(input())

distancia = (x ** 2 + y ** 2)
raiz = cmath.sqrt(distancia)

print(f"{raiz.real:.2f}") 