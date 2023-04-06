"""
26. Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w
drugiej. Do funkcji należy przekazać wskazania na pierwsze elementy obu
list, funkcja powinna zwrócić wartość logiczną.
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

    def moc(self):
        ile = 0
        com = self.head
        while com.next is not None:
            ile += 1
            com = com.next
        return ile


def is_inside(l1, l2):
    # ktoras jest pusta
    if l1.head.value == 10**10 or l2.head.value == 10**10:
        return True
    # reszta
    if l1.moc() > l2.moc():
        s1 = l1.head
        s2 = l2.head
        b1 = l1.head
        b2 = l2.head
    else:
        s2 = l1.head
        s1 = l2.head
        b2 = l1.head
        b1 = l2.head
    flag = 0

    while s2.value != 10**10:

        if s1.value == 10**10:
            return False
        else:
            if s1.value == s2.value:
                if flag == 0:
                    flag = 1
                    b1 = s1.next
                    b2 = s2.next
                s1 = s1.next
                s2 = s2.next
            else:
                if flag == 0:
                    s1 = s1.next
                else:
                    flag = 0
                    s1 = b1
                    s2 = b2
    return True


x = Linklist()
x.add(1)
x.add(2)
x.add(3)
x.add(4)
y = Linklist()
y.add(1)
y.add(2)
z = Linklist()
z.add(2)
z.add(3)
v = Linklist()
v.add(3)
v.add(4)
x.print()
print(is_inside(x, y))
print(is_inside(x, z))
print(is_inside(x, v))
print(is_inside(y, v))
