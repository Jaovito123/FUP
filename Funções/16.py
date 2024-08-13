def horas(temp):
    hor = temp // 3600
    resto = temp % 3600

    min = resto // 60
    resto = resto % 60

    seg = resto

    return hor, min, seg
