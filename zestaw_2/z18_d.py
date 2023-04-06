a0 = 0
a1 = 1

b0 = 2

b1 = b0 + 2 * a0

if int(input("wpisz: ")) == a0:
    print(b0)
else:
    print("To nie a0, koniec")
    exit()

while int(input("wpisz: ")) == a1:
    print(b1)

    a0 = a1
    a1 = a1 - b1 * a0
    b0 = b1
    b1 = b1 + 2*a0
