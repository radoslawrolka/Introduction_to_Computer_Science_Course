"""
11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
elementu o zadanym kluczu brak w liście należy element o takim kluczu
wstawić do listy.

"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def dodaj(self, val):
        com = self.head
        if com is None:
            self.head = Node(val)
        else:
            while com.next is not None:
                com = com.next
            com.next = Node(val)

    def wypisz(self):
        com = self.head
        while com is not None:
            print(com.value)
            com = com.next
        print("-----")


def zad(link, key):
    lista = link.head
    if lista.value == key:
        link.head = link.head.next
    else:
        while lista.next is not None:
            if lista.next.value != key:
                lista = lista.next
            else:
                break
        if lista.value == key:
            lista.next = lista.next.next
        elif lista.next.value == key:
            pass
        else:
            lista.next = Node(key)


x = Linklist()
x.dodaj(1)
x.dodaj(3)
x.dodaj(5)
x.wypisz()
zad(x, 7)
x.wypisz()
