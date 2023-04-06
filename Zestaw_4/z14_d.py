def jedynki_binarne(x):
    ile = 0
    while x > 0:
        if x % 2 == 1:
            ile += 1
        x //= 2
    return ile


def zad14(tab1, tab2):
    n1 = len(tab1)
    n2 = len(tab2)
    for i in range(n2 - n1 + 1):  # ustawianie kolumny
        for j in range(n2 - n1 + 1):  # ustawianie wiersze
            ile = 0
            for k in range(i, i + n1):  # sprawdzanie kolumny
                for l in range(j, j + n1):  # sprawdzanie wiersze
                    if jedynki_binarne(tab1[k - i][l - j]) == jedynki_binarne(tab2[k][l]):
                        ile += 1
            if ile / (n1 * n1) > 1 / 3:
                return True
    return False


x = [
    [1, 1, 0],
    [0, 0, 0],
    [0, 1, 0]
]
y = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]
print(zad14(x, y))
