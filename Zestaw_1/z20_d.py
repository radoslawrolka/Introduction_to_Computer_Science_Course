import math

a = int(input("wpisz1: "))
b = int(input("wpisz2: "))

x = math.sqrt(a*b)
y = (a+b)/2

eps = 1e-5
while abs(x-y) > eps:
    a, b = math.sqrt(a*b), (a+b)/2

print(a)
