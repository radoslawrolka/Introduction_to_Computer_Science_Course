def z9(tab, ile):
    n = len(tab)
    for i in range(3, n+1, 2):   #dlugosc boku
        for j in range(0, n-i+1): #wartosc x
            for k in range(0, n-i+1): #wartosc y
                jeden = tab[k][j]
                dwa = tab[k][j + i - 1]
                trzy = tab[k + i - 1][j]
                cztery = tab[k + i - 1][j + i - 1]
                iloczyn = jeden * dwa * trzy * cztery
                print(iloczyn)
                if iloczyn == ile:
                    return True, "liczymy od 1", "kolumna", k+i//2, "wiersz", j+i//2
    return False


x = [[2,2,1,2,2], [2,1,1,1,1], [1,1,1,4,1], [1,1,1,1,1], [2,1,1,1,24]]
for i in range(len(x)):
    print(x[i])

print(z9(x, 16))
