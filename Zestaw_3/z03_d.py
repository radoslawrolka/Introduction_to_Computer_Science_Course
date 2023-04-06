def sito(x):
    tab = [True]*x
    tab[0], tab[1] = False, False
    for i in range(2, x):
        if tab[i]:
            for j in range(i+i, x, i):
                tab[j] = False

    for i in range(x):
        if tab[i]:
            print(i)


sito(100)
