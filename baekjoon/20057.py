N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]


def trans(mv):
    new_mv = []
    for i, j in mv:
        new_mv.append((-j, i))
    return new_mv


mv = [(0, -1), (1, 0), (0, 1), (-1, 0)]
pos = [[(-2, -1), (-1, -2), (-1, -1), (-1, 0), (0, -3), (1, -2), (1, -1), (1, 0), (2, -1), (0, -2)]]
pos.append(trans(pos[-1]))
pos.append(trans(pos[-1]))
pos.append(trans(pos[-1]))
per = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02]
global ans
ans = 0


def cal(x, y, dx, dy, pos):
    global ans
    A = grid[dx][dy]
    grid[dx][dy] = 0
    total = 0
    for i in range(9):
        xx, yy = pos[i]
        nx, ny = x + xx, y + yy
        sand = int(A * per[i])
        if 0 <= nx < N and 0 <= ny < N:
            grid[nx][ny] += sand
            total += sand
        else:
            ans += sand
            total += sand
    nx, ny = x + pos[9][0], y + pos[9][1]
    if 0 <= nx < N and 0 <= ny < N:
        grid[nx][ny] += A - total
    else:
        ans += A - total
    return True


l = 0
d = -1
x, y = N // 2, N // 2
for i in range(2 * (N - 1) + 1):
    d = (d + 1) % 4
    if d % 2 == 0:
        l += 1
    for j in range(l):
        if x | y == 0:
            break
        dx = x + mv[d][0]
        dy = y + mv[d][1]
        cal(x, y, dx, dy, pos[d])
        x, y = dx, dy
print(ans)