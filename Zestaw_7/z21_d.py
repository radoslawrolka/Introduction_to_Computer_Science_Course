"""
21. Kolejne elementy listy o zwiększającej się wartości pola val nazywamy
podlistą rosnącą. Proszę napisać funkcję, która usuwa z listy wejściowej
najdłuższą podlistę rosnącą. Warunkiem usunięcia jest istnienie w liście
dokładnie jednej najdłuższej podlisty rosnącej.
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Linklist:
    def __init__(self):
        self.head = Node(10**10)

    def insert(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    def print(self):
        com = self.head
        while com.value != 10**10:
            print(com.value)
            com = com.next
        print("-----")

    def zad(self):
        com = self.head
        m_ile = 1
        m_hed = com
        ile = 1
        s = com
        while com.next.value != 10**10:
            if com.value < com.next.value:
                ile += 1
                if m_ile < ile:
                    m_ile = ile
                    m_hed = s
            else:
                ile = 1
                s = com.next
            com = com.next

        if m_ile > 1:
            com = self.head
            if com == m_hed:
                while m_ile > 0:
                    self.head = self.head.next
                    m_ile -= 1
            else:
                while com.next != m_hed:
                    com = com.next
                while m_ile > 0:
                    com.next = com.next.next
                    m_ile -= 1


x = Linklist()
x.insert(6)
x.insert(5)
x.insert(4)
x.insert(3)
x.insert(2)
x.insert(1)
x.insert(4)
x.insert(3)
x.insert(2)
x.insert(1)
x.print()
x.zad()
x.print()
