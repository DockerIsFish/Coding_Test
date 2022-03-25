from collections import defaultdict
R, C, K = map(int, input().split())
R, C = R - 1, C - 1
A = [list(map(int, input().split())) for _ in range(3)]

def oper(A):
    l = 0
    for i in range(len(A)):
        cnt_dict = defaultdict(int)
        for a in A[i]:
            if a != 0:
                cnt_dict[a] += 1
        cnt_pairs = [(c, n) for n, c in cnt_dict.items()]
        cnt_pairs.sort()
        A[i] = []
        for c, n in cnt_pairs:
            A[i].append(n)
            A[i].append(c)
            if len(A[i]) > 100:
                break
        l = max(l, len(A[i]))
    for row in A:
        for j in range(max(0, l-len(row))):
            row.append(0)
    return


for i in range(100):
    if 0 <= R < len(A) and 0 <= C < len(A[0]) and A[R][C] == K:
        print(i)
        break
    if len(A) >= len(A[0]):
        oper(A)
    else:
        A = list(map(list, zip(*A)))
        oper(A)
        A = list(map(list, zip(*A)))
else:
    if 0 <= R < len(A) and 0 <= C < len(A[0]) and A[R][C] == K:
        print(100)
    else:
        print(-1)