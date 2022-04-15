def solution(n, works):
    answer = 0
    works.sort(reverse=True)
    l, r = 0, works[0]
    while l <= r:
        mid = (l + r) // 2
        if check(mid, n, works):
            r = mid - 1
        else:
            l = mid + 1
    for i in range(len(works)):
        diff = works[i] - l
        if diff <= 0:
            continue
        works[i] = l
        n -= diff
    for i in range(min(n, len(works))):
        if works[i] == 0:
            break
        works[i] -= 1
    for work in works:
        answer += work ** 2
    return answer
def check(d, n, works):
    total = 0
    for work in works:
        diff = work - d
        if diff <= 0:
            continue
        total += diff
        if total > n:
            return False
    return True