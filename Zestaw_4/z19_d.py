# elementy są odległe o jeden ruch skoczka szachowego.

def z20(tab, szukana):
    n = len(tab)
    ile_par = 0
    for i in range(n):
        for j in range(n):

            for (y2, x2) in ((i+2, j-1), (i+2, j+1), (i+1, j-2), (i+1, j+2), (i-1, j-2), (i-1, j+2), (i-2, j-1), (i-2, j+1)):
                if x2 < 0 or x2 > n-1 or y2 < 0 or y2 > n-1:
                    continue
                if tab[i][j] * tab[y2][x2] == szukana:
                    ile_par += 1
    return ile_par // 2


x = [[1, 1, 1,] for _ in range(3)]
print(z20(x, 1))
