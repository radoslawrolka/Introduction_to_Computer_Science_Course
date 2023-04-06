def sum_sqr(a):
    return abs(a[1] - a[0]) * abs(a[3] - a[2])


# TO DO
def nachodzi(tab):
    n = len(tab)
    """
    for i in range(n):
        for j in range(i+1,n):
            if tab[i][0] < tab[j][1] and tab[i][1] > tab[j][0]:
                return False
            """


def zad(tab, suma=0, ile=0, indeks=0, ktore=[]):
    n = len(tab)
    if ile == 13:
        if suma == 2012:
            return True
        return False
    if suma > 2011 or indeks == n:
        return False
    if nachodzi(ktore):
        return False

    return zad(tab, suma, ile, indeks + 1, ktore) or \
           zad(tab, suma + sum_sqr(tab[indeks]), ile + 1, indeks + 1, ktore + tab[indeks])


T = [(1, 2, 3, 4) for i in range(100)]
zad(T)
