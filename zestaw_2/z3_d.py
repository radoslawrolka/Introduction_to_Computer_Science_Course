def ile_cyfr(x):
    suma = 0
    while x > 0:
        suma += 1
        x = x // 10
    return suma


def na_binary(x):
    i = 0
    a = 0
    while x > 0:
        if x % 2 != 0:
            a += 10 ** i
        i += 1
        x = x // 2
    return a


def czy_palindrom(x):
    ile = ile_cyfr(x)
    while ile > 1:
        if (x - x % (10 ** (ile - 1))) // 10 ** (ile - 1) != x % 10:
            return False
        x -= x - x % (10 ** (ile - 1))
        x = x // 10
        ile -= 2
    return True


def zad3(x):
    print("czy palindrom: ")
    print(czy_palindrom(x))
    print("binar")
    x = na_binary(x)
    print(x)
    print(czy_palindrom(x))


zad3(21)
