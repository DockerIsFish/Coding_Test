import re


def solution(n, k):
    knum = (re.sub(r'0+', r'0', convert(n, k).strip('0'))).split('0')
    nums = list(map(int, knum))
    visited = [False] * (int(max(nums)**(1/2))+1)
    for i in range(2, len(visited)):
        if visited[i]:
            continue
        for j in range(i*2, len(visited), i):
            visited[j] = True
        rm = []
        for num in nums:
            if num == 1 or (num % i == 0 and num > i):
                rm.append(num)
        for num in rm:
            nums.remove(num)
    return len(nums)


def convert(n, k):
    ans = ''
    while n:
        ans = str(n%k) + ans
        n //= k
    return ans