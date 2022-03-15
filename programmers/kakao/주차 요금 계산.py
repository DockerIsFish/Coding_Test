from collections import defaultdict
from math import ceil


def solution(fees, records):
    d = defaultdict(list)
    btime, bfee, utime, ufee = fees
    for record in records:
        time, car, inout = record.split()
        hh, mm = time.split(':')
        hh, mm = int(hh) * 60, int(mm)
        d[car].append(hh + mm)
    ans = []
    for car in sorted(d.keys()):
        if len(d[car]) % 2 == 1:
            d[car].append(23 * 60 + 59)
        time = 0
        while d[car]:
            b, a = d[car].pop(), d[car].pop()
            time += b - a
        fee = bfee + ceil(max(0, (time - btime)) / utime) * ufee
        ans.append(fee)
    return ans
