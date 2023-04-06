def zad17(tab):
    n = len(tab)
    maks_suma = 0
    kolumna = 0
    wiersz = 0
    for i in range(n):  # pion
        for j in range(n):  # poziom
            suma = 0
            if i - 1 >= 0:
                suma += tab[i - 1][j]  # gora
                if j - 1 >= 0:
                    suma += tab[i - 1][j - 1]  # gora-lewo
                if j + 1 <= n - 1:
                    suma += tab[i - 1][j + 1]  # gora-prawo
            if i + 1 <= n - 1:
                suma += tab[i + 1][j]  # dol
                if j - 1 >= 0:
                    suma += tab[i + 1][j - 1]  # dol-lewo
                if j + 1 <= n - 1:
                    suma += tab[i + 1][j + 1]  # dol-prawo
            if j - 1 >= 0:
                suma += tab[i][j - 1]  # lewo
            if j + 1 <= n-1:
                suma += tab[i][j + 1]  # prawo
            if maks_suma < suma:
                maks_suma = suma
                kolumna = j
                wiersz = i
    return maks_suma, "kolumna", kolumna, "wiersz", wiersz


x = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(zad17(x))
