global answer
def solution(n):
    global answer
    answer = []
    hanoi(n, 1, 2, 3)
    return answer
def hanoi(n, src, mid, des):
    if n == 1:
        global answer
        answer.append([src, des])
        return
    hanoi(n-1, src, des, mid)
    hanoi(1, src, mid, des)
    hanoi(n-1, mid, src, des)
    return