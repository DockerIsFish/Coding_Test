from collections import deque
from sys import stdin
N = int(stdin.readline())
fishes = []
for i in range(N):
    col = list(map(int, stdin.readline().split()))
    for j, fish in enumerate(col):
        if fish == 9:
            baby = [i, j]
            col[j] = 0
    fishes.append(col)
mv = [(0, 1), (1, 0), (0, -1), (-1, 0)]
bsize = 2
bcnt = 0


def bfs():
    visited = [[False] * N for _ in range(N)]
    q = deque([(0, baby[0], baby[1])])
    maxp = 10000
    candi = []
    while q:
        p, x, y = q.popleft()
        if visited[x][y]:
            continue
        if maxp < p:
            break
        elif 0 < fishes[x][y] < bsize:
                maxp = p
                candi.append((x, y, p))
        visited[x][y] = True
        for i, j in mv:
            xx = x + i
            yy = y + j
            if 0 <= xx < N and 0 <= yy < N and fishes[xx][yy] <= bsize and not visited[xx][yy]:
                q.append((p+1, xx, yy))
    if not candi:
        return False
    candi.sort()
    return candi[0]


answer = 0
while True:
    ret = bfs()
    if not ret:
        break
    x, y, p = ret
    answer += p
    baby = [x, y]
    fishes[x][y] = 0
    bcnt += 1
    if bcnt == bsize:
        bsize += 1
        bcnt = 0


print(answer)