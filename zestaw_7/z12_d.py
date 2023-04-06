"""
12. Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci
jednokierunkowej listy. Napisy w łańcuchu są uporządkowane
leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy
oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą,
czy w wyniku operacji moc zbioru uległa zmianie.
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def wypisz(self):
        com = self.head
        while com is not None:
            print(com.value)
            com = com.next
        print("-----")

    def moc(self):
        ile = 0
        com = self.head
        while com is not None:
            ile += 1
            com = com.next
        return ile

    def containing(self, val):
        com = self.head
        while com is not None:
            if com.value == val:
                return True
            com = com.next
        return False

    def insert(self, val):
        com = self.head
        if not self.containing(val):
            if com is None:
                self.head = Node(val)
            elif com.value > val:
                first = Node(val)
                first.next = com
                self.head = first
            else:
                while com.next is not None and com.next.value < val:
                    com = com.next
                buff = com.next
                com.next = Node(val)
                com.next.next = buff


def zad(link, napis):
    m1 = link.moc()
    link.insert(napis)
    return not (m1 == link.moc())


x = Linklist()
x.insert(1)
x.insert(3)
x.insert(5)
x.wypisz()
print(zad(x, -1))
x.wypisz()
