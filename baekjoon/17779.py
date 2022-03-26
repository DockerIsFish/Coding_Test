N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
total = 0
for i in range(N):
    total += sum(A[i])

def divide(x, y, d1, d2):
    popul = [0, 0, 0, 0]
    lx, ly = x+d1, y-d1
    rx, ry = x+d2, y+d2
    bx, by = x+d1+d2, y-d1+d2
    for i in range(x):
        popul[0] += sum(A[i][:y+1])
        popul[1] += sum(A[i][y+1:])
    for i in range(x, lx):
        popul[0] += sum(A[i][:y-i+x])
    for i in range(x, rx+1):
        popul[1] += sum(A[i][y+1+i-x:])
    for i in range(lx, bx+1):
        popul[2] += sum(A[i][:ly-lx+i])
    for i in range(rx+1, bx+1):
        popul[3] += sum(A[i][ry+rx+1-i:])
    for i in range(bx+1, N):
        popul[2] += sum(A[i][:by])
        popul[3] += sum(A[i][by:])
    popul.append(total-sum(popul))
    return max(popul) - min(popul)


ret = float('inf')
for x in range(N - 2):
    for y in range(1, N - 1):
        for d1 in range(1, y):
            for d2 in range(1, min(N - y, N-(x+d1))):
                ret = min(ret, divide(x, y, d1, d2))

print(ret)
