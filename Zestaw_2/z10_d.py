def wielokrotnosc(x):
    a = 2
    while a <= x:
        if x % a == 0:
            return True
        a = 3*a + 1
    return False


print(wielokrotnosc(21))
