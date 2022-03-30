N = int(input())
bboard = [[0] * 4 for _ in range(6)]
gboard = [[0] * 4 for _ in range(6)]
global score
score = 0


def cal(t, x, y, board):
    global score
    if t == 1:
        for i in range(2, 7):
            if i >= 6 or board[i][y]:
                board[i - 1][y] = 1
                break
    elif t == 2:
        for i in range(2, 7):
            if i >= 6 or (board[i][y] or board[i][y+1]):
                board[i - 1][y] = 1
                board[i - 1][y + 1] = 1
                break
    else:
        for i in range(2, 7):
            if i >= 6 or (board[i][y] or board[i-1][y]):
                board[i - 1][y] = 1
                board[i - 2][y] = 1
                break
    i = 5
    while i > 1:
        if board[i] == [1, 1, 1, 1]:
            score += 1
            board.pop(i)
            board = [[0, 0, 0, 0]] + board
            i += 1
        i -= 1
    cnt = 0
    for i in range(2):
        if 1 in board[i]:
            cnt += 1
    for i in range(cnt):
        board.pop()
        board = [[0, 0, 0, 0]] + board
    return board


for _ in range(N):
    t, x, y = map(int, input().split())
    if t == 1:
        gboard = cal(1, x, y, gboard)
        bboard = cal(1, y, x, bboard)
    else:
        gboard = cal(t, x, y, gboard)
        bboard = cal(t + (-2*(t%2)) + 1, y, x, bboard)


blocknum = 0
for i in range(2, 6):
    blocknum += sum(bboard[i])
    blocknum += sum(gboard[i])
print(score)
print(blocknum)