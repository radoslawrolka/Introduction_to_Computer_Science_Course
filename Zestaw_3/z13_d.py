def zad(n):
    #tab = [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
    tab = [2, 2, 3]
    max = 0
    tab2 = tab[::-1]
    for i in range(n):  #dlugosc
        for j in range(n-i):    #start
            probka = tab[j:j+1+i]
            print(probka)
            for k in range(n-i):    #start testu
                test = tab2[k:k+1+i]
                if test == probka:
                    if i > max:
                        max = i
    return max

print(zad(3))
