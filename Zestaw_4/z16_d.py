import math


def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i < math.sqrt(x) + 1:
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def zad16(tab):
    n = len(tab)
    for i in range(n):
        flag_wiersz = 0
        for j in range(n):
            flag = 1
            while tab[i][j] > 0:
                if not is_prime(tab[i][j]%10):
                    flag = 0
                    break
                tab[i][j] //= 10
            if flag:
                flag_wiersz = 1
                break
        if not flag_wiersz:
            return False
    return True


x = [
    [1, 2, 1, 4],
    [2, 2, 4, 2],
    [9, 6, 9, 8],
    [26, 7, 5, 3]
    ]
print(zad16(x))
