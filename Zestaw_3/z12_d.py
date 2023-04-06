from random import randint


def zad12(n):
    tab = [0 for _ in range(n)]
    for i in range(n):
        while True:
            tab[i] = randint(1, 99)
            if tab[i] % 2 == 1:
                break
    print(tab)

    maks = 0
    minus = 0

    for i in range(n - 1):  # start
        curr_len = 1
        roznica = tab[i + 1] - tab[i]
        if roznica > 0:
            flag = 1
        elif roznica < 0:
            flag = -1
        for j in range(n - i - 1):  # dlugosc
            if tab[i + j + 1] - tab[i + j] != roznica:
                break
            curr_len += 1
            if flag == 1:
                maks = max(maks, curr_len)
            elif flag == -1:
                minus = max(minus, curr_len)
    return maks - minus


print(zad12(12))
