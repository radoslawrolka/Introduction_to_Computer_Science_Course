def fib(num):
    a = 1
    b = 1
    while a*b <= num:
        a, b = b, a + b
        if a*b == num:
            return True
    return False


print(fib(715))
