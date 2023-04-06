'''
def silnia(x):
    w = 1
    for i in range(2, x + 1):
        w *= i
    return w


def po_przecinku(a, b, n):
    w = [0]*n
    a %= b
    i = 0
    while a > 0 and n > 0:
        a *= 10
        w[i] = a // b
        a %= b
        n -= 1
        i += 1
    return w


def dodawanie(x, y, n):
    w = [0]*n
    for i in range(n):
        w[n-1-i] += x[n-1-i] + y[n-1-i]
        if w[n-1-i] > 9:
            w[n-2-i] += 1
            w[n-1-i] -= 10
    return w


def e(n):
    wynik = [0]*n
    i = 2
    while i < 10:
        skladnik = po_przecinku(1, silnia(i), n)
        wynik = dodawanie(wynik, skladnik, n)
        i += 1
    w = "2."
    for i in wynik:
        w += str(i)
    return w


print(e(10000))
'''

def long_div(a, b, tab):
    for i in range(1, len(tab)):
        a *= 10
        tab[i] += a//b
        a %= b
        if a == 0:
            return

def zad4(n):
    digits = [1]+[0]*(n+10)
    fact = 1
    k = 1
    while fact <= 10**n:
        fact *= k
        k += 1
        long_div(1, fact, digits)
    for i in range(len(digits)-1, 0, -1):
        digits[i-1] += digits[i]//10
        digits[i] %= 10
    return digits[:n+1]


print(zad4(100))
