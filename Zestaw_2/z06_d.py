import math

def dzielniki(x):
    i = 1
    max = x-1
    maxa = 1
    maxb = i
    while i <= math.sqrt(x):
        if x%i == 0:
            if x//i - i < max:
                max = x//i - i
                maxa = i
                maxb = x//i
        i += 1
    return maxa, maxb


print(dzielniki(120))
