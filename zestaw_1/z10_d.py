import math
for liczba in range(1000000):
    x = 2
    suma = 1
    while x <= math.sqrt(liczba):
        if liczba%x == 0:
            suma += x + liczba//x
        x += 1

    if suma == liczba:
        print(liczba)