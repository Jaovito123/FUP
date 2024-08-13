import cmath


def distancia(x, y):
    distancia = (x ** 2 + y ** 2)
    raiz = cmath.sqrt(distancia)
    return raiz.real
