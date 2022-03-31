N, M, K = map(int, input().split())
prior = []
sharks = {} # x, y, direction
pos = []
# 1,2,3,4 위,아래,왼쪽,오른
for i in range(N):
    s = map(int, input().split())
    pos.append([])
    for j, n in enumerate(s):
        if n:
            pos[-1].append([n, K]) # [shark num, remaining time]
            sharks[n] = [i, j]
        else:
            pos[-1].append([0, 0])
for i, d in enumerate(list(map(int, input().split()))):
    sharks[i+1].append(d-1)
for i in range(1, M+1):
    prior.append([])
    for j in range(4):
        prior[-1].append([])
        for d in list(map(int, input().split())):
            prior[-1][-1].append(d-1)
mv = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def mvs(sharks):
    # sharks move
    tmp_sharks = {}
    for shark, [x, y, d] in sharks.items():
        for cur_d in prior[shark - 1][d]:
            i, j = mv[cur_d]
            nx, ny = x + i, y + j
            if 0 <= nx < N and 0 <= ny < N and not pos[nx][ny][0]:
                tmp_sharks[shark] = [nx, ny, cur_d]
                break
        else:
            for cur_d in prior[shark - 1][d]:
                i, j = mv[cur_d]
                nx, ny = x + i, y + j
                if 0 <= nx < N and 0 <= ny < N and pos[nx][ny][0] == shark:
                    tmp_sharks[shark] = [nx, ny, cur_d]
                    break
    # calculate time
    for i in range(N):
        for j in range(N):
            if pos[i][j][1]:
                pos[i][j][1] -= 1
            if not pos[i][j][1]:
                pos[i][j][0] = 0
    # check sharks pos
    dels = []
    for shark, [x, y, _ ] in tmp_sharks.items():
        if not pos[x][y][0] or pos[x][y][0] == shark:
            pos[x][y] = [shark, K]
        else: # other shark exists
            if pos[x][y][0] < shark:
                dels.append(shark)
            else:
                dels.append(pos[x][y][0])
                pos[x][y][0] = shark
    for shark in dels:
        del tmp_sharks[shark]
    return tmp_sharks


ans = 0
while len(sharks) > 1:
    if ans >= 1000:
        ans = -1
        break
    sharks = mvs(sharks)
    ans += 1
print(ans)