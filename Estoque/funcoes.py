lista_tipo = []
lista_nome = []
lista_quantidade = []


def adicionar(tipo, nome, quantidade):

    lista_tipo.append(tipo)
    lista_nome.append(nome)
    lista_quantidade.append(quantidade)
    return lista_tipo, lista_nome, lista_quantidade


def remover(tipo, nome, quantidade):
    lista_tipo.remove(tipo)
    lista_nome.remove(nome)
    lista_quantidade.remove(quantidade)
    return lista_tipo, lista_nome, lista_quantidade


def verificar_itens():
    indice = len(lista_tipo)
    for i in range(indice):
        print(lista_tipo[i], end=" ")
        print(lista_nome[i], end=" ")
        print(lista_quantidade[i], end=" ")
        print()
