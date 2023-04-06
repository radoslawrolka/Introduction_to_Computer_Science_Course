class Lista:
    def __init__(self, val=None, indeks=-1):
        self.value = val
        self.next = None
        self.indeks = indeks

    def wypisz(self):
        while self is not None:
            print(self.value, end=", ")
            self = self.next
        print()


def wartosc_indeks(lis, indeks):
    i = 0
    while lis is not None:
        if indeks == i:
            return lis.value
        i += 1
        lis = lis.next
    return "Index out of range"


def podstaw(lis, indeks, val):
    i = 0
    while i <= indeks:
        if indeks == i:
            lis.value = val
            return "Podstawione"
        if lis.next is None:
            lis.next = Lista(None, i)
        i += 1
        lis = lis.next


def inicjalizuj():
    a = Lista()
    return a


x = inicjalizuj()
podstaw(x, 0, 0)
podstaw(x, 2, 2)
x.wypisz()
print(wartosc_indeks(x, 2))
