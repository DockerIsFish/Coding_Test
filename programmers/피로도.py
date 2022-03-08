from itertools import permutations


def solution(k, dungeons):
    orders = list(permutations(list(range(len(dungeons))), len(dungeons)))
    ans = 0
    for order in orders:
        remain = k
        cnt = 0
        for i in order:
            minp, req = dungeons[i]
            if remain >= minp:
                remain -= req
                cnt += 1
        ans = max(ans, cnt)
    return ans


'''
def solution(k, dungeons):
    global ans
    ans = 0
    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, 0, 0, -1)
    return ans

def dfs(remain, dungeons, visited, depth, cnt, cur):
    global ans
    if depth == len(dungeons):
        ans = max(ans, cnt)
        return
    for i in range(len(dungeons)):
        if visited[i]:
            continue
        visited[i] = True
        if remain >= dungeons[i][0]:   
            dfs(remain-dungeons[i][1], dungeons, visited, depth+1, cnt+1, i)
        else:
            dfs(remain, dungeons, visited, depth+1, cnt, i)
        visited[i] = False
    return
'''
