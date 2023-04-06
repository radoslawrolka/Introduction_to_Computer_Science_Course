prev = 1
curr = 1
next = 0
while abs(curr/prev - (prev + curr)/curr) > 0:
    next = prev + curr
    prev = curr
    curr = next
    print(curr/prev)