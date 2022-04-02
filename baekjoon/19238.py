from collections import deque

N, M, F = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))
drv = [i-1 for i in list(map(int, input().split()))]
spos = [] # start position
dpos = [] # destination
for i in range(M):
    a, b, c, d = map(int, input().split())
    spos.append([a-1, b-1])
    dpos.append([c-1, d-1])
mv = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def spath(des, src):
    q = deque([src])
    visited = [[False] * N for _ in range(N)]
    candi = []
    for d in range(N*N):
        next_q = deque([])
        while q:
            x, y = q.popleft()
            if visited[x][y]:
                continue
            if [x, y] in des:
                candi.append([x, y, d])
            visited[x][y] = True
            for i, j in mv:
                xx, yy = x + i, y + j
                if 0 <= xx < N and 0 <= yy < N and not visited[xx][yy] and not maps[xx][yy]:
                    next_q.append([xx, yy])
        if candi:
            break
        q = next_q
    candi.sort()
    if not candi:
        return -1, -1, F + 1
    return candi[0]


while spos:
    x, y, f = spath(spos, drv)
    F -= f
    if F < 0:
        break
    i = spos.index([x, y])
    drv = spos[i]
    del spos[i]
    des = dpos[i]
    del dpos[i]

    x, y, f = spath([des], drv)
    drv = des
    F -= f
    if F < 0:
        break
    F += f * 2
if F < 0:
    print(-1)
else:
    print(F)