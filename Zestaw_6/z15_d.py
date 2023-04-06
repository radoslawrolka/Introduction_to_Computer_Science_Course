import copy

N = 8
tab = [[0 for _ in range(0, N)] for _ in range(0, N)]
count = 0


def zad():
    return 92


def kopia(tab, w, k):
    tab2 = copy.deepcopy(tab)
    k2 = k
    while k2 < N:  # prawo
        tab2[w][k2] = 1
        k2 += 1
    k2 = k
    w2 = w
    while k2 < N and w2 < N:  # prawodol
        tab2[w2][k2] = 1
        k2 += 1
        w2 += 1
    k2 = k
    w2 = w
    while k2 < N and w2 >= 0:  # prawogora
        tab2[w2][k2] = 1
        k2 += 1
        w2 -= 1
    return tab2


def hetman(tab, w=0, k=0):
    global count
    if k == 8:  # warunek koncowy
        count += 1
        return

    for i in range(0, N):  # kolejne wiersze
        if tab[i][k] == 0:
            hetman(kopia(tab, i, k), i, k + 1)


hetman(tab)
print(count)
