def bin(x):
    jedynki = 0
    while x>0:
        if x%2 == 1:
            jedynki += 1
        x //= 2
    return jedynki


def zad(tab, org=1, ile1= 0, ile2=0, ile3=0, indeks=0, x=""):
    n = len(tab)
    if org:
        org = 0
        for i in range(n):
            tab[i] = bin(tab[i])

    if indeks == n:
        if ile1 == ile2 and ile1 == ile3:
            return True
        else:
            return False

    return zad(tab, 0, ile1+tab[indeks], ile2, ile3, indeks+1, x+"l") or \
           zad(tab, 0, ile1, ile2+tab[indeks], ile3, indeks+1, x+"s") or \
           zad(tab, 0, ile1, ile2, ile3+tab[indeks], indeks+1, x+"p")

dupa = [5,7,15]
print(zad(dupa))