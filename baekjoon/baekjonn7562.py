from collections import deque
import sys
##우선 최소 이동 경우의 수 를 구해야하기 때문에 DFS처럼 전체를 탐색할 필요가 없다
##나이트의 이동 방향을 좌표로 표시하면 8가지 방향이 나온다
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(a, b, c, d):
    queue = deque()
    queue.append((a, b))

    while queue:
        curX, curY = queue.popleft()
        if curX == c and curY == d:
            print(visited[curX][curY] - 1)
            return True

        for i in range(8):
            nx = curX + dx[i]
            ny = curY + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[curX][curY] + 1
                queue.append((nx, ny))

    return False


n = int(sys.stdin.readline())
for i in range(n):
    l = int(sys.stdin.readline())
    visited = [[0] * l for _ in range(l)]
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())
    ## 현재 위치한 곳은 방문 표시
    visited[a][b] = 1
    bfs(a, b, c, d)

