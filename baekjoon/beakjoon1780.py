import sys

result = []

def solution(x,y,N):
    number = paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if number != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        solution(x+k*N//3, y+l*N//3, N//3)
                return

    if number == 1:
        result.append(1)
    elif number == 0:
        result.append(0)
    elif number == -1:
        result.append(-1)


N = int(sys.stdin.readline())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
solution(0,0,N)
print(result.count(-1))
print(result.count(0))
print(result.count(1))
