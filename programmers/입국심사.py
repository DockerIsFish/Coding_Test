def solution(n, times):
    l, r = 0, 10 ** 14
    while l <= r:
        mid = (l + r) // 2
        if check(n, mid, times):
            r = mid - 1
        else:
            l = mid + 1
    return l


def check(n, t, times):
    p = 0
    for time in times:
        p += t // time
        if p >= n:
            return True
    return False
