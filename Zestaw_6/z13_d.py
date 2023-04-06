def zad(liczba, dzialanie="", maks=1):
    if liczba == 0:
        print(dzialanie)
    elif liczba < maks:
        return
    else:
        for i in range(maks, liczba+1):
            zad(liczba - i, dzialanie + "+" + str(i), max(maks, i))

zad(5)
