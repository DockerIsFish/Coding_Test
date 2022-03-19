def solution(n):
    answer = 0
    chess = [[0] * n for _ in range(n)]
    return dfs(0, n, chess)


def dfs(row, n, chess):
    if row == n:
        return 1
    ret = 0
    for i in range(n):
        if chess[row][i]:
            continue
        chesstmp = [chess[j][:] for j in range(n)]
        for j in range(row + 1, n):
            chesstmp[j][i] = 1
            if 0 <= i + j - row < n:
                chesstmp[j][i + j - row] = 1
            if 0 <= i - j + row < n:
                chesstmp[j][i - j + row] = 1
        ret += dfs(row + 1, n, chesstmp)
    return ret
