def trzeciapotega(x):
    for i in range(10**(x-1), 10**x):
        suma = 0
        a = i
        while a > 0:
            suma += (a%10)**x
            a = a//10
        if suma == i:
            print(suma)


trzeciapotega(3)
