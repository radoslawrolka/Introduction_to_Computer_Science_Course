from random import randint


def zad7(n):
    tab = [randint(1, 1000) for _ in range(n)]

    for liczba in tab:
        print(liczba)
        while liczba > 0:
            if liczba%2 == 0:
                return False
            liczba //= 10
    return True


print(zad7(12))
