def solution(n):
    dp = [1, 1]
    for i in range(2, n+1):
        dp.append((dp[-1] + dp[-2]) % 1000000007)
    return dp[n]