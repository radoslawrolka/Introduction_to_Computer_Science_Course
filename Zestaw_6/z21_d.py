from copy import deepcopy

def kopia(tab, x):
    tab2 = deepcopy(tab)
    tab2.remove(x)
    return tab2

def zad(tab, szukana, n, suma=0, wiersze=[_ for _ in range(3)], kolumny=[_ for _ in range(3)]):
    if szukana == suma:
        return True
    if wiersze != [] and kolumny != []:
        for wiersz in wiersze:
            for kolumna in kolumny:
                if zad(tab, szukana, n, suma+tab[wiersz][kolumna], kopia(wiersze, wiersz), kopia(kolumny, kolumna)):
                    return True
    return False


x = [[1,6,3],
     [6,6,4],
     [1,6,3]]
print(zad(x, 5, 3))