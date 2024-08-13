salario = float(input())
prestacao = float(input())
conta = salario * 0.20
if prestacao > conta:
    print("Emprestimo nao concedido")
else:
    print("Emprestimo concedido")