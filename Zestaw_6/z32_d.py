def zad(tab, k, sum1=0, sum2=0, ile1=0, ile2=0, indeks=0):
    n = len(tab)
    if ile1 == k and ile2 == k:
        if sum1 == sum2:
            return True
        else:
            return False
    if indeks == n:
        return False

    return zad(tab, k, sum1, sum2, ile1, ile2, indeks + 1) or \
           zad(tab, k, sum1 + tab[indeks], sum2, ile1 + 1, ile2, indeks + 1) or \
           zad(tab, k, sum1, sum2 + tab[indeks], ile1, ile2 + 1, indeks + 1)


x = [2,4,3,7,3]
print(zad(x, 2))
