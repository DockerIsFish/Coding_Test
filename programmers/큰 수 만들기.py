def solution(number, k):
    answer = []
    num = list(map(int, number))
    for idx, n in enumerate(num):
        while answer:
            if answer[-1] < n and len(answer) + (len(num)-idx) > (len(num) - k):
                answer.pop()
            else:
                break
        if len(answer) + k < len(num):
            answer.append(n)
    return "".join(list(map(str, answer)))