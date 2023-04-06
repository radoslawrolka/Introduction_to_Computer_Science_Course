"""
28. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
naturalne. W pierwszej liście liczby są posortowane rosnąco, a w drugiej
nie. Proszę napisać funkcję usuwającą z obu list liczby występujące w obu
listach. Do funkcji należy przekazać wskazania na obie listy, funkcja
powinna zwrócić łączną liczbę usuniętych elementów.
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Linklist:
    def __init__(self):
        self.head = Node(10**10)

    def add(self, val):
        if self.head.value == 10**10:
            self.head = Node(val)
            self.head.next = Node(10**10)
        else:
            com = self.head
            while com.next.value != 10**10:
                com = com.next
            new = Node(val)
            new.next = com.next
            com.next = new

    def print(self):
        com = self.head
        while com.value != 10**10:
            print(com.value)
            com = com.next
        print("-----")


def zad(l1, l2):
    ile = 0
    com = l1.head
    while com.next.value != 10**10:
        kom = l2.head
        while kom.next.value != 10**10:
            if com.next.value == kom.next.value:
                ...
