## dfs 재귀 함수를 8 곳 check
import sys
read = sys.stdin.readline
## 파이썬 재귀 깊이 1000
sys.setrecursionlimit(1000)
## dfs 재귀를 통해 땅의 위치 확인
def dfs(x, y):
    if 0 <= x < h and 0 <= y < w:
        if graph[x][y] == 1:
            graph[x][y] = 2
            dfs(x - 1, y - 1)
            dfs(x - 1, y)
            dfs(x - 1, y + 1)
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x + 1, y - 1)
            dfs(x + 1, y)
            dfs(x + 1, y + 1)
            return True
        return False


dx = [0,0,0,0,0,0,0,0]
dy = [0,0,0,0,0,0,0,0]

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    ## garph의 땅 표시
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            ## 만약 땅이면 dfs 함수 호출 후 cnt 1 증가
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)




