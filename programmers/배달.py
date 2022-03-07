# https://programmers.co.kr/learn/courses/30/lessons/12978
from heapq import heapify, heappush, heappop


def solution(N, road, K):
    answer = 0
    edge = [[10001] * (N + 1) for _ in range(N + 1)]
    for a, b, c in road:
        edge[a][b] = min(edge[a][b], c)
        edge[b][a] = edge[a][b]
    q = [(0, 1)]
    dist = [float('inf')] * (N + 1)
    while q:
        d, cur = heappop(q)
        if d >= dist[cur]:
            continue
        dist[cur] = d
        for nei in range(1, N + 1):
            if edge[cur][nei] < 10001:
                if edge[cur][nei] + d < dist[nei]:
                    heappush(q, (edge[cur][nei] + d, nei))
    answer = 0
    for d in dist:
        if d <= K:
            answer += 1
    return answer
