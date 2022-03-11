def solution(s):
    answer = []
    e = eval('[' + s[1:len(s) - 1] + ']')
    e.sort(key=len)
    cmp = set()
    for i in e:
        answer.append((i - cmp).pop())
        cmp = i
    return answer
