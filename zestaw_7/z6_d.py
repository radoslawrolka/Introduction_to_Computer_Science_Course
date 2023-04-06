"""
6. Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
wartość.
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def dodaj(self, val):
        while self is not None:
            if self.next is None:
                self.next = Node(val)
                return "Dodano"
            self = self.next

    def wypisz(self):
        while self is not None:
            print(self.value, end=", ")
            self = self.next
        print()


def zad(lista, val):
    s = lista
    while lista.next is not None:
        lista = lista.next
    lista.next = Node(val)


x = Node(3)
x.dodaj(5)
x.dodaj(7)
x.wypisz()
zad(x, 8)
x.wypisz()
