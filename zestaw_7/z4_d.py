class Lista:
    def __init__(self, val):
        self.value = val
        self.next = None

    def dodaj(self, val):
        while self is not None:
            if self.next is None:
                self.next = Lista(val)
                return "Dodano"
            self = self.next

    def wypisz(self):
        while self is not None:
            print(self.value, end=", ")
            self = self.next
        print()


# to odwraca w obrębie funkcji, nie orginalna liste
# aby obrocic liste trzeba: x = odwroc(x)
def odwroc(lis):
    if lis is None:
        return None
    if lis.next is None:
        return lis

    p = None
    q = lis
    curr = q.next

    while q is not None:
        q.next = p
        p = q
        q = curr
        if curr is not None:
            curr = curr.next
    return p


x = Lista(1)
x.dodaj(3)
x.dodaj(5)
x.dodaj(7)
x.dodaj(9)
x.dodaj(11)
x.dodaj(13)
x.wypisz()
#x = odwroc(x)
x.wypisz()

