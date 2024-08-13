import math
pi = math.pi


def volumearea(raio):
    volume = 4 * pi * raio ** 3 / 3
    area = 4 * pi * raio ** 2
    return volume, area
