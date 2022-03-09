from collections import deque


def solution(s):
    par = {j: i for i, j in enumerate("[({})]")}
    for i in range(len(s)):
        q = deque([])
        sub = 0
        for c in s[i:] + s[:i]:
            q.append(c)
            while len(q) > 1:
                b, a = q.pop(), q.pop()
                if par[a] >= par[b] or par[a] + par[b] != 5:
                    q.append(a), q.append(b)
                    break
            if not q:
                sub += 1
        if not q:
            return sub
    return 0
