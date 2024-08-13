temp = int(input())

hor = temp // 3600
resto = temp % 3600

min = resto // 60
resto = resto % 60

seg = resto

print(f"{hor}\n{min} \n{seg}")

