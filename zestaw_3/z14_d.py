import random


def prob(n):
    year = [-1 for _ in range(366)]
    counter = 0
    ile_prob = 10000
    for i in range(ile_prob):    #ilosc prób
        for j in range(n):  #ilosc osob (20-40)
            birthday = random.randint(0, 365)
            if year[birthday] == i:
                counter += 1
                break
            year[birthday] = i
    return counter/ile_prob


print(prob(76))
