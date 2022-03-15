def solution(n, t, m, p):
    answer = ''
    chrs = '0123456789ABCDEF'
    num = 0
    cur = 0
    while len(answer) < t:
        ret = convert_num(num, n, chrs)
        num += 1
        for i in range(p, cur+len(ret)+1, m):
            if i-cur-1 < 0:
                continue
            answer += ret[i-cur-1]
        cur = (cur+len(ret)) % m
    return answer[:t]


def convert_num(num, n, chrs):
    ret = ''
    while True:
        ret = chrs[num % n] + ret
        num //= n
        if num == 0:
            break
    return ret