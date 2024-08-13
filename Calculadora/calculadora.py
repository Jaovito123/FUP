from os import system
from time import sleep
import funcoes


while True:
    print("---CALCULADORA--- \n\n")
    print("""
Informe qual opção deseja seguir
    1- Calculos básicos
    2- IMC
    3- Verificar se um número é primo
    4- Bhaskara 
    5- Sair
""", end="")
    indice = int(input())
    sleep(1.5)
    system('cls')

    match indice:
        case 1:
            print("---Calculos Matemáticos--- \n\n")
            print("""
    1- Adicão
    2- Subtração
    3- Multiplicaçao
    4- Divisão
    5- Exponenciação
""", end="")
            indice_2 = int(input())
            sleep(2)
            system('cls')

            match indice_2:
                case 1:
                    funcoes.soma()
                case 2:
                    funcoes.subtracao()
                case 3:
                    funcoes.multiplicacao()
                case 4:
                    funcoes.divisao()
                case 5:
                    funcoes.exponeciacao()
                case _:
                    print("ERRO: Indice não encontrado.")
                    sleep(1.5)
                    system('cls')
        case 2:
            funcoes.imc()
        case 3:
            funcoes.primo()
        case 4:
            funcoes.baskara()
        case 5:
            print("Calculadora encerrada.")
            sleep(2)
            break
        case _:
            print("ERRO: Indice não encontrado.")
            sleep(1.5)
            system('cls')
