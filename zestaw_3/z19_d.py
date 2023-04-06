def zad19(tab):
    n = len(tab)
    maks_dlugosc = 0
    for i in range(n):  #start
        curr_dlugosc = 1
        sum_element = tab[i]
        sum_indeks = i
        for j in range(i, n-1):   #dlugosc
            if tab[j] >= tab[j+1]:
                break
            else:
                curr_dlugosc += 1
                sum_element += tab[j+1]
                sum_indeks += j+1
        if sum_indeks == sum_element:
            maks_dlugosc = max(maks_dlugosc, curr_dlugosc)
    return maks_dlugosc


x = [0,1,2,7,3,4,8,6]
print(zad19(x))
