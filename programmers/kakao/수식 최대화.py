import re


def solution(expression):
    ex = re.sub(r"([^0-9])", r" \1 ", expression).split()
    return dfs(ex, ['*','+','-'])


def dfs(ex, oper):
    if len(ex) == 1:
        return abs(int(ex[0]))
    ret = 0
    for i in range(len(oper)):
        tmp = ex[:]
        k = 1
        while k < len(tmp):
            if tmp[k] == oper[i]:
                tmp = tmp[:k-1]+[str(eval(tmp[k-1]+tmp[k]+tmp[k+1]))]+tmp[k+2:]
                continue
            k += 2
        ret = max(ret, dfs(tmp, oper[:i]+oper[i+1:]))
    return ret