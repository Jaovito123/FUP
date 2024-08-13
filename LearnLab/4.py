num = int(input("Digite um número: "))
conta = 0
for i in range(0, 11):
    conta = i * num
    print(f"{num} x {i} = {conta}")