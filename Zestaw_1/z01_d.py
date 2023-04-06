prev = 1
curr = 1
next = 0
while prev + curr <(1000000):
    next = prev + curr
    prev = curr
    curr = next
    print(next)