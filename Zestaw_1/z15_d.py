import math

precision = 0.000000001
x = math.sqrt(0.5)
y = math.sqrt(0.5)
while abs(x-x*y)>precision:
    y = math.sqrt(0.5 + 0.5 * y)
    x *= y
print("pi= " + str(2/x))