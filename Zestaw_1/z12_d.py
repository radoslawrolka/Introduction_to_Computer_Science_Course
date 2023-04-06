def nwd(x,y):
    while y:
        x,y = y, x%y
    return x

a = int(input("wpisz1: "))
b = int(input("wpisz2: "))
c = int(input("wpisz3: "))

b = nwd(a,b)
maxnwd = nwd(b,c)
print(maxnwd)
