def solution(N, number):
    answer = 0
    dp = []
    for i in range(8):
        tmp = [int(str(N)*(i+1))]
        if dp:
            for j in range(i):
                for k in dp[j]:
                    for l in dp[i-j-1]:
                        if l != 0:
                            tmp.append(k//l)
                        if k != 0:
                            tmp.append(l//k)
                        tmp.append(k*l)
                        tmp.append(k+l)
                        tmp.append(l-k)
                        tmp.append(k-l)
        dp.append(list(set(tmp)))
        if number in dp[-1]:
            return i+1
    return -1