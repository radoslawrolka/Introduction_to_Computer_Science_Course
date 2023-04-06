a = int(input("wpisz: "))
b = int(input("wpisz: "))

print(a // b, ".", end="")
c = a / b
c = str(c - a // b)

flag = 0
for i in range(3, len(c)):
    for j in range(i + 1, len(c)):
        if c[i] == c[j]:
            print(c[2:(i - 1)] + "(" + c[i - 1:j] + ")")
            flag = 1
            break
    if flag == 1:
       break


def funkcja(a, b):
    wynik = ""
    tablica_reszt = [] * b
    reszta = a % b
    while reszta != 0 and tablica_reszt[reszta] == None:
        tablica_reszt[reszta] = len(wynik)
        reszta *= 10
        iloraz = reszta // b
        wynik += str(iloraz)
        reszta %= b
    if reszta == 0:
        return a / b
    else:
        return str(a // b) + "." + str(wynik[:tablica_reszt[reszta]]) + "(" + str(wynik[tablica_reszt[reszta]:]) + ")"
