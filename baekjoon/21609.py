from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]  # empty: -2
mv = ((1, 0), (0, 1), (-1, 0), (0, -1))
global score
score = 1


def pulldown(grid):
    ngrid = [[-2] * N for _ in range(N)]
    for j in range(N):
        idx = N - 1
        for i in range(N - 1, -1, -1):
            if grid[i][j] >= 0:
                ngrid[idx][j] = grid[i][j]
                idx -= 1
            elif grid[i][j] == -1:
                ngrid[i][j] = -1
                idx = i - 1
    return ngrid


def rotate(grid):
    ngrid = []
    for j in range(N - 1, -1, -1):
        tmp = []
        for i in range(N):
            tmp.append(grid[i][j])
        ngrid.append(tmp)
    return ngrid


def cal_score(grid):
    global score
    visited = [[False] * N for _ in range(N)]
    maxsize = 0
    maxrainbow = 0
    large_block = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] or grid[i][j] <= 0:
                continue
            q = deque([(i, j)])
            candi = []
            rainbow = 0
            size = 0
            color = grid[i][j]
            while q:
                x, y = q.popleft()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                size += 1
                candi.append((x, y))
                for dx, dy in mv:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < N and 0 <= yy < N and not visited[xx][yy] and grid[xx][yy] in [0, color]:
                        q.append((xx, yy))
            for x, y in candi:
                if not grid[x][y]:
                    visited[x][y] = False
                    rainbow += 1
            if size > 1:
                if size > maxsize:
                    maxsize = size
                    large_block = candi
                    maxrainbow = rainbow
                elif size == maxsize:
                    if rainbow >= maxrainbow:
                        large_block = candi
                        maxrainbow = rainbow
    for x, y in large_block:
        grid[x][y] = -2
    score = maxsize ** 2
    return grid


total = 0
while score:
    grid = cal_score(grid)
    total += score
    grid = pulldown(grid)
    grid = rotate(grid)
    grid = pulldown(grid)
print(total)