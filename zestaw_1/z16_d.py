max = 0
wyraz = 0
for a in range(2,10000):
    x = (a % 2) * (3 * a + 1) + (1 - a % 2) * a / 2
    krok = 1
    while x != 1:
        x = (x % 2) * (3 * x + 1) + (1 - x % 2) * x / 2
        krok += 1
    if krok > max:
        max = krok
        wyraz = a
print(max)
print(wyraz)