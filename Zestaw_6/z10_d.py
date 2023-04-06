def nowa_macierz(tab, k):
    n = len(tab)
    tab2 = [[0 for _ in range(n - 1)] for _ in range(n - 1)]
    x, y = 0, 0
    for i in range(1, n):
        for j in range(n):
            if j != k:
                tab2[y][x] = tab[i][j]
                x += 1
        y += 1
        x = 0
    return tab2


def zad(tab):
    n = len(tab)
    for i in range(n):
        print(tab[i])
    print()
    if n == 1:
        return tab[0][0]
    wyznacznik = 0
    for i in range(n):
        wyznacznik += ((-1) ** i) * tab[0][i] * zad(nowa_macierz(tab, i))
    return wyznacznik


T = [[1, 9, 0],
     [0, 1, 7],
     [3, 0, 1]]
print(zad(T))
