def zad11(tab, n, ilo, iloczyn=1, ile=0, indeks=0):
    if ile == n:
        if iloczyn == ilo:
            return 1
        else:
            return 0
    if indeks == len(tab):
        return 0
    else:
        return zad11(tab, n, ilo,  iloczyn, ile, indeks+1) + zad11(tab, n, ilo, iloczyn*tab[indeks], ile+1, indeks+1)


def zad(tab, iloc):
    maks = 0
    nka = 0
    for i in range(1, len(tab)):
        x = zad11(tab, i, iloc)
        if maks < x:
            maks = x
            nka = i
    return maks, nka


x = [2,2,2,2,2]
print(zad(x, 8))
