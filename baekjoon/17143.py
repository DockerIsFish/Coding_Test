R, C, M = map(int, input().split())
sharks = [[False for i in range(C)] for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[r - 1][c - 1] = (s, d - 1, z)
ans = 0


def cal_mv(sharks):
    new_pos = [[False for i in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if not sharks[i][j]:
                continue
            s, d, z = sharks[i][j]
            if d == 0 or d == 1:
                if d == 0:
                    p = -s + i
                else:
                    p = s + i
                d = (p // (R - 1) + d) % 2
                p %= (2 * (R - 1))
                if p > (R - 1):
                    p = 2 * (R - 1) - p
                if not new_pos[p][j] or new_pos[p][j][2] < z:
                    new_pos[p][j] = (s, d, z)
            else:
                if d == 3:
                    p = -s + j
                else:
                    p = s + j
                if (p // (C - 1)) % 2:
                    d = (d - 1) % 2 + 2
                p %= (2 * (C - 1))
                if p > (C - 1):
                    p = 2 * (C - 1) - p
                if not new_pos[i][p] or new_pos[i][p][2] < z:
                    new_pos[i][p] = (s, d, z)
    return new_pos


for c in range(C):
    for i in range(R):
        if sharks[i][c]:
            ans += sharks[i][c][2]
            sharks[i][c] = False
            break
    sharks = cal_mv(sharks)
print(ans)
