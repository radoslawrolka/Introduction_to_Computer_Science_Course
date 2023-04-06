def czyunikalna(x):
    last = x%10
    x = x//10
    while x > 0:
        if last == x%10:
            return False
        x = x//10
    return True


print(czyunikalna(3654))
