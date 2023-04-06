"""
18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Linklist:
    def __init__(self):
        self.head = Node(10 ** 10)

    def insert(self, val):
        com = self.head
        # na pierwsze wstawienie
        if com.value == 10 ** 10:  # or com.value > val:
            buff = com
            self.head = Node(val)
            self.head.next = buff
        # reszta
        else:
            while com.next.value != 10**10:
                com = com.next
            # if com.next.value == val:
            #    return
            buff = com.next
            com.next = Node(val)
            com.next.next = buff

    def print(self):
        com = self.head
        while com.value != 10 ** 10:
            print(com.value)
            com = com.next
        print("-----")

    def set(self):
        com = self.head
        if com.value == 10 ** 10 or com.next.value == 10 ** 10:
            return
        else:
            while com.value != 10 ** 10:
                kom = com
                while kom.next.value != 10 ** 10:
                    if com.value == kom.next.value:
                        kom.next = kom.next.next
                    kom = kom.next
                com = com.next


x = Linklist()
for i in range(3):
    for j in range(5):
        x.insert(j)
x.print()
x.set()
x.print()
