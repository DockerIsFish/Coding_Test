import sys

def dfs(v):
    visited[v] = True ## 방문 표시
    for i in adj[v]:
        if not visited[i]:
            dfs(v)

N, M = map(int, sys.stdin.readline().split())
##인접 list 생성
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0
for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    ## undirected graph 임으로 서로 연결
    ## dfs 사용해야 하기 때문에 append로 stack 활용
    adj[u].append(v)
    adj[v].append(u)

for j in range(1,N+1):
    if not visited[j]:
        dfs(j)
        cnt += 1
print (cnt)







