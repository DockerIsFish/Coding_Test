from collections import deque


def solution(msg):
    answer = []
    d = {chr(ord('A') + i): i + 1 for i in range(26)}
    msg = deque(" ".join(msg).split())
    s = ''
    while msg:
        s += msg.popleft()
        if not s in d:
            d[s] = len(d) + 1
            answer.append(d[s[:-1]])
            s = s[-1]
    answer.append(d[s])
    return answer
