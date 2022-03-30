mv = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
fishes = []
orders = [0] * 17
for i in range(4):
    a, b, c, d, e, f, g, h = map(int, input().split())
    fishes.append([[a, b-1], [c, d-1], [e, f-1], [g, h-1]])
for i in range(4):
    for j in range(4):
        orders[fishes[i][j][0]] = [i, j]
global ans
ans = 0


def dfs(fishes, x, y, s, orders):
    global ans
    n, d = fishes[x][y]
    s += n
    fishes[x][y][0] = 17
    orders[n] = []
    for i in range(1, 17):
        if not orders[i]:
            continue
        cx, cy = orders[i]
        cn, cd = fishes[cx][cy]
        for j in range(8):
            nd = (cd + j) % 8
            tx, ty = cx + mv[nd][0], cy + mv[nd][1]
            if 0 <= tx < 4 and 0 <= ty < 4 and fishes[tx][ty][0] <= 16:
                tn, td = fishes[tx][ty]
                fishes[tx][ty] = [cn, nd]
                orders[cn] = [tx, ty]
                fishes[cx][cy] = [tn, td]
                orders[tn] = [cx, cy]
                break
    candi = []
    for i in range(1, 4):
        xx, yy = x + i*mv[d][0], y + i*mv[d][1]
        if (0 <= xx < 4 and 0 <= yy < 4) and fishes[xx][yy][0]:
            candi.append((xx, yy))
    if not candi:
        ans = max(ans, s)
        return
    for cx, cy in candi:
        tmp = []
        tmp_orders = orders[:]
        for i in range(4):
            tmp.append([])
            for j in range(4):
                tmp[-1].append(fishes[i][j][:])
        tmp[x][y][0] = 0
        dfs(tmp, cx, cy, s, tmp_orders)
    return


dfs(fishes, 0, 0, 0, orders)
print(ans)
