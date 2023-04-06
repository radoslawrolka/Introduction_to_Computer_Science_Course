def nwd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def trojki(tab):
    n = len(tab)
    counter = 0
    for i in range(n - 2):
        if nwd(nwd(tab[i], tab[i + 1]), tab[i + 2]) == 1:
            counter += 1
    for i in range(n - 3):
        if nwd(nwd(tab[i], tab[i + 1]), tab[i + 3]) == 1:
            counter += 1
        if nwd(nwd(tab[i], tab[i + 2]), tab[i + 3]) == 1:
            counter += 1
    for i in range(n - 4):
        if nwd(nwd(tab[i], tab[i + 2]), tab[i + 4]) == 1:
            counter += 1
    return counter


x = [1, 2, 3, 4, 5]
print(trojki(x))
