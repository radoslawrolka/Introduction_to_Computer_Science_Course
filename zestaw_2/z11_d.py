def ciag_rosnacy(x):
    while x > 1:
        a = x % 10
        x = x//10
        if a <= x % 10:
            return False
    return True


print(ciag_rosnacy(345567))
