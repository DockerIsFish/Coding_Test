def solution(arr):
    narr = dfs(len(arr), arr, 0, 0)
    return [narr.count(0), narr.count(1)]


def dfs(l, arr, x, y):
    if l == 0:
        return [arr[x][y]]
    ll = l // 2
    nran = [(x, y), (x + ll, y), (x, y + ll), (x + ll, y + ll)]
    ret = []
    for xx, yy in nran:
        ret += dfs(ll, arr, xx, yy)
    if ret == [1, 1, 1, 1]:
        return [1]
    elif ret == [0, 0, 0, 0]:
        return [0]
    return ret
