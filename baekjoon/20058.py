from collections import deque

N, Q = map(int, input().split())
NN = 2 ** N
A = [list(map(int, input().split())) for _ in range(NN)]
L = list(map(int, input().split()))
mv = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def rotate(l, A):
    mA = [[0] * NN for _ in range(NN)]
    for r in range(0, NN, l):
        for c in range(0, NN, l):
            for x in range(r, r + l):
                for y in range(c, c + l):
                    #px, py = r + l // 2, c + l // 2
                    #dx, dy = x - px, y - py
                    #nx, ny = int(px + dy), int(py - dx)
                    mA[r - c + y][r + c + l - x - 1] = A[x][y]
    candi = []
    for x in range(NN):
        for y in range(NN):
            cnt = 0
            for i, j in mv:
                xx, yy = x + i, y + j
                if 0 <= xx < NN and 0 <= yy < NN and mA[xx][yy]:
                    cnt += 1
            if cnt < 3:
                candi.append((x, y))
    for x, y in candi:
        if mA[x][y]:
            mA[x][y] -= 1
    return mA


for l in L:
    A = rotate(2 ** l, A)
total = 0
for a in A:
    total += sum(a)
maxsize = 0
for i in range(NN):
    for j in range(NN):
        if not A[i][j]:
            continue
        q = deque([(i, j)])
        tmpmax = 0
        while q:
            x, y = q.popleft()
            if not A[x][y]:
                continue
            A[x][y] = 0
            tmpmax += 1
            for mx, my in mv:
                nx, ny = x + mx, y + my
                if 0 <= nx < NN and 0 <= ny < NN and A[nx][ny]:
                    q.append((nx, ny))
        maxsize = max(maxsize, tmpmax)
print(total)
print(maxsize)