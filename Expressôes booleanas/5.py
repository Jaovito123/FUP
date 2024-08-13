a = float(input())
b = float(input())
c = float(input())

if (a + b < c) or (a + c < b) or (b + c < a):
    print("Nao triangulo")
else:
    if a == b and a == c:
        print("Triangulo equilatero")
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")