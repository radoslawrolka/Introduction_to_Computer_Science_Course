def suma_podciagu_fib(sum_to_find):
    curr_sum = 1

    smallest, second_smallest = 1, 1
    second_largest, largest = 0, 1

    while smallest <= sum_to_find:
        second_largest, largest = largest, second_largest + largest
        curr_sum += largest
        if curr_sum == sum_to_find:
            return True
        while curr_sum > sum_to_find:
            curr_sum -= smallest
            smallest, second_smallest = second_smallest, smallest + second_smallest
            if curr_sum == sum_to_find:
                return True
    return False


def brak_podciągu(x):
    while True:
        if suma_podciagu_fib(x+1) == 0:
            return x+1
        else:
            x += 1


print(brak_podciągu(14))
