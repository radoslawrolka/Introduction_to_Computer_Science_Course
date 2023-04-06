"""
32. Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w
liście ułożone są według rosnących potęg. Proszę napisać funkcję
obliczającą różnicę dwóch dowolnych wielomianów. Wielomiany reprezentowane
są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo
utworzonej listy reprezentującej wielomian wynikowy. Listy wejściowe
powinny pozostać niezmienione.
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


def odejmij(l1, l2):
    lw = Linklist()
    com = l1.head
    kom = l2.head
    while com.value != 10**10 and kom.value != 10**10:
        lw.add(com.value - kom.value)
        com = com.next
        kom = kom.next
    if com.value == 10**10:
        while kom.value != 10**10:
            lw.add(-1 * kom.value)
            kom = kom.next
    else:
        while com.value != 10**10:
            lw.add(kom.value)
            com = com.next
    return lw
