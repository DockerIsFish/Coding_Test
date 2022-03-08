from collections import deque
from sys import stdin

mv = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
while True:
    w, h = map(int, stdin.readline().split())
    if (w, h) == (0, 0):
        break
    maps = []
    for i in range(h):
        maps.append(list(map(int, stdin.readline().split())))
    res = 0
    for i in range(w * h):
        x, y = i // w, i % w
        if not maps[x][y]:
            continue
        res += 1
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            if not maps[x][y]:
                continue
            maps[x][y] = 0
            for xx, yy in mv:
                nx = x + xx
                ny = y + yy
                if 0 <= nx < h and 0 <= ny < w and maps[nx][ny]:
                    q.append((nx, ny))
    print(res)
