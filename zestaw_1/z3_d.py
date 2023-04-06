def zad3(sum_to_find):
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


print(zad3(26))
