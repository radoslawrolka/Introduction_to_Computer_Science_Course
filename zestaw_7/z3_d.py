class Lista:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def wypisz(self):
        while self is not None:
            print(self.value, end=", ")
            self = self.next
        print()


def dodaj(lis, val):
    if lis.value is None:
        lis.value = val
    while lis.next is not None:
        lis = lis.next
    lis.next = Lista(val)


def sortuj_i(l1, l2):
    l3 = Lista()
    s = l3
    while l1 is not None and l2 is not None:
        if l1.value < l2.value:
            l3.value = l1.value
            l3.next = Lista()
            l1 = l1.next
        else:
            l3.value = l2.value
            l3.next = Lista()
            l2 = l2.next
        l3 = l3.next
    if l1 is None:
        while l2 is not None:
            l3.value = l2.value
            l2 = l2.next
            l3.next = Lista()
            l3 = l3.next
    if l2 is None:
        while l1 is not None:
            l3.value = l1.value
            l1 = l1.next
            l3.next = Lista()
            l3 = l3.next
    return s


def sortuj_r(l1, l2, s="dupa", l4=0):
    if s == "dupa":
        l4 = Lista()
        s = l4
    if l1 is None and l2 is None:
        return s
    if l2 is None:
        l4.next = Lista(l1.value)
        l4 = l4.next
        return sortuj_r(l1.next, l2, s, l4)
    elif l1 is None:
        l4.next = Lista(l2.value)
        l4 = l4.next
        return sortuj_r(l1, l2.next, s, l4)
    else:
        if l1.value < l2.value:
            l4.next = Lista(l1.value)
            l4 = l4.next
            return sortuj_r(l1.next, l2, s, l4)
        else:
            l4.next = Lista(l2.value)
            l4 = l4.next
            return sortuj_r(l1, l2.next, s, l4)


lis1 = Lista(1)
dodaj(lis1, 3)
dodaj(lis1, 5)
lis2 = Lista(2)
dodaj(lis2, 4)
dodaj(lis2, 6)
lis3 = sortuj_i(lis1, lis2)
lis4 = sortuj_r(lis1, lis2)
lis3.wypisz()
lis4.wypisz()
