szuk = int(input("szukana: "))

flag = 0
suma = 0
increment = 1
while suma < szuk:
       flag += 1
       suma += increment
       increment += 2

print("pierwiastek: " + str(flag))
