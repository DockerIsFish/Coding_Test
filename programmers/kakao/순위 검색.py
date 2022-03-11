from collections import defaultdict


def solution(info, query):
    answer = []
    d = defaultdict(list)
    for i in range(len(info)):
        info[i] = info[i].split()
        info[i][4] = int(info[i][4])
    info.sort(key = lambda x: (-x[4]))
    for i in info:
        for l in [i[0], '-']:
            for j in [i[1], '-']:
                for e in [i[2], '-']:
                    for f in [i[3], '-']:
                        d[l, j, e, f].append(i[4])
    for i in range(len(query)):
        query[i] = query[i].replace('and ', '').split()
        query[i][4] = int(query[i][4])
    for la, j, e, f, s in query:
        l, r = 0, len(d[la, j, e, f])-1
        while l <= r:
            mid = (l+r)//2
            if d[la, j, e, f][mid] >= s:
                l = mid+1
            else:
                r = mid-1
        if l >= len(d[la, j, e, f]) or d[la, j, e, f][l] < s:
            answer.append(l)
        else:
            answer.append(r)
    return answer