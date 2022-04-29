M, S = map(int, input().split())
fishes = {}
for i in range(4):
    for j in range(4):
        fishes[(i, j)] = []
mv = {0: (0, -1), 1: (-1, -1), 2: (-1, 0), 3: (-1, 1), 4: (0, 1), 5: (1, 1), 6: (1, 0), 7: (1, -1)}
grid = [[0] * 4 for _ in range(4)]
scents = [[0] * 4 for _ in range(4)]
for i in range(M):
    x, y, d = map(int, input().split())
    fishes[(x-1, y-1)].append(d-1)
    grid[x-1][y-1] += 1
origin = {}
s1, s2 = list(map(int, input().split()))
shark = [s1-1, s2-1]
smv = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 상좌하우


def move(fishes):
    nfishes = {}
    for i in range(4):
        for j in range(4):
            nfishes[(i, j)] = []
    for x, y in fishes:
        for d in fishes[(x, y)]:
            for i in range(8):
                xx, yy = mv[(d-i) % 8]
                nx, ny = x+xx, y+yy
                if 0 <= nx < 4 and 0 <= ny < 4 and shark != [nx, ny] and not scents[nx][ny]:
                    nfishes[(nx, ny)].append((d-i) % 8)
                    grid[x][y] -= 1
                    grid[nx][ny] += 1
                    break
            else:
                nfishes[(x, y)].append(d)
    return nfishes


def search():
    candi = []
    cnt = -1
    for i in range(4):
        xx1, yy1 = smv[i]
        nx1, ny1 = shark[0] + xx1, shark[1] + yy1
        if not(0 <= nx1 < 4 and 0 <= ny1 < 4):
            continue
        cnt1 = grid[nx1][ny1]
        for j in range(4):
            xx2, yy2 = smv[j]
            nx2, ny2 = nx1 + xx2, ny1 + yy2
            if not (0 <= nx2 < 4 and 0 <= ny2 < 4):
                continue
            cnt2 = cnt1 + grid[nx2][ny2]
            for k in range(4):
                xx3, yy3 = smv[k]
                nx3, ny3 = nx2 + xx3, ny2 + yy3
                if not (0 <= nx3 < 4 and 0 <= ny3 < 4):
                    continue
                cnt3 = cnt2 + grid[nx3][ny3]
                if nx3 == nx1 and ny3 == ny1:
                    cnt3 = cnt2
                if cnt3 > cnt:
                    cnt = cnt3
                    candi = [i, j, k]
    for d in candi:
        xx, yy = smv[d]
        shark[0] += xx
        shark[1] += yy
        if grid[shark[0]][shark[1]] > 0:
            scents[shark[0]][shark[1]] = 3
        grid[shark[0]][shark[1]] = 0
        fishes[tuple(shark)] = []
    return


def rm_scent():
    for i in range(4):
        for j in range(4):
            if scents[i][j] > 0:
                scents[i][j] -= 1


def fishcopy():
    for fish, v in origin.items():
        x, y = fish
        grid[x][y] += len(v)
        fishes[(x, y)].extend(v)
    return


for i in range(S):
    for j in range(4):
        for k in range(4):
            origin[(j, k)] = fishes[(j, k)][:]
    fishes = move(fishes)
    search()
    rm_scent()
    fishcopy()
res = 0
for i in range(4):
    res += sum(grid[i])
print(res)