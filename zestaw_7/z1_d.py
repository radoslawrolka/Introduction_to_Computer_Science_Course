"""
1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
struktury listy odsyłaczowej.
- czy element należy do zbioru
- wstawienie elementu do zbioru
- usunięcie elementu ze zbioru
"""


class Lista:
    def __init__(self, val):
        self.value = val
        self.next = None

    def czy_zawiera(self, val):
        while self is not None:
            if self.value == val:
                return True
            self = self.next
        return False

    def dodaj(self, val):
        while self is not None:
            if self.next is None:
                self.next = Lista(val)
                return "Dodano"
            self = self.next

    def usun(self, val):
        while self.next is not None:
            if self.next.value == val:
                self.next = self.next.next
                return "Usunieto"
            self = self.next
        return "Brak elementu w liscie"

    def wypisz(self):
        while self is not None:
            print(self.value, end=", ")
            self = self.next
        print()


lis = Lista(3)
lis.dodaj(5)
lis.dodaj(9)
lis.wypisz()
print(lis.usun(9))
print(lis.czy_zawiera(9))
lis.wypisz()
