# coding=utf-8
# https://programmers.co.kr/learn/courses/30/lessons/1844#
from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 움직일 수 있는 경우의 수
    q = deque([(0, 0, 1)])  # 시작점과 이동거리을 큐에 넣기
    answer = -1  # 도착못하는 경우
    while q:  # bfs로 탐색
        cur = q.popleft()
        x, y, dist = cur
        if not maps[x][y]:
            continue
        if x == n - 1 and y == m - 1:
            answer = dist
            break
        maps[x][y] = 0
        for i, j in mv:
            xx, yy = x + i, y + j
            if 0 <= xx < n and 0 <= yy < m and maps[xx][yy]:
                q.append((xx, yy, dist + 1))
    return answer
