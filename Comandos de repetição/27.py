def funcao(n):
    result = 1
    for i in range(2, n+1):
        result = i ** result
    return result
