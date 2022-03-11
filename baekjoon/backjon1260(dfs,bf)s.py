from collections import deque
import sys
read = sys.stdin.readline

## bfs는 너비 우선 탐색으로 queue를 사용
def bfs(v):
 ## list를 사용하면 O(n)이 걸리지만 deque인 경우 O(1)이 걸린다.
  q = deque()
  q.append(v)
  visit_list[v] = 1
  while q:
    v = q.popleft()
    print(v, end = " ")
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visit_list[i] = 1
## dfs는 깊이 우선 탐색으로 stack를 사용
def dfs(v):
  visit_list2[v] = 1
  print(v, end = " ")
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1:
      dfs(i)

n, m = map(int, read().split())
## 인접 행렬 생성
graph = [[0] * (n + 1) for _ in range(n + 1)]
## bfs 방문 array 생성
visit_list = [0] * (n + 1)

## dfs 방문 array 생성
visit_list2 = [0] * (n + 1)

## 간선의 개수만큼 반복
for _ in range(m):
  a, b = map(int, read().split())
  ## 입력된 두 vertex를 서로 연결
  graph[a][b] = graph[b][a] = 1

