# coding=utf-8
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


def solution(grid):
    answer = []
    # 0, 1, 2, 3 방향은 U, R, D, L
    visited = [[[0] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                res = search([i, j, k], [i, j, k], visited, 0, grid)
                if res:
                    answer.append(res)
    answer.sort()
    return answer


def search(start, cur, visited, cycle, grid):
    if visited[cur[0]][cur[1]][cur[2]]:
        if cur == start:
            return cycle
        else:
            return False
    mv = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    visited[cur[0]][cur[1]][cur[2]] = True

    if grid[cur[0]][cur[1]] == "R":
        cur[2] = (cur[2] + 1) % 4
    elif grid[cur[0]][cur[1]] == "L":
        cur[2] = (cur[2] - 1) % 4
    x, y = mv[cur[2]]
    cur[0] = (cur[0] + x) % len(grid)
    cur[1] = (cur[1] + y) % len(grid[0])
    return search(start, cur, visited, cycle + 1, grid)