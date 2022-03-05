# coding=utf-8
# https://programmers.co.kr/learn/courses/30/lessons/87377
# 직선들 사이의 교점 찾기
def solution(line):
    answer = []
    max_x, min_x = -float('inf'), float('inf')
    max_y, min_y = -float('inf'), float('inf')
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a*d - b*c == 0:
                continue
            A = (b*f-e*d)%(a*d-b*c)
            B = (e*c-a*f)%(a*d-b*c)
            X = (b*f-e*d)//(a*d-b*c)
            Y = (e*c-a*f)//(a*d-b*c)
            if  A == 0 and B == 0:
                if not [X,Y] in answer:
                    answer.append([X, Y])
                    max_x = max(max_x, X)
                    min_x = min(min_x, X)
                    max_y = max(max_y, Y)
                    min_y = min(min_y, Y)
    p = [["."] * ((max_x-min_x+1)) for _ in range(max_y-min_y+1)]
    for x, y in answer:
        p[max_y-y][x-min_x] = "*"
    for i in range(len(p)):
        p[i] = "".join(p[i])
    return p