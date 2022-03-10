from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    combi = defaultdict(int)
    sorted_orders = [sorted(" ".join(order).split()) for order in orders]
    for order in sorted_orders:
        for n in course:
            tmp = map(tuple, combinations(order, n))
            for s in tmp:
                combi[s] += 1
    for n in course:
        m = 0
        for k, v in combi.items():
            if len(k) == n:
                m = max(m, v)
        if m < 2:
            continue
        for k, v in combi.items():
            if len(k) == n and v == m:
                answer.append("".join(k))
    answer.sort()
    return answer
