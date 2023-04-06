def spirala(n):
    tab = [[0]*n for d in range(n)]
    x, y = 0, 0
    i = 1
    while i <= n*n:
        while x < n - 1 and tab[y][x+1] == 0:
            tab[y][x] = i
            i += 1
            x += 1
        while y < n - 1 and tab[y+1][x] == 0:
            tab[y][x] = i
            i += 1
            y += 1
        while x > 0 and tab[y][x-1] == 0:
            tab[y][x] = i
            i += 1
            x -= 1
        while y > 0 and tab[y-1][x] == 0:
            tab[y][x] = i
            i += 1
            y -= 1
        if i == n*n:
            tab[y][x] = i
            i += 1
    for i in range(n):
        print(tab[i])


spirala(6)
