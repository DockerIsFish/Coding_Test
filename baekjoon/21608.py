from collections import defaultdict
N = int(input())
mv = ((0, 1), (1, 0), (-1, 0), (0, -1))
room = [[0] * N for _ in range(N)]
pos = {i:0 for i in range(1, N**2 + 1)}
dictfri = {}
for _ in range(N*N):
    stus = list(map(int, input().split()))
    cur = stus[0]
    fris = stus[1:]
    dictfri[cur] = fris
    candi = defaultdict(int)
    for idx, fri in enumerate(fris):
        if not pos.get(fri):
            continue
        fx, fy = pos[fri]
        for dx, dy in mv:
            cx, cy = fx + dx, fy + dy
            if 0 <= cx < N and 0 <= cy < N and not room[cx][cy]:
                candi[(cx, cy)] += 1
    if candi:
        vs = list(candi.values())
        m = max(vs)
        if vs.count(m) == 1:
            idx = vs.index(m)
            ks = list(candi.keys())
            x, y = ks[idx]
            pos[cur] = (x, y)
            room[x][y] = cur
            continue
        else:
            tmp = []
            for k, v in candi.items():
                if v == m:
                    tmp.append(k)
            candi = []
            for i, j in tmp:
                if room[i][j]:
                    continue
                cnt = 0
                for dx, dy in mv:
                    x, y = i + dx, j + dy
                    if 0 <= x < N and 0 <= y < N and not room[x][y]:
                        cnt += 1
                candi.append((cnt, i, j))
    else:
        candi = []
        for i in range(N):
            for j in range(N):
                if room[i][j]:
                    continue
                cnt = 0
                for dx, dy in mv:
                    x, y = i+dx, j+dy
                    if 0 <= x < N and 0 <= y < N and not room[x][y]:
                        cnt += 1
                candi.append((cnt, i, j))
    candi.sort(key=lambda x: (-x[0], x[1], x[2]))
    x, y = candi[0][1], candi[0][2]
    room[x][y] = cur
    pos[cur] = (x, y)
score = [0, 1, 10, 100, 1000]
ans = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        cur = room[i][j]
        fris = dictfri[cur]
        for dx, dy in mv:
            x, y = i + dx, j + dy
            if 0 <= x < N and 0 <= y < N and room[x][y] in fris:
                cnt += 1
        ans += score[cnt]
print(ans)