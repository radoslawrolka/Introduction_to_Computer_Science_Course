def cyfry(x):
    digit = [False] * 10
    while x > 0:
        digit[x % 10] = True
        x //= 10
    return digit


def zad11(tab):
    n = len(tab)
    sasiedzi = 0
    for i in range(n):
        for j in range(n):
            dig = cyfry(tab[i][j])
            ile = 0
            if i - 1 >= 0:
                if dig == cyfry(tab[i - 1][j]):
                    ile += 1
            else:
                ile += 1
            if i + 1 <= n - 1:
                if dig == cyfry(tab[i + 1][j]):
                    ile += 1
            else:
                ile += 1
            if j - 1 >= 0:
                if dig == cyfry(tab[i][j - 1]):
                    ile += 1
            else:
                ile += 1
            if j + 1 <= n - 1:
                if dig == cyfry(tab[i][j + 1]):
                    ile += 1
            else:
                ile += 1
            if ile == 4:
                sasiedzi += 1
    return sasiedzi


x = [
    [1,6,3,4],
    [6,6,6,8],
    [9,6,2,7],
    [4,5,7,7]
]
print(zad11(x))
