n = int(input())
m = list(map(int, input().split()))
cnts = [0]*20
for num in m:
    d = 1
    for i in range(20):
        if num & d:
            cnts[i] += 1
        d <<= 1
max(cnts)
