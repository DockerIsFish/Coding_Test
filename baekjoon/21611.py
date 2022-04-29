N, M = map(int, input().split())
beads = [list(map(int, input().split())) for _ in range(N)]
magic = []
pos = {}
mv = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
j = 0
p = 1
x, y = N//2, N//2
scores = {1: 0, 2: 0, 3: 0}
for i in range(N//2*4 + 1):
    if i % 2 == 0:
        j += 1
    if i % 4 == 0:
        d = 3
    elif i % 4 == 1:
        d = 2
    elif i % 4 == 2:
        d = 4
    else:
        d = 1
    for k in range(j):
        xx, yy = mv[d]
        x, y = x + xx, y + yy
        pos[p] = (x, y)
        p += 1
del pos[N*N]


def pullBead():
    cnt = 0
    for i in range(1, N * N):
        x, y = pos[i]
        p = beads[x][y]
        if p > 0:
            cnt += 1
            x, y = pos[cnt]
            beads[x][y] = p
    for i in range(cnt + 1, N * N):
        x, y = pos[i]
        beads[x][y] = 0
    return


def ice(d, s):
    x, y = N//2, N//2
    xx, yy = mv[d]
    for i in range(s):
        x += xx
        y += yy
        beads[x][y] = 0
    pullBead()
    return


def explode():
    n = -1
    cnt = 0
    res = False
    for i in range(1, N*N):
        x, y = pos[i]
        cur = beads[x][y]
        if cur == 0:
            break
        if n == cur:
            cnt += 1
        else:
            if cnt >= 4:
                for j in range(1, cnt+1):
                    x, y = pos[i-j]
                    beads[x][y] = 0
                scores[n] += cnt
                res = True
            n = cur
            cnt = 1
    if cnt >= 4:
        for j in range(cnt):
            x, y = pos[i-j]
            beads[x][y] = 0
        scores[n] += cnt
        res = True
    return res


def makeBeads():
    nbeads = [[0] * N for _ in range(N)]
    n = beads[N//2][N//2-1]
    nbeads[N//2+1][N//2-1] = n
    cur_idx = 1
    for i in range(1, N*N):
        x, y = pos[i]
        cur = beads[x][y]
        if cur == 0:
            break
        if cur == n:
            x, y = pos[cur_idx]
            nbeads[x][y] += 1
        else:
            cur_idx += 2
            if cur_idx >= N*N:
                break
            x, y = pos[cur_idx]
            nbeads[x][y] += 1
            x, y = pos[cur_idx + 1]
            nbeads[x][y] = cur
            n = cur
    return nbeads


for i in range(M):
    d, s = map(int, input().split())
    ice(d, s)
    while explode():
        pullBead()
    beads = makeBeads()
print(scores[1] + scores[2]*2 + scores[3]*3)