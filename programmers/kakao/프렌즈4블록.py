def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = " ".join(board[i]).split()
    board = list(map(list, zip(*board)))
    res = 1
    while res:
        res = find_block(board, m, n)
        answer += res
    return answer


def find_block(board, m, n):
    empty = set()
    for i in range(n - 1):
        for j in range(m - 1):
            if not board[i][j]:
                continue
            if board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][j + 1]:
                empty.add((i, j))
                empty.add((i + 1, j))
                empty.add((i, j + 1))
                empty.add((i + 1, j + 1))
    for i, j in empty:
        board[i][j] = 0
    for b in board:
        b.sort(key=lambda x: 0 if x == 0 else 1)
    return len(empty)
