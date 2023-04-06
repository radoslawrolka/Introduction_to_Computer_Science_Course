import math

szukana = int(input("wpisz: "))

flag = 0
if szukana == 2 or szukana == 3:
    print("Tak")
    flag = 1
elif szukana % 2 == 0 or szukana % 3 == 0 or szukana <= 1:
    print("Nie")
    flag = 1
else:
    x = 5
    while x < math.sqrt(szukana) + 1:
        if szukana % x == 0:
            print("Nie")
            flag = 1
            break
        x += 2
        if szukana % x == 0:
            print("Nie")
            flag = 1
            break
        x += 4

if flag == 0:
    print("Tak")
