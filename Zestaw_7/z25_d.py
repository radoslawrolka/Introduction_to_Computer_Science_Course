"""
25. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która
zwraca wskaźnik do ostatniego elementu przed cyklem.
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
        while com.next != self.head:
            print(com.value)
            com = com.next
        print(com.value)
        print("-----")

    def last(self):
        com = self.head
        while com.next != self.head:
            com = com.next
        return com


x = Linklist()
x.add(1)
x.add(2)
x.add(3)
x.add(4)
x.print()
print(x.last())
print(x.last().value)
