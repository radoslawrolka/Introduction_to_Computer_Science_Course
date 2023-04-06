"""
33. Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza”
od pierwszej litery s2. Według tej zasady rozmieszczono napisy w liście
cyklicznej, na przykład:
┌─bartek──leszek──marek──ola──zosia─┐
└───────────────────────────────────┘
Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do listy
napis z zachowaniem zasady poprzedzania. Do funkcji należy przekazać
wskaźnik do listy oraz wstawiany napis, funkcja powinna zwrócić wartość
logiczną wskazującą, czy udało się wstawić napis do listy. Po wstawieniu
elementu wskaźnik do listy powinien wskazywać na nowo wstawiony element.
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def print(self):
        com = self.head
        while com.next != self.head:
            print(com.value)
            com = com.next
        print(com.value)

    def add(self, val):
        com = self.head
        if com is None:
            self.head = Node(val)
            self.head.next = self.head
        else:
            while com.next != self.head:
                com = com.next
            new = Node(val)
            new.next = self.head
            com.next = new

