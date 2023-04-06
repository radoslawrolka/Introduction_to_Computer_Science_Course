def zad16(tab):
    n = len(tab)
    max = tab[0]
    min = tab[0]
    for i in range(1, n):
        if tab[i] > max:
            max = tab[i]
        elif tab[i] < min:
            min = tab[i]
        elif max == tab[i] or min == tab[i]:
            return False
    return True


print(zad16([1,2,3,4,5,6,7,8,8]))
