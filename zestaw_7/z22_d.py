"""
22. Dana jestlista, który być może zakończona jest cyklem.
Napisać funkcję, która sprawdza ten fakt.
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
            self.head.next = self.head
        else:
            com = self.head
            while com.next != self.head:
                com = com.next
            com.next = Node(val)
            com.next.next = self.head

    def print(self):
        com = self.head
        while com is not None:
            print(com.value)
            com = com.next
        print("-----")

    def is_cycle(self):
        com = self.head
        if com is None:
            return False
        while com.next is not None:
            if com.next == self.head:
                return True
            com = com.next
        return False


x = Linklist()
x.add(1)
x.add(2)
x.add(3)
x.add(4)
# x.print()
print(x.is_cycle())
