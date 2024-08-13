for i in range(1, 31):
    if i % 2 == 1:
        print("Impar")
    elif i % 4 == 0:
        print("Par e divisivel por 4")
    elif i % 2 == 0:
        print("Apenas par")
    else:
        print(i)
    