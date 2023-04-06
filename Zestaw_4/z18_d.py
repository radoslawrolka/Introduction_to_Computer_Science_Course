def z18(tab):
    n = len(tab)
    max_sum = 0
    for i in range(n):
        sum_pion = 0
        sum_poziom = 0
        for j in range(n):
            if j > 10:
                max_sum = max(max_sum, sum_pion, sum_poziom, sum_pion - tab[j - 10][i] + tab[j][i], sum_poziom - tab[i][j - 10] + tab[i][j])
                sum_pion -= tab[j - 10][i]
                sum_poziom -= tab[i][j - 10]
            sum_pion += tab[j][i]
            sum_poziom += tab[i][j]
        max_sum = max(max_sum, sum_pion, sum_poziom)
    return max_sum


x = [ [1,2,3,4,5,6,7,8,9,10,11] for _ in range(11)]
print(z18(x))
