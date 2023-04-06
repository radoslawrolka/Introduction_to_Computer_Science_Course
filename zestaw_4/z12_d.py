import math


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if not x % i:
            return False
    return True


def is_composite(n):
    if n == 1:
        return False
    else:
        return not is_prime(n)


def condition(array, x, y, z):
    count = 0
    n = len(array)
    for i, j in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y + 1), (x - 1, y - 1),
                 (x - 1, y + 1)]:
        if not array[z][i][j]:
            count += 1
    return count


def zad12(array_3d):
    n = len(array_3d)
    for i in range(n):  # zamiana liczb w arr_3d na True/False w zależności czy jest złożona
        for j in range(n):
            for k in range(n):
                array_3d[i][j][k] = is_composite(array_3d[i][j][k])

    level_count = -1
    for z in range(n):  #level
        current_count = 0
        for x in range(1, n - 1):   # liczymy bez brzegów, bo nie będzie tam 6 sąsiadów
            for y in range(1, n - 1):
                neighbours = condition(array_3d, x, y, z)
                if neighbours >= 6:
                    current_count += 1
        if level_count == -1:
            level_count = current_count
        else:
            if level_count != current_count:
                return False
    return True


tab = [[[2, 2, 2, 2], [3,3,3,3], [3,4,5,6], [6,7,8,9]] for t in range(4)]
for a in range(len(tab)):
    for b in range(len(tab)):
        print(tab[a][b])
    print("----------------")
print(zad12(tab))
