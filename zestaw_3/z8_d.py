def czy_end(tab):
    n = len(tab)
    tab2 = [False for _ in range(n)]
    tab2[0] = True
    for i in range(n):
        if tab2[i]:
            temp = tab[i]
            k = 2
            while temp != 1:
                while temp % k == 0:
                    if i + k < n:
                        tab2[i + k] = True
                    temp = temp // k
                k += 1
    if tab2[n - 1]:
        return True
    return False


print(czy_end([6, 5, 3, 2, 4, 5, 2]))
