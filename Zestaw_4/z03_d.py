def czy_parzyste(x):
    while x > 0:
        if x % 2 == 0:
            return True
        x //= 10
    return False


def z3(t):
    for row in t:
        flag = 0
        for number in row:
            if czy_parzyste(number) == False:
                flag = 1
                break
        if flag == 0:
            return True
    return False


x = [[1, 2, 3, 4], [2,2,2,2,13,2]]
print(z3(x))
