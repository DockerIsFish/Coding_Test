from collections import defaultdict


N, M, K = map(int, input().split())
fballs = defaultdict(list)
maps = [[0] * N for j in range(N)]
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fballs[(r-1, c - 1)].append([m, s, d])
    maps[r-1][c-1] += 1
mv = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def cal_mv(fballs):
    ret_fballs = defaultdict(list)
    for (r, c), infos in fballs.items():
        maps[r][c] -= len(infos)
        for m, s, d in infos:
            i, j = mv[d]
            rr, cc = (s*i + r)%N, (s*j + c)%N
            ret_fballs[(rr, cc)].append([m, s, d])
            maps[rr][cc] += 1
    dels = []
    for (r, c), infos in ret_fballs.items():
        l = len(infos)
        if l < 2:
            continue
        newm, news, newd = 0, 0, []
        for m, s, d in infos:
            newm += m
            news += s
            newd.append(d % 2)
        newm //= 5
        if not newm:
            dels.append((r, c))
            continue
        news //= l
        if newd == [0] * l or newd == [1] * l:
            newd = [0, 2, 4, 6]
        else:
            newd = [1, 3, 5, 7]
        tmp = []
        if newm:
            for d in newd:
                tmp.append([newm, news, d])
        ret_fballs[(r, c)] = tmp
    for i in dels:
        del ret_fballs[i]
    return ret_fballs


for i in range(K):
    fballs = cal_mv(fballs)
ans = 0
for infos in fballs.values():
    for m, d, s in infos:
        ans += m
print(ans)