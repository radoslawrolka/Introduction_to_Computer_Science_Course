"""
19. Elementy w liście są uporządkowane według wartości klucza. Proszę
napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu. Do
funkcji przekazujemy wskazanie na pierwszy element listy,
funkcja powinna zwrócić liczbę usuniętych elementów.
"""


class Node:
    def __init__(self, keyy, val):
        self.key = keyy
        self.value = val
        self.next = None


class Linklist:
    def __init__(self):
        self.head = Node(10 ** 10, 0)

    def insert(self, key=0, val=-1):
        com = self.head
        # na pierwsze wstawienie
        if com.key == 10 ** 10 or com.key > key:
            buff = com
            self.head = Node(key, val)
            self.head.next = buff
        # reszta
        else:
            while com.next.key != 10**10:
                com = com.next
            # if com.next.value == val:
            #    return
            buff = com.next
            com.next = Node(key, val)
            com.next.next = buff

    def print(self):
        com = self.head
        while com.key != 10 ** 10:
            print(com.key, com.value)
            com = com.next
        print("-----")

    def zad(self):
        ile = 0
        com = self.head
        # none or one
        if com.key == 10**10 or com.next.key == 10**10:
            return
        # other
        while com.next.key != 10**10:
            if com.key == com.next.key:
                com.next = com.next.next
                continue
            com = com.next


x = Linklist()
for i in range(3):
    for j in range(3):
        x.insert(i, j)
x.print()
x.zad()
x.print()
