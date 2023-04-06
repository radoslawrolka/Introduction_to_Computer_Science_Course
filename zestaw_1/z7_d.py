szukana = int(input("wpisz: "))

prev = 1
curr = 1
next = 0
while True:
    next = prev + curr
    prev = curr
    curr = next
    if curr * prev == szukana:
        print("Tak: " + str(prev) + " " + str(curr))
        break
    elif curr * prev > szukana:
        print("Nie")
        break