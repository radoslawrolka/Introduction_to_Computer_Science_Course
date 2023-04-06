a = int(input("a: "))
b = int(input("b: "))
n = int(input("n: "))

print(str(a//b), ".", end="")
a %= b
while a > 0 and n > 0:
    a *= 10
    print(str(a//b), end="")
    a %= b
    n -= 1
