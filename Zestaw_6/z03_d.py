"""
Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt przebywania
na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie k.
Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
polu startowym i ostatnim także wliczamy do kosztu przejścia.
"""


def fun(T, w, k):
    if k > 0:
        left = fun(T, w + 1, k - 1)
    else:
        left = float('inf')
    if k < 7:
        right = fun(T, w + 1, k + 1)
    else:
        right = float('inf')
    middle = fun(T, w + 1, k)

    return min(left, middle, right)
