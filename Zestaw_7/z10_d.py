"""
10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
powstać nowa lista.
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def dodaj(self, val):
        x = self.head
        if x is None:
            self.head = Node(val)
        else:
            while x.next is not None:
                x = x.next
            x.next = Node(val)

    def wypisz(self):
        a = self.head
        while a is not None:
            print(a.value)
            a = a.next
        print("--------")

    def reverse(self):
        if self is None:
            return None
        if self.head.next is None:
            return self

        p = None
        q = self.head
        curr = q.next

        while q is not None:
            q.next = p
            p = q
            q = curr
            if curr is not None:
                curr = curr.next
        self.head = p

    def sumuj(self, l1, l2):
        l1.reverse()
        l2.reverse()
        b = Linklist()
        s1 = l1.head
        s2 = l2.head
        while s1 is not None and s2 is not None:
            b.dodaj(s1.value + s2.value)
            s1 = s1.next
            s2 = s2.next
        while s1 is not None:
            b.dodaj(s1.value)
            s1 = s1.next
        while s2 is not None:
            b.dodaj(s2.value)
            s2 = s2.next
        c = b.head
        while c.next is not None:
            if c.value > 9:
                c.value -= 10
                c.next.value += 1
            c = c.next
        if c.value > 9:
            c.value -= 10
            c.next = Node(1)
        b.reverse()
        return b


x = Linklist()
x.dodaj(8)
x.dodaj(1)
x.dodaj(3)
x.dodaj(5)
#x.wypisz()
y = Linklist()
y.dodaj(2)
y.dodaj(4)
y.dodaj(6)
y.dodaj(8)
#y.wypisz()
z = x.sumuj(x, y)
z.wypisz()
