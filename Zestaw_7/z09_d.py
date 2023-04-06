"""
9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
zwiększającą taką liczbę o 1.
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


def zad(lista):
    while lista.next is not None:
        lista = lista.next
    lista.value += 1


x = Node(3)
x.dodaj(5)
x.dodaj(7)
x.dodaj(9)
x.dodaj(1)
x.wypisz()
zad(x)
x.wypisz()
