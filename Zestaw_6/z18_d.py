def top(tab):
    czy = False

    def zad(tab, w=0, k=0):
        nonlocal czy
        n = len(tab[w][k])

        if czy:
            return
        else:
            if w==7 and k==7:
                czy = True
            else:
                if w+1<8 and tab[w][k][n-1] < tab[w+1][k][0]:
                    zad(tab, w+1, k)
                if k+1<8 and tab[w][k][n-1] < tab[w][k+1][0]:
                    zad(tab, w, k+1)
                if w + 1 < 8 and k+1<8 and tab[w][k][n - 1] < tab[w + 1][k+1][0]:
                    zad(tab, w + 1, k + 1)

    zad(tab)
    return czy


x = [[1,2,3,4,5,6,7,8],
     [2,2,3,4,5,6,7,8],
     [3,3,0,4,5,6,7,8],
     [4,4,4,4,5,6,7,8],
     [5,5,5,5,5,6,7,8],
     [6,6,6,6,6,6,7,8],
     [7,7,7,7,7,7,7,8],
     [8,8,8,8,8,8,8,8]]
for i in range(8):
    for j in range(8):
        x[i][j] = str(x[i][j])
print(top(x))
