'''
która poszukje w tablicy najdłuższego ciągu geometrycznego
leżącego ukośnie w kierunku prawo dół
liczącego co najmniej 3 elementy.
Funkcja powinna zwrócić informacje czy udało się znaleźć taki ciąg oraz długość tego ciągu.
'''


def zad8(tab):
    n = len(tab)
    maks_dlugosc = 0

    for i in range(n-2):    # kolumny
        curr_dlugosc = 1
        curr_dl2 = 1
        curr_q = tab[i][0] / tab[i+1][1]
        curr_q2 = tab[0][i] / tab[1][i+1]
        for j in range(n-i-1):    # wiersze
            print(j, i+j)
            if tab[i+j][j] / tab[i+j+1][j+1] == curr_q:
                curr_dlugosc += 1
                #print("x")
            else:
                curr_dlugosc = 1
                curr_q = tab[i][j] / tab[i+1][j+1]

            if tab[j][i+j] / tab[j+1][i+j+1] == curr_q2:
                curr_dl2 += 1
                print("y")
            else:
                curr_dl2 = 1
                curr_q2 = tab[j][i] / tab[j+1][i+1]
            maks_dlugosc = max(maks_dlugosc, curr_dlugosc, curr_dl2)
    if maks_dlugosc > 2:
        return True, maks_dlugosc
    return False


x = [
    [1,1,1,1],
    [1,3,1,1],
    [1,1,1,1],
    [1,1,1,1]
    ]
print(zad8(x))
