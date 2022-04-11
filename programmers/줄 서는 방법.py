def solution(n, k):
    answer = []
    numbers = [i + 1 for i in range(n)]
    d = 1
    k -= 1
    for i in range(1, n+1):
        d *= i
    for i in range(n, 0, -1):
        d //= i
        r = int(k // d)
        k = k % d
        num = numbers.pop(r)
        answer.append(num)
        #numbers = numbers[:r] + numbers[r + 1:]
    return answer