def z4(tab):
    n = len(tab)
    minim = 9999999
    minim_i = 0
    maks = 0
    maks_i = 0
    for i in range(n):
        suma = 0
        suma2 = 0
        for j in range(n):
            suma += tab[i][j]
            suma2 += tab[j][i]
        if maks < suma2:
            maks = suma2
            maks_i = i
        if minim > suma:
            minim = suma
            minim_i = tab[i]
    tab2 = [0]*n
    for i in range(n):
        tab2[i] = tab[i][maks_i]
    return tab2, minim_i


x = [[1,2,3], [4,5,6], [7,8,9]]
print(z4(x))
