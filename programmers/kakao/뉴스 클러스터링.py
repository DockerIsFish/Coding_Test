import re
from collections import defaultdict


def solution(str1, str2):
    answer = 0
    str1 = re.sub('[^a-z]', ' ', str1.lower())
    str2 = re.sub('[^a-z]', ' ', str2.lower())
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    elements = set()
    for i in range(len(str1) - 1):
        tmp = str1[i:i + 2]
        if not ' ' in tmp:
            d1[tmp] += 1
            elements.add(tmp)
    for i in range(len(str2) - 1):
        tmp = str2[i:i + 2]
        if not ' ' in tmp:
            d2[tmp] += 1
            elements.add(tmp)
    inter = 0
    union = 0
    for e in elements:
        inter += min(d1[e], d2[e])
        union += max(d1[e], d2[e])
    if not inter and not union:
        return 65536
    return int(inter / union * 65536)
