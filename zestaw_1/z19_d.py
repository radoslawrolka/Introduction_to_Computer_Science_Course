def silnia(x):
    if x == 0:
        return 1
    else:
        sil = 1
        for i in range(2, x+1):
            sil = sil*i
        return sil


e = 1
for i in range(1, 101):
    if i > 5 and e == e+(1/silnia(i)):
        break
    e += 1/silnia(i)
    print(str(i) + ": " + str(e))
