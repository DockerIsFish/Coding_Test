from heapq import heappush, heappop


def solution(operations):  # min heap & max heap
    maxh = []
    minh = []
    for ops in operations:
        op, n = ops.split()
        n = int(n)
        if op == "D":
            if n == 1:
                if not maxh:
                    continue
                heappop(maxh)
                if not maxh or -maxh[0] < minh[0]:  ## 동기화
                    minh, maxh = [], []
            else:
                if not minh:
                    continue
                heappop(minh)
                if not minh or minh[0] > -maxh[0]:
                    minh, maxh = [], []
        else:
            heappush(maxh, -n)
            heappush(minh, n)
    if not maxh:
        return [0, 0]
    return [heappop(maxh), heappop(minh)]
