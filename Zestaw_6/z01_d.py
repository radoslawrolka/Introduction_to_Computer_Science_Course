import math


def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i < int(math.sqrt(x)) + 1:
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def len_int(x):
    return int(math.log10(x)) + 1


def zad(pierwotna, is_original=1, mnoznik=1):
    if len_int(pierwotna) < 2:
        print("Za krótka liczba (len < 2)")
    elif len_int(mnoznik) <= len_int(pierwotna):
        if is_original:
            zad(pierwotna, 1, mnoznik * 10)  # ta sama, next indeks
            zad(((pierwotna // mnoznik) // 10) * mnoznik + pierwotna % mnoznik, 0, mnoznik)  # liczba wykreslona
        else:
            if is_prime(pierwotna):
                print(pierwotna)
            if len_int(pierwotna) > 2:
                zad(pierwotna, 0, mnoznik * 10)  # ta sama, next indeks
                zad(((pierwotna // mnoznik) // 10) * mnoznik + pierwotna % mnoznik, 0, mnoznik)  # liczba wykreslona


def nastringu(x, is_origin=1, indeks=0):
    #print(x, indeks)
    if len(x) < 2:
        print("Za krotka")
    if is_origin:
        if indeks < len(x):
            nastringu(x, 1, indeks + 1)
            nastringu(x[0:indeks] + x[indeks+1:], 0, indeks)
    else:
        if is_prime(int(x)):
            print(x)
        if len(x) > 2:
            if indeks < len(x):
                nastringu(x, 1, indeks + 1)
                nastringu(x[0:indeks] + x[indeks+1:], 0, indeks)


a = 1234567
nastringu(str(a))
# zad(a)
