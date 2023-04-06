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
