n = int(input())
m = [0] + list(map(int, input().split()))
dp = [0]
s = [0]
for i in range(1, n+1):
    if m[i] > s[-1]:
        dp.append(len(s))
        s.append(m[i])
    else:
        for j in range(i):
            if s[j] >= m[i]:
                s[j] = m[i]
                dp.append(j)
                break
print(len(s)-1)