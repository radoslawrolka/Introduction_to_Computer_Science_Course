from copy import deepcopy


def kopia(tab, x, y):
    tab2 = deepcopy(tab)
    tab2[x][y] = "x"
    return tab2


def top(tab, w=0, k=0):
    kierunki = ("Lewo-Gora", "Prawo-Gora", "Prawo-Dol", "Lewo-Dol")
    czy = [False for i in range(4)]
    win = [[["." for i in range(8)] for j in range(8)] for k in range(4)]
    for i in range(4):
        win[i][w][k] = "X"
    corner = ((0, 0), (0, 7), (7, 7), (7, 0))
    move = ((-1, -1), (-1, 1), (1, 1), (1, -1))
    for i in range(0, 4):
        def zad(tab, w, k, odp):
            nonlocal i
            nonlocal czy
            nonlocal corner
            n = len(tab[w][k])
            if czy[i]:
                return
            else:
                if w == corner[i][0] and k == corner[i][1]:
                    czy[i] = True
                    win[i] = odp
                else:
                    if -1 < w + move[i][0] < 8 and tab[w][k][n - 1] < tab[w + move[i][0]][k][0]:
                        zad(tab, w + move[i][0], k, kopia(odp, w + move[i][0], k))
                    if -1 < k + move[i][1] < 8 and tab[w][k][n - 1] < tab[w][k + move[i][1]][0]:
                        zad(tab, w, k + move[i][1], kopia(odp, w, k + move[i][1]))
                    if -1 < w + move[i][0] < 8 and -1 < k + move[i][1] < 8 and tab[w][k][n - 1] < \
                            tab[w + move[i][0]][k + move[i][1]][0]:
                        zad(tab, w + move[i][0], k + move[i][1], kopia(odp, w + move[i][0], k + move[i][1]))

        zad(tab, w, k, win[i])

    for i in range(4):
        print(kierunki[i], ": ", czy[i])
        for j in range(8):
            print(win[i][j])


x = [[8, 2, 3, 4, 5, 6, 7, 8],
     [2, 7, 3, 4, 5, 6, 7, 7],
     [3, 6, 0, 4, 5, 6, 7, 6],
     [6, 2, 4, 3, 5, 6, 7, 5],
     [5, 5, 5, 5, 2, 6, 7, 4],
     [6, 6, 6, 6, 6, 1, 2, 3],
     [7, 7, 7, 7, 7, 7, 7, 8],
     [8, 8, 8, 8, 8, 8, 8, 8]]
for i in range(8):
    for j in range(8):
        x[i][j] = str(x[i][j])
top(x, 5, 5)
