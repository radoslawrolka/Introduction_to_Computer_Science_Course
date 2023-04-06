def zad(tab, indeks=0, suma_ind=0, suma_ele=0, curr_ile=0):
    if (curr_ile > 1) and (suma_ind == suma_ele):
        return suma_ele, curr_ile
    if indeks == len(tab):
        return 9999
    else:
        return min(zad(tab, indeks + 1, suma_ind, suma_ele, curr_ile),
                   zad(tab, indeks + 1, suma_ind + indeks, suma_ele + tab[indeks], curr_ile + 1))


x = [1, 7, 3, 5, 11, 2]
print(zad(x))
