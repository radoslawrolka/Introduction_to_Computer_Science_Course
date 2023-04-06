stop = False


def zad(T, i, r, w1, w2):
    global stop
    if stop:
        return False
    n = len(T)
    if r == 0:
        stop = True
        print(w1, w2)
    if r < 0 or i > n - 1:
        return False
    return zad(T, i + 1, r, w1, w2) or \
           zad(T, i + 1, r - T[i], w1+[T[i]], w2) or \
           zad(T, i + 1, r + T[i], w1, w2+[T[i]])
