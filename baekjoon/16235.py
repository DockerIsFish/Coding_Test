N, M, K = map(int, input().split())
A = []
namu = [[{} for _ in range(N)] for i in range(N)]
land = [[5] * N for _ in range(N)]
for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(M):
    x, y, z = map(int, input().split())
    if z in namu[x - 1][y - 1]:
        namu[x - 1][y - 1][z] += 1
    else:
        namu[x - 1][y - 1][z] = 1
mv = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

for _ in range(K):
    # spring
    for i in range(N):
        for j in range(N):
            tmp = {}
            die = 0
            for age, cnt in sorted(namu[i][j].items()):
                l = (land[i][j] // age)
                if cnt <= l:
                    land[i][j] -= age * cnt
                    tmp[age + 1] = cnt
                elif 1 <= l:
                    land[i][j] -= l * age
                    tmp[age + 1] = l
                    die += (age // 2) * (cnt - l)
                else:
                    die += (age // 2) * cnt
            namu[i][j] = tmp
            land[i][j] += die
    for i in range(N):  # fall
        for j in range(N):
            for age, cnt in namu[i][j].items():
                if age % 5 == 0:
                    for x, y in mv:
                        ii = i + x
                        jj = j + y
                        if 0 <= ii < N and 0 <= jj < N:
                            if namu[ii][jj].get(1):
                                namu[ii][jj][1] += cnt
                            else:
                                namu[ii][jj][1] = cnt
            land[i][j] += A[i][j]  # winter
answer = 0
for i in range(N):
    for j in range(N):
        for k in namu[i][j].values():
            answer += k
print(answer)