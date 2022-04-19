def solution(n, costs):
    parent = [i for i in range(n)]
    rank = [0] * n

    def find(u):
        p = parent[u]
        if p == u:
            return u
        return find(p)

    def union(u, v, root1, root2):
        rank1, rank2 = rank[root1], rank[root2]
        if rank1 > rank2:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank1 == rank2:
                rank[root2] += 1
        return

    answer = 0
    costs.sort(key=lambda x: x[2])
    for a, b, c in costs:
        p1, p2 = find(a), find(b)
        if p1 != p2:
            union(a, b, p1, p2)
            answer += c
    return answer