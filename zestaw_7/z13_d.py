"""
13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
element listy o wartościach typu int, usuwającą wszystkie elementy, których
wartość jest mniejsza od wartości bezpośrednio poprzedzających je
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

    def zad(self, val):
        com = self.head
        while com.next is not None:
            if com.next.value >= val:
                self.head = com.next
                break
            com = com.next


x = Linklist()
for i in range(5):
    x.insert(i)
x.wypisz()
x.zad(6)
x.wypisz()
