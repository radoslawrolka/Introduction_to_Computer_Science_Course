def zad7(tab):
    n = len(tab)
    odp = [0] * (n * n)
    lider = [0] * n
    i = 0
    minus = tab[0][lider[0]]
    minus_indeks = 0
    while i < n * n:
        minus = 999999999999999
        for j in range(n):
            if lider[j] >= n:
                continue
            if minus > tab[j][lider[j]]:
                minus = tab[j][lider[j]]
                minus_indeks = j
        odp[i] = minus
        lider[minus_indeks] += 1
        print(lider)
        i += 1
    return odp


x = [[1, 26, 35], [4, 5, 6], [7, 8, 9]]
print(zad7(x))
