import math


def find_row(tab, lider):
    result = 0
    for i in range(1, len(tab)):
        if tab[i][lider[i]] < tab[result][lider[result]]:
            result = i
    return result


def z6(tab1):
    n = len(tab1)
    odp = [0] * (n * n)
    lider = [0] * n
    prev = -1
    odp_indeks = 0
    i = 0
    while i < n * n:
        row = find_row(tab1, lider)
        if tab1[row][lider[row]] != prev:
            prev = odp[odp_indeks] = tab1[row][lider[row]]
            odp_indeks += 1
        if lider[row] == n - 1:
            tab1[row][lider[row]] = math.inf
        else:
            lider[row] += 1
        i += 1
    return odp


x = [[4,5,6] for _ in range(3)]
for i in range(len(x)):
    print(x[i])
print(z6(x))
