N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
mv = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]


def biba(d, s, maps, clouds):
    x, y = mv[d]
    xx, yy = x * s, y * s
    visited = [[False] * N for _ in range(N)]
    for i in range(len(clouds)):
        r, c = clouds[i]
        clouds[i][0] = (r + xx) % N
        clouds[i][1] = (c + yy) % N
    for r, c in clouds:  #rainning
        maps[r][c] += 1
        visited[r][c] = True
    cnts = []
    for r, c in clouds:  #water copy
        cnts.append(0)
        for x, y in diagonal:
            xx, yy = r + x, c + y
            if 0 <= xx < N and 0 <= yy < N and maps[xx][yy]:
                cnts[-1] += 1
    for idx, cloud in enumerate(clouds):
        r, c = cloud
        maps[r][c] += cnts[idx]
    clouds = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and maps[i][j] > 1:
                maps[i][j] -= 2
                clouds.append([i, j])
    return clouds


for i in range(M):
    d, s = map(int, input().split())
    clouds = biba(d-1, s, maps, clouds)
res = 0
for i in range(N):
    res += sum(maps[i])
print(res)