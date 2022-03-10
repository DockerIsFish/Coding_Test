from collections import deque


def solution(p):
    if p == '':
        return p
    u, v = '', ''
    l, r = 0, 0
    for i, c in enumerate(p):
        if c == '(':
            l += 1
        else:
            r += 1
        if l == r:
            u = p[:i + 1]
            v = p[i + 1:]
            break
    q = deque([])
    for c in u:
        q.append(c)
        while len(q) > 1:
            b, a = q.pop(), q.pop()
            if a != '(' or b != ')':
                q.append(a), q.append(b)
                break
    if not q:
        return u + solution(v)
    x = '(' + solution(v) + ')'
    for c in u[1:len(u) - 1]:
        if c == '(':
            x += ')'
        else:
            x += '('
    return x
