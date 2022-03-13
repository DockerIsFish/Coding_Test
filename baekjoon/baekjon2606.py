import sys
from collections import deque
def bfs(v):
    cnt = 0
    q = deque()
    q.append(v)
    virus[v] = 1
    while q:
        v = q.popleft()
        for i in range(1, N + 1):
            if virus[i] == 0 and graph[v][i] == 1:
                q.append(i)
                virus[i] = 1
                cnt+=1
    print(cnt)
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[0] * (N+1) for _ in range(N+1)]
virus = [0] * (N+1)
result = []
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

bfs(1)