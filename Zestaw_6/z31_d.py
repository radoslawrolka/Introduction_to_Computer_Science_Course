def na_czynniki(x):
    tab = []
    i = 2
    while x > 1:
        if x % i == 0:
            tab.append(i)
            while x % i == 0:
                x //= i
        i += 1
    return tab


def zad(x):
    tabs = na_czynniki(x)
    n = len(tabs)
    print(x, "->", tabs)
    suma = 0

    def licz(tab, iloczyn=1, ile=0, indeks=0):
        nonlocal suma
        nonlocal n
        if indeks == n:
            if ile != 0:
                suma += iloczyn
                return
            else:
                return 0
        licz(tab, iloczyn, ile, indeks+1)
        licz(tab, iloczyn*tab[indeks], ile+1, indeks+1)

    licz(tabs)
    return suma


print(zad(60))
