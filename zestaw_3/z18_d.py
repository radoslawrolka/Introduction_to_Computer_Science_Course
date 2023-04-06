def zad18(tab):
    n = len(tab)
    longest = 0
    for x in range(n):
        for y in range(x + 1, n):
            flag = True
            for i in range(y - x + 1):
                if tab[x + i] != tab[y - i] or tab[x + i] % 2 == 0:
                    flag = False
                    break
            if flag == True:
                longest = max(longest, y - x + 1)
    return longest
