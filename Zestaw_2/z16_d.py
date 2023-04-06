def suma_czynniki(x):
    suma = 0
    a = 2
    while x > 1:
        if x % a == 0:
            suma += suma_cyfr(a)
            x = x // a
            a -= 1
        a += 1
    return suma


def suma_cyfr(x):
    suma = 0
    while x > 0:
        suma += x % 10
        x = x // 10
    return suma


i = 1
while i < 1000000:
    if suma_cyfr(i) == suma_czynniki(i):
        print(i)
    i += 1
