def solution(n, s):
    r, q = divmod(s, n)
    if r < 1:
        return [-1]
    answer = [r] * n
    for i in range(n-q, n):
        answer[i] += 1
    return answer