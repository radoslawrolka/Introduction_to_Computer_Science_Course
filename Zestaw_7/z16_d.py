"""
16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
początek listy jednokierunkowej, przenosi na początek listy te z nich,
które mają parzystą ilość piątek w zapisie ósemkowym.
"""


def octan_five(x):
    ile = 0
    while x > 0:
        if x % 8 == 5:
            ile += 1
        x //= 8
    return ile % 2 == 0


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
        while com.value != 10**10 or com.next.value != 10 ** 10:
            if octan_five(com.next.value):
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
