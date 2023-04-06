"""
5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
należy połączyć w jedną listę odsyłaczową, która jest posortowana
niemalejąco według ostatniej cyfry pola val.
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


def zad(Lista):
    t = [None] * 10
    s = [0] * 10

    while Lista is not None:
        if t[Lista.value % 10] is None:
            t[Lista.value % 10] = Node(Lista.value)
            s[Lista.value % 10] = t[Lista.value % 10]
        else:
            t[Lista.value % 10].next = Node(Lista.value)
            t[Lista.value % 10] = t[Lista.value % 10].next
        Lista = Lista.next

    for i in range(9):
        t[i].next = s[i + 1]
    s[0].wypisz()
    return Lista


x = Node(4)
for i in range(20):
    x.dodaj(i)
x.wypisz()
x = zad(x)
x.wypisz()
