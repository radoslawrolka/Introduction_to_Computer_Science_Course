from random import randint


def zad6(n):
    tab = [randint(1, 1000) for _ in range(n)]

    for liczba in tab:
        print(liczba)
        flag = 0
        while liczba > 0:
            if liczba % 2 == 1:
                flag = 1
                break
            liczba //= 10
        if flag == 0:
            return False
    return True

print(zad6(12))
