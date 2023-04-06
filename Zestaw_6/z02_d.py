"""
”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.
"""


def wagi(x):
    ile = 0
    i = 2
    while x > 1:
        if x % i == 0:
            ile += 1
            while x % i == 0:
                x //= i
        i += 1
    return ile


def suma(t):
    sum = 0
    for x in t:
        sum += x
    return sum


def zad(tab, second=1, third=2):
    waga = [wagi(x) for x in tab]
    uno = suma(waga[:second])
    dos = suma(waga[second:third])
    tre = suma(waga[third:])
    if uno == dos and dos == tre:
        print(waga[:second], waga[second:third], waga[third:])
        return True
    if third == len(waga) - 1:
        if second == third - 1:
            return False
        return zad(tab, second + 1, second + 2)
    return zad(tab, second, third + 1)


v = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 1, 2*3*5, 2*3*5]
w = [1, 1, 1, 1, 2, 1, 1, 1,  2, 1, 0, 0]
print(zad(v))
