"""
Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
wymiarach NxN ruchem skoczka szachowego.
"""

def rek(m, T, n, i=0, j=0, val=0):
    T[i][j] = val

    if val == (n ** 2) - 1:
        return True

    for move in m:
        x, y = move
        if -1 < x + i < n and -1 < y + j < n and T[x + i][y + j] == -1:
            if rek(m, T, n, i + x, j + y, val + 1):
                return True
    T[i][j] = -1
    return False



m = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, 1), (2, -1)]    #ruchy skoczka
n = 6   #pola szachownicy
T = [[-1 for _ in range(n)] for _ in range(n)]
for i in T:
    print(i)
print()
rek(m, T, n, 0, 0, 0)
for i in T:
    print(i)
