from heapq import heappush, heappop
from collections import defaultdict


def solution(n, edge):
    answer = 0
    q = [(0, 1)]
    neis = defaultdict(list)
    for a, b in edge:
        neis[a].append(b)
        neis[b].append(a)
    dist = [float('inf') for _ in range(n + 1)]
    while q:
        d, cur = heappop(q)
        if d >= dist[cur]:
            continue
        dist[cur] = d
        for nei in neis[cur]:
            heappush(q, (d + 1, nei))
    dist[0] = 0
    m = max(dist)
    for i in range(1, n + 1):
        if dist[i] == m:
            answer += 1
    return answer
