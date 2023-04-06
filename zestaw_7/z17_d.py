"""
17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.
"""


def binar(a):
    ile = 0
    while a > 0:
        if a%2 == 1:
            ile += 1
        a //= 2
    return ile%2==1


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
        if com.value == 10 ** 10 or com.value > val:
            buff = com
            self.head = Node(val)
            self.head.next = buff
        # reszta
        else:
            while com.next.value < val:
                com = com.next
            if com.next.value == val:
                return
            else:
                buff = com.next
                com.next = Node(val)
                com.next.next = buff

    def print(self):
        com = self.head
        while com.value != 10 ** 10:
            print(com.value)
            com = com.next
        print("-----")

    def zad(self):
        com = self.head
        # pusta or jeden element
        if com.value == 10 ** 10 or com.next.value == 10 ** 10:
            return
        # reszta
        while com.value != 10**10:
            if com.next.value == 10 ** 10:
                break
            if binar(com.next.value):
                buff = self.head
                self.head = com.next
                com.next = com.next.next
                self.head.next = buff
            com = com.next


x = Linklist()
for i in range(2, 7):
    x.insert(i)
x.print()
x.insert(5)
x.insert(1)
x.print()
x.zad()
x.print()
