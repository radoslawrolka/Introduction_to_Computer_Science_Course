precision = 0.00001

def pierwiastek(x, precision):
    a = 1
    b = x
    while abs(a-b)>=precision:
        a = (a+b)/2
        b = x/a
    return (a+b)/2

liczba = int(input("wpisz: "))
print(pierwiastek(liczba, precision))