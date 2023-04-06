"""
20. Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
Krańce przedziałów określa uporządkowana para liczb całkowitych. Proszę
napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]
"""


class Node:
    def __init__(self, fir, las):
        self.first = fir
        self.last = las
        self.next = None


class Linklist:
    def __init__(self):
        self.head = Node(10 ** 10, 10 ** 10)

    def insert(self, fir, las):
        # always first
        new = Node(fir, las)
        new.next = self.head
        self.head = new

    def print(self):
        com = self.head
        while com.first != 10 ** 10:
            print(com.first, com.last)
            com = com.next
        print("-----")

    def zad(self):
        com = self.head
        if com.first == 10 ** 10 or com.next.first == 10 ** 10:
            return
        while com.first != 10**10:
            if com.next.first == 10**10:
                break
            kom = com
            while kom.first != 10**10:
                if kom.next.first == 10**10:
                    break
                f = 0
                if kom.next.first <= com.first <= kom.next.last:
                    com.first = min(com.first, kom.next.first)
                    f = 1
                if kom.next.last >= com.last >= kom.next.first:
                    com.last = max(com.last, kom.next.last)
                    f = 1
                if com.first <= kom.next.first and com.last >= kom.next.last:
                    f = 1
                if f == 1:
                    kom.next = kom.next.next
                kom = kom.next
            com = com.next


x = Linklist()
x.insert(15, 19)
x.insert(2, 5)
x.insert(7, 11)
x.insert(8, 12)
x.insert(5, 6)
x.insert(13, 17)
x.print()
x.zad()
x.print()
