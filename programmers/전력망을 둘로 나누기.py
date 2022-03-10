from collections import deque


def solution(n, wires):
    answer = 10 ** 10
    edges = [[False] * (n + 1) for _ in range(n + 1)]
    for i, j in wires:
        edges[i][j] = True
        edges[j][i] = True
    for i, j in wires:
        edges[i][j] = False
        edges[j][i] = False
        visited = [False] * (n + 1)
        q = deque([i])
        while q:
            cur = q.popleft()
            if visited[cur]:
                continue
            visited[cur] = True
            for nei in range(1, n + 1):
                if edges[cur][nei]:
                    q.append(nei)
        N = visited.count(True)
        answer = min(answer, abs(N - (n - N)))
        edges[i][j] = True
        edges[j][i] = True
    return answer