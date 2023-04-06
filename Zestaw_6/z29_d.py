import math


def odleglosc(a):
    x = a[0]
    y = a[1]
    z = a[2]
    odc = math.sqrt((math.sqrt(x ** 2 + y ** 2)) ** 2 + z ** 2)
    return odc


def srodek_ciezkosci(srodek, punkt, ile):
    for i in range(3):
        srodek[i] *= ile
        srodek[i] += punkt[i]
        srodek[i] /= (ile + 1)
    return srodek


def zad(tab, r, srodek=[0, 0, 0], ile=0, indeks=0):
    n = len(tab)
    print(ile, indeks, srodek)
    if ile > 2 and odleglosc(srodek) < r:
        return True
    elif indeks == n:
        return False
    else:
        return zad(tab, r, srodek, ile, indeks + 1) or \
               zad(tab, r, srodek_ciezkosci(srodek, tab[indeks], ile), ile + 1, indeks + 1)


d = [(2, 1, 1) for _ in range(3)]
print(zad(d, 2))
