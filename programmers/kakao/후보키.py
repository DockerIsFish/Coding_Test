def solution(relation):
    answer = 0
    trn = list(zip(*relation))
    candis = []
    for i in range(1, 2 ** len(trn)):
        tmp = set()
        for j in range(len(trn)):
            if i & 1:
                tmp.add(j)
            i >>= 1
        if len(tmp) == 0:
            continue
        for c in candis:
            if c & tmp == c:
                break
        else:
            cols = []
            for col in tmp:
                cols.append(trn[col])
            candi = list(zip(*cols))
            if len(candi) == len(set(candi)):
                answer += 1
                candis.append(tmp)
    return answer
