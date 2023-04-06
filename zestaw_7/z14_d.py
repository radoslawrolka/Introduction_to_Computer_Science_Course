"""
14. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
element listy o wartościach typu int, usuwającą wszystkie elementy, których
wartość dzieli bez reszty wartość bezpośrednio następujących po nich
elementów.
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
        a = Linklist()
        while com.next is not None:
            if com.next.value%com.value != 0:
                a.add(com.value)
            com = com.next
        self.head = a.head


x = Linklist()
for i in (2,4,5,15,30, 46, 22, 11, 33):
    x.add(i)
x.wypisz()
x.zad()
x.wypisz()
