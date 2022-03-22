N, M, K = map(int, input().split())
A = []
namu = [[[] for _ in range(N)] for i in range(N)]
land = [[5] * N for _ in range(N)]
for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(M):
    x, y, z = map(int, input().split())
    namu[x - 1][y - 1].append(z)
mv = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
for _ in range(K):
    # spring
    for i in range(N):
        for j in range(N):
            namu[i][j].sort()  # 어린 순
            for k in range(len(namu[i][j])):
                if namu[i][j][k] <= land[i][j]:
                    land[i][j] -= namu[i][j][k]
                    namu[i][j][k] += 1
                else:
                    for l in range(k, len(namu[i][j])):  # summer
                        land[i][j] += namu[i][j].pop() // 2
                    break
    for i in range(N):  # fall
        for j in range(N):
            for k in range(len(namu[i][j])):
                if namu[i][j][k] % 5 == 0:
                    for x, y in mv:
                        if 0 <= i + x < N and 0 <= j + y < N:
                            namu[i + x][j + y].append(1)
    for i in range(N):  # winter
        for j in range(N):
            land[i][j] += A[i][j]
answer = 0
for i in range(N):
    for j in range(N):
        answer += len(namu[i][j])
print(answer)