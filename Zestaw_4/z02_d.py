def czy_nieparzyste(x):
    while x > 0:
        if x%2 == 0:
            return False
        x //= 10
    return True


def z2(t):
    for row in t:
        flag = 0
        for number in row:
            if czy_nieparzyste(number):
                flag = 1
                break
        if flag == 0:
            return False
    return True


x = [[1,2,3,4], [2]]
print(z2(x))
