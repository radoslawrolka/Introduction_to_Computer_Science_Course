import math


def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3 or num == 5:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(6, int(math.sqrt(num)) + 1, 6):
        if num % (i - 1) == 0 or num % (i + 1) == 0:
            return False
        i += 2

    return True


# maska binarna
def mix_numbers(a, b, mask):
    num = 0
    multi = 1
    while mask > 0 or a > 0:
        if mask % 2 == 0:
            d = a % 10
            a //= 10
        else:
            d = b % 10
            b //= 10
        mask //= 2

        num = d * multi + num
        multi *= 10

    return num


def validate_mask(a, b, mask):
    cnt1 = len(str(a))  # counter liczb
    cnt2 = len(str(b))  # liczymy ile cyfr użyliśmy z każdej cyfry
    while mask > 0:
        if mask % 2 == 0:
            cnt1 -= 1
        else:
            cnt2 -= 1
        mask //= 2

    return cnt1 >= 0 and cnt2 == 0  # cnt1 musi byc >=0 bo maska może zaczynać sie od 0 a while tego nie wie


def zad14(a, b):
    ile = 0
    for mask in range(2**(len(str(a))+len(str(b)))):
        if validate_mask(a, b, mask):
            if is_prime(mix_numbers(a, b, mask)):
                ile += 1
    print(ile)


zad14(14, 123)
