import math

def dzielniki(liczba):
    x = 2
    suma = 1
    while x <= math.sqrt(liczba):
        if liczba % x == 0:
            suma += x + (liczba//x)
        x += 1
    return suma

x = 1
while x < 1000001:
    sumx = dzielniki(x)
    if sumx > x:
        if sumx < 1000000:
            if dzielniki(sumx) == x:
                print(str(x) + " " + str(sumx))
    x += 1