def calc_sum(board, rows, columns, x1, y1, x2, y2):
    if x1 == x2:
        return columns[x1] + rows[y1] + rows[y2] - board[y1][x1] - board[y2][x2]
    if y1 == y2:
        return columns[x1] + columns[x2] + rows[y1] - board[y1][x1] - board[y2][x2]
    return columns[x1] + columns[x2] + rows[y1] + rows[y2] - board[y1][x1] * 2 - board[y2][x2] * 2 - board[y1][x1] - board[y2][x1]


def zad20(board):
    n = len(board)

    rows = [0]*n
    columns = [0]*n
    best = None
    best_sum = 0

    for i in range(n):
        for j in range(n):
            rows[i] += board[i][j]
            columns[i] += board[j][i]

    for x1 in range(n):
        for y1 in range(n):
            for x2 in range(n):
                for y2 in range(n):
                    if x1 == x2 and y1 == y2:
                        continue
                    if calc_sum(board, rows, columns, x1, y1, x2, y2) > best_sum:
                        best = (x1, y1, x2, y2)
                        best_sum = calc_sum(board, rows, columns, x1, y1, x2, y2)
    return best


x = [[1,2,9,4,5,6,7,8] for _ in range(8)]
for i in range(8):
    print(x[i])
print(zad20(x))
