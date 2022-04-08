V, E = map(int, input().split())
cost = 0
parent = [i for i in range(V+1)]
rank = [0 for i in range(V+1)]
edges = []
for e in range(E):
    edges.append(tuple(map(int, input().split())))
edges.sort(key=lambda x: x[2])


def find(u):
    p = parent[u]
    if p == u:
        return u
    return find(p)


def union(u, v):
    p1 = find(u)
    p2 = find(v)
    r1 = rank[p1]
    r2 = rank[p2]
    if r1 > r2:
        parent[p2] = p1
    elif r1 < r2:
        parent[p1] = p2
    else:
        parent[p1] = p2
        rank[p2] += 1
    return


l = 1
for a, b, w in edges:
    if find(a) != find(b):
        union(a, b)
        cost += w
        l += 1
        if l == V:
            break
print(cost)