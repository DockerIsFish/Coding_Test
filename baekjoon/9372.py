def union(parent, u, v):
    p1 = find(parent, u)
    p2 = find(parent, v)
    r1, r2 = rank[u], rank[v]
    if r1 > r2:
        parent[p2] = p1
    else:
        parent[p1] = p2
        if r1 == r2:
            rank[p2] += 1
    return


def find(parent, v):
    p = parent[v]
    if p == v:
        return p
    return find(parent, p)


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]
    rank = [0 for i in range(N+1)]
    cost = 0
    for i in range(M):
        a, b = map(int, input().split())
        p1, p2 = find(parent, a), find(parent, b)
        if p1 != p2:
            union(parent, p1, p2)
            cost += 1
    print(cost)