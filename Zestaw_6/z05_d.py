"""
Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
110100 nie jest możliwe.
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


def number(tab):
    n = len(tab)
    num = 0
    for i in range(n):
        num += tab[i]*(10**(n-1))
        n -= 1
    return num


def zad(tab):
    print(tab)
    n = len(tab)
    if n == 0:
        return True
    for i in range(n):
        liczba = number(tab[0:i+1])
        if is_prime(liczba):
            return zad(tab[i+1:])


x = [1,1,2,3,4,7,8,3]
print(zad(x))
