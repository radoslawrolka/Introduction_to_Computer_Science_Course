def wielokrotnosc(x):
    n = 1
    a = n * n + n + 1
    while a <= x:
        print(a)
        if x % a == 0:
            return True
        n += 1
        a = n * n + n + 1
    return False


print(wielokrotnosc(999999))
