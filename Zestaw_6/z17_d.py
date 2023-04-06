"""
Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić wszystkie cyfry
występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
zadanych liczb
"""
import math


def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i < int(math.sqrt(x)) + 1:
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def len_int(x):
    return len(str(x))


def zad(l1, l2, l3=0, ile=1):
    #print(l1, l2)
    if l1 == 0 and l2 == 0:
        if is_prime(l3):
            print(l3)
            return 1
        else:
            return 0
    if l1 == 0:
        while l2 > 0:
            l3 += (l2%10)*ile
            ile *= 10
            l2 //= 10
        if is_prime(l3):
            print(l3)
            return 1
    if l2 == 0:
        while l1 > 0:
            l3 += (l1 % 10) * ile
            ile *= 10
            l1 //= 10
        if is_prime(l3):
            print(l3)
            return 1
    return zad(l1//10, l2, l3+((l1%10)*ile), ile*10) + zad(l1, l2//10, l3+((l2%10)*ile), ile*10)


print(zad(11, 2))
