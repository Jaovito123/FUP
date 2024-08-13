def funcao(n, m):
    a = n
    b = m
    while b != 0:
        a, b = b, a % b
    
    result = (n * m) // a
    result = abs(result)
    return result