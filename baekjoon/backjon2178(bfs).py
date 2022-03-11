from collections import deque
import sys
read = sys.stdin.readline

def bfs(x, y):
    # 이동할 동,서,남,북 표시
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # deque 생성
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4 가지 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽이므로 진행 불가
            if graph[nx][ny] == 0:
                continue

            # 벽이 아니므로 이동
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 마지막 값에서 카운트 값을 뽑는다.
    return graph[N - 1][M - 1]

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

print(bfs(0, 0))
