"""
31. Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza
powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać
wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
powinna zwrócić liczbę usuniętych elementów.
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Linklist:
    def __init__(self):
        self.head = Node(10**10)

    def print(self):
        com = self.head
        while com.value != 10**10:
            print(com.value)
            com = com.next

    def add(self, val):
        com = self.head
        if com.value == 10**10:
            new = Node(val)
            new.next = self.head
            self.head = new
        while com.next.value != 10**10:
            com = com.next
        new = Node(val)
        new.next = com.next
        com.next = new


def zad(l1, lp, lm):
    ile = 0
    com = l1.head
    while l1.value != 10**10:
        if l1.value > 0:
            lp.add(l1.value)
        elif l1.value < 0:
            lm.add(l1.value)
        else:
            ile += 1
    return lp, lm, ile
