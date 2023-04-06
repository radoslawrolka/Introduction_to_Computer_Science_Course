def Suma(x=str):
    sumka = 0
    ile_s = 0
    samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in x:
        sumka += (ord(i)-96)
        for j in samogloski:
            if i == j:
                ile_s += 1
                break
    return sumka, ile_s


def zad(s1, s2, sums1=0, samogloskis1=0, suma=0, ile_samoglosek=0, indeks=0, s3=""):
    print(". ", s3)
    samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
    if sums1 == 0:  #orginal
        sums1, samogloskis1 = Suma(s1)
        if sums1 == 0:
            print("")
            return True
    if sums1 == suma and samogloskis1 == ile_samoglosek:    #True
        print(s3)
        return True
    if indeks == len(s2):
        return False
    flag = 0
    for i in samogloski:
        if s2[indeks] == i:
            flag = 1
            break
    if flag:
        return zad(s1,s2,sums1, samogloskis1, suma, ile_samoglosek, indeks+1, s3) or \
               zad(s1,s2,sums1, samogloskis1, suma+ord(s2[indeks])-96, ile_samoglosek+1, indeks+1, s3+s2[indeks])
    else:
        return zad(s1,s2,sums1, samogloskis1, suma, ile_samoglosek, indeks+1, s3) or \
               zad(s1, s2, sums1, samogloskis1, suma + ord(s2[indeks]) - 96, ile_samoglosek, indeks + 1, s3 + s2[indeks])


print(zad("da", "aaabaaaaba"))
