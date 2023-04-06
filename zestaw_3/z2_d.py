def czy_same(a, b):
    cyfry = [0]*10
    while a > 0:
        cyfry[a%10] += 1
        a //= 10
    while b > 0:
        cyfry[b%10] -= 1
        b //= 10
    for i in range(10):
        if cyfry[i] != 0:
            return False
    return True


print(czy_same(123, 3201))
