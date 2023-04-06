"""
15. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.
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

    def add(self, val):
        com = self.head
        if com is None:
            self.head = Node(val)
        else:
            while com.next is not None:
                com = com.next
            com.next = Node(val)

    def zad(self):
        com = self.head
        while com.next is not None:
            if trinal(com.next.value):
                com.next = com.next.next
            com = com.next
        if trinal(self.head.value):
            self.head = self.head.next


def trinal(x):
    uno = 0
    dos = 0
    while x > 0:
        if x%3 == 1:
            uno += 1
        elif x%3 == 2:
            dos += 1
        x//=3
    return uno > dos


x = Linklist()
for i in range(7):
    x.add(i)
x.wypisz()
x.zad()
x.wypisz()
