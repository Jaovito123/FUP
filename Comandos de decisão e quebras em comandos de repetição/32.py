n1 = int(input())
n2 = int(input())
divisao = 0
if n1 > n2:
    divisao = int(n1 * (n2 ** -1))
else:
    divisao = int(n2 * (n1 ** -1))
print(divisao)
