def zad(T, i, r):
    n = len(T)
    if r == 0:
        return True
    if r < 0 or i > n - 1:
        return False
    return zad(T, i + 1, r) or zad(T, i + 1, r - T[i])
