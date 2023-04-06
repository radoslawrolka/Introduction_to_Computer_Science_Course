szukana = int(input("wpisz: "))

x = (1 / 3) * (2 * szukana + (szukana / szukana ** 2))
while abs(x - (1 / 3) * (2 * x + (szukana / x ** 2))) > 0:
    x = (1 / 3) * (2 * x + (szukana / x ** 2))
print(x)
