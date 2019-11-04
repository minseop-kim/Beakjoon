h, w = map(int, input().split(' '))
board = []
for _ in range(h):
    board.append(list(input()))

w_b = ['W', 'B']
mini = h * w
for i in range(h - 7):
    for j in range(w - 7):
        white = 0
        black = 0

        for n in range(8):
            for m in range(8):
                if n % 2 == 0:
                    if board[i + n][j + m] != w_b[m % 2]:
                        white += 1
                    if board[i + n][j + m] != w_b[(m + 1) % 2]:
                        black += 1
                else:
                    if board[i + n][j + m] != w_b[(m + 1) % 2]:
                        white += 1
                    if board[i + n][j + m] != w_b[m % 2]:
                        black += 1

        if white < mini:
            mini = white
        if black < mini:
            mini = black

print(mini)