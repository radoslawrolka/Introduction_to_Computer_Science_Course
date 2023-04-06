def przesun(tab, x):
    if x < tab[9]:
        return tab
    for i in range(9, -1, -1):
        if x == tab[i]:
            return tab
        if x > tab[i]:
            indeks = i
    for i in range(indeks, 10):
        tab[i], x = x, tab[i]
    return tab


def zad5():
    tab = [0 for _ in range(10)]
    ile = 1
    while True:
        x = int(input())
        if x == 0:
            return tab[9]
        else:
            tab = przesun(tab, x)
            print(tab)


print(zad5())
