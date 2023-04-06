import math

liczba = int(input("wpisz: "))

x = 1
while x <= math.sqrt(liczba):
    if liczba%x == 0:
        print(str(x) + " " + str(liczba//x))
    x += 1