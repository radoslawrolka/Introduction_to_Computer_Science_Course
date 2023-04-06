def nwd(x,y):
    while y:
        x,y = y, x%y
    return x

def nww(x,y):
    return (x*y)/nwd(x,y)

a = int(input("wpisz1: "))
b = int(input("wpisz2: "))
c = int(input("wpisz3: "))

b = nww(a,b)
minnww = nww(b,c)
print(minnww)