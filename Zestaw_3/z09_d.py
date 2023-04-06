def zad9(tab):
    n = len(tab)
    maks = 0
    for i in range(n):  # start
        curr_len = 1
        for j in range(n - i-1):  # dlugosc
            if tab[i + j] >= tab[i + j + 1]:
                break
            curr_len += 1
            maks = max(maks, curr_len)
    return maks


print(zad9([1, 3, 2, 8, 3, 5, 5, 6, 1, 7, 8, 4, 5]))
