def zad10(tab):
    n = len(tab)

    maks = 0
    for i in range(n - 1):  # start
        curr_len = 1
        roznica = tab[i + 1] - tab[i]
        for j in range(n - i - 1):  # dlugosc
            if tab[i + j + 1] - tab[i + j] != roznica:
                break
            curr_len += 1
            maks = max(maks, curr_len)
    return maks


print(zad10([0, 4, 1, 2, 3, 3, 3, 3, 4, 7]))
