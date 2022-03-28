N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
pos = [[[] for _ in range(N)] for _ in range(N)]
pieces = []
t = [0, 0, 2, 1, 3]
for k in range(K):
    r, c, m = map(int, input().split())
    pieces.append([r-1, c-1, t[m]])
    pos[r-1][c-1].append(k)
mv = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def play():
    for k in range(K):
        r, c, m = pieces[k]
        rr, cc = r + mv[m][0], c + mv[m][1]
        if not (0 <= rr < N and 0 <= cc < N) or board[rr][cc] == 2: # 밖에 나가는 것과 파란색일 case
            rr, cc = rr - 2 * mv[m][0], cc - 2 * mv[m][1]
            pieces[k][2] = (m + 2) % 4
            if not (0 <= rr < N and 0 <= cc < N) or board[rr][cc] == 2: # 한번더 밖에 나가는 것과 파란색일 case
                pieces[k][2] = (m + 2) % 4
                continue
        idx = pos[r][c].index(k)
        tmp = pos[r][c][idx:]
        pos[r][c] = pos[r][c][:idx]
        if board[rr][cc]:
            tmp = list(reversed(tmp))
        for p in tmp:
            pieces[p][0] = rr
            pieces[p][1] = cc
            pos[rr][cc].append(p)
        if len(pos[rr][cc]) > 3:
            return True
    return False


for i in range(1000):
    if play():
        print(i+1)
        break
else:
    print(-1)