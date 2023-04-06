"""
8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
element listy. Do funkcji należy przekazać wskazanie na pierwszy element
listy.
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
    while lista is not None:
        if lista.next is not None:
            lista.next = lista.next.next
        lista = lista.next


x = Node(3)
x.dodaj(5)
x.dodaj(7)
x.dodaj(9)
x.dodaj(10)
x.wypisz()
zad(x)
x.wypisz()
