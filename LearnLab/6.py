lista = ["batata", "limao", "Arroz"]
while True:
    q1 = input("Deseja adicionar algum item? (Sim/Não)").strip().lower()
    if q1 == "sim":
        lista.append(input("Adicione um item a sua lista: "))
    
    q2 = input("Deseja remover algum item? (Sim/Não)").strip().lower()
    if q2 == "sim":
        remover = input("Remova um item da sua lista: ")
        lista.remove(remover)
    
    q3 = input("Deseja atualizar um item da sua lista? (Sim/Não)").strip().lower()
    if q3 == "sim":
        trocar1 = input("Qual item deseja remover? ").strip().lower()
        trocar2 = input("qual item deseja adicionar? ").strip().lower()
        # . . . 
    tamanho = len(lista)
    for i in range(0, tamanho): 
        print(lista[i], end=" ")
    
    q4 = input("\nDeseja encerra a lista? (Sim/Não)")
    if q4 == "sim":
        break
