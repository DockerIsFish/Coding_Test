N, K = map(int, input().split())
A = list(map(int, input().split()))
robots = []
stage = 1
while stage:
    A = A[-1:] + A[:-1]
    for i in range(len(robots)):
        robots[i] += 1
    if robots and robots[0] == N - 1:
        robots.pop(0)
    for i, robot in enumerate(robots):
        if A[robot + 1]:
            if not i or (i and robots[i-1] != robot+1):
                A[robot+1] -= 1
                robots[i] += 1
    if robots and robots[0] == N - 1:
        robots.pop(0)
    if A[0]:
        A[0] -= 1
        robots.append(0)
    if A.count(0) >= K:
        print(stage)
        break
    stage += 1