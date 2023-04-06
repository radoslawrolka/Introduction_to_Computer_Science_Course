def dzielniki(x):
    i = 2
    org = x
    t = []
    while x > 1 and i < org:
        if x % i == 0:
            t.append(i)
            while x % i == 0:
                x //= i
        i += 1
    return t


def top(tab):
    n = len(tab)
    for i in range(n):
        tab[i] = dzielniki(tab[i])

    def zad(tab, ile=0, indeks=0):
        if indeks == n - 1:
            return ile
        elif indeks >= n:
            return -1
        elif not tab[indeks]:
            return -1
        else:
            for dziel in tab[indeks]:
                if zad(tab, ile + 1, indeks + dziel) != -1:
                    return zad(tab, ile + 1, indeks + dziel)
        return -1

    return zad(tab)


x = [6, 6, 11, 6, 43, 11, 6, 11, 11, 11]
print(top(x))
