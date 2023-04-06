def zad11(tab):
    n = len(tab)

    maks = 0
    for i in range(n - 1):  # start
        curr_len = 1
        roznica = tab[i + 1] / tab[i]
        for j in range(n - i - 1):  # dlugosc
            if tab[i + j + 1] / tab[i + j] != roznica:
                break
            curr_len += 1
            maks = max(maks, curr_len)
    return maks


print(zad11([1,2,3,4,2,8,16,3,3,3,1,3,3]))
