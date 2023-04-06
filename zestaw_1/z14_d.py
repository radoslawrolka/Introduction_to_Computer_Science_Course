def silnia(x):
    if x == 0:
        return 1
    else:
        sil = 1
        for i in range(2, x+1):
            sil = sil*i
        return sil

x = int(input("wpisz: "))

suma = 1
i = 2
flag = -1
while i<100:
    if flag == 1:
        suma += (x**i) * (1/silnia(i))
    else:
        suma -= (x**i) * (1/silnia(i))
    i += 2
    flag = (-1)*flag
print(suma)