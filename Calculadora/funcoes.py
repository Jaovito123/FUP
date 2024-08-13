import cmath
from os import system
from time import sleep


def soma():
    print("Digite os números que deseja somar: ")
    n1 = float(input())
    n2 = float(input())
    soma = n1 + n2
    print(f"{n1:.2f} + {n2:.2f} = {soma:.2f}")
    sleep(3)
    system('cls')


def subtracao():
    print("Digite os números que deseja subtrair: ")
    n1 = float(input())
    n2 = float(input())
    sub = n1 - n2
    print(f"{n1:.2f} - {n2:.2f} = {sub:.2f}")
    sleep(3)
    system('cls')


def multiplicacao():
    print("Digite os números que deseja multiplicar: ")
    n1 = float(input())
    n2 = float(input())
    mult = n1 * n2
    print(f"{n1:.2f} x {n2:.2f} = {mult:.2f}")
    sleep(3)
    system('cls')


def divisao():
    print("Digite os números que deseja dividir: ")
    n1 = float(input())
    n2 = float(input())
    divi = n1 / n2
    print(f"{n1:.2f} / {n2:.2f} = {divi:.2f}")
    sleep(3)
    system('cls')


def exponeciacao():
    print("Digite a base e seu expoente: ")
    n1 = float(input())
    n2 = float(input())
    soma = n1 ** n2
    print(f"{n1:.2f} ^ {n2:.2f} = {soma:.2f}")
    sleep(3)
    system('cls')


def imc():
    print("Informe sua altura e peso consecultivamente: ")
    x1 = float(input())
    x2 = float(input())
    x1 **= 2
    imc = x2 / x1
    print(f"{imc:.2f}")
    sleep(3)
    system('cls')


def primo():
    num = int(input("Informe o número que deseja verificar se é primo: \n"))
    cont = 0
    for i in range(1, num):
        if num % i == 0:
            cont += 1
    if cont > 2:
        print("Não é primo.")
    else:
        print("É primo.")
    sleep(3)
    system('cls')


def baskara():
    print("Informe A, B e C consecultivamente: ")
    a = int(input())
    b = int(input())
    c = int(input())
    delta = b**2 - 4 * a * c
    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
    print(f"X1 = {x1.real:.2f} \nX2 = {x2.real:.2f}")
    sleep(3)
    system('cls')
