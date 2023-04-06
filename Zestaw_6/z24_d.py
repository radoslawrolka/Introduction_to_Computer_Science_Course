import math


def odleglosc(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def srodek_c(a, b):
    return (a[0]+b[0])/2, (a[1]+b[1])/2


def zad(tab, uno=None, dos=None, tre=None, qua=None, indeks=0, ile=0):
    # print(uno, dos, tre, qua)
    n = len(tab)
    if uno is not None and dos is not None and tre is not None and qua is not None:
        print(uno, dos, tre, qua)
        return odleglosc(srodek_c(uno, dos), srodek_c(tre, qua))
    if indeks == n or ile == 4:
        return float('inf')
    return min(zad(tab, uno, dos, tre, qua, indeks+1, ile),
               zad(tab, tab[indeks], dos, tre, qua, indeks+1, ile+1),
               zad(tab, uno, tab[indeks], tre, qua, indeks+1, ile+1),
               zad(tab, uno, dos, tab[indeks], qua, indeks+1, ile+1),
               zad(tab, uno, dos, tre, tab[indeks], indeks+1, ile+1))


x = [(1, 1), (3, 3), (10, 10), (0, 0)]
print(zad(x))
