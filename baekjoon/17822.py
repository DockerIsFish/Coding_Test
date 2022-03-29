from collections import deque


N, M, T = map(int, input().split())
circle = [list(map(int, input().split())) for _ in range(N)]
multiple = {i+1: [] for i in range(N)}
mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(1, N+1):
    for j in range(1, N//i + 1):
        multiple[i].append(i*j-1)


def swap(n, d, k):
    res = 0
    if d == 0:  # 0 clockwise
        k = M - k
    for i in multiple[n]:  # 숫자를 swap
        circle[i] = circle[i][k:] + circle[i][:k]
    candi = set()
    for i in range(N):
        for j in range(M):
            if circle[i][j] > 0 and circle[i][j] == circle[i][j-1]:
                candi.add((i, j))
                candi.add((i, j-1))
    for i in range(N-1):
        for j in range(M):
            if circle[i][j] > 0 and circle[i][j] == circle[i+1][j]:
                candi.add((i, j))
                candi.add((i+1, j))
    for i, j in candi:
        circle[i][j] = 0
    if not candi:
        nums = []
        for i in range(N):
            for j in range(M):
                if circle[i][j] > 0:
                    nums.append(circle[i][j])
        mean = sum(nums) / len(nums)
        for i in range(N):
            for j in range(M):
                if circle[i][j] > mean:
                    circle[i][j] -= 1
                elif 0 < circle[i][j] < mean:
                    circle[i][j] += 1
    for i in range(N):  # 원판의 숫자를 sum
        res += sum(circle[i])
    return res


for i in range(T):
    n, d, k = map(int, input().split())
    res = swap(n, d, k)
    if not res:
        print(res)
        break
else:
    print(res)