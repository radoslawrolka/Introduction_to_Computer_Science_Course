def move(n, fro, to, use):
    if n == 1:
        print(fro, "->", to)
    else:
        move(n-1, fro, use, to)
        print(fro, "->", to)
        move(n-1, use, to, fro)


move(3, "A", "C", "B")
