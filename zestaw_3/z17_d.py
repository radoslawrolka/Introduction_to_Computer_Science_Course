import math


def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i < math.sqrt(x) + 1:
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def trojkowy(x):
    w = ""
    while x > 0:
        if x % 3 == 0:
            w = "0" + w
        elif x % 3 == 2:
            w = "2" + w
        else:
            w = "1" + w
        x //= 3
    return w


def suma(a, b):
    n = len(a)
    counter = 0
    for i in range(3 ** n):
        mask = trojkowy(i)
        sum = 0
        for j in mask:
            if j == 0:
                sum += int(a[int(j)])
            elif j == 1:
                sum += int(b[int(j)])
            else:
                sum += int(a[int(j)]) + int(b[int(j)])
        if is_prime(sum):
            print(sum)
            counter += 1
    return counter


# ---------------------------------------------------------------


def sumka(a, b):
    n = len(a)
    count = 0
    masks = 3 ** n
    for mask in range(masks):
        decrypt = 3 ** (n - 1)
        sume = 0
        for i in range(n):
            if mask - 2 * decrypt >= 0:
                sume += b[n - 1 - i]
                mask -= 2 * decrypt
            elif mask - decrypt >= 0:
                sume += a[n - 1 - i]
                mask -= decrypt
            else:
                sume += a[n - 1 - i] + b[n - 1 - i]
            decrypt //= 3
        if is_prime(sume):
            print(sume)
            count += 1
    return count


x = [2, 3, 4]
y = [4, 7, 3]

print(suma(x, y))
print("------------")
print(sumka(x, y))
