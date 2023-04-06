def zmiana(liczba, system):
    wynik = ""
    znak = "0123456789ABCDEF"
    while liczba > 0:
        wynik = znak[liczba % system] + wynik
        liczba //= system
    return wynik


print(zmiana(9, 3))
