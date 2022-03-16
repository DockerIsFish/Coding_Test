def solution(n, info):
    apeach = sum([10 - i for i in range(11) if info[i]])
    score = [(10 - i) * 2 if info[i] else 10 - i for i in range(11)]
    req = [i + 1 for i in info]

    def dfs(n, depth, arr):
        if depth == 10:
            ret = arr[:]
            ret[10] += n
            return ret, sum([score[i] for i in range(11) if ret[i]])
        s1 = 0
        if n >= req[depth]:
            tmp_arr = arr[:]
            tmp_arr[depth] = req[depth]
            arr1, s1 = dfs(n - req[depth], depth + 1, tmp_arr)
        arr2, s2 = dfs(n, depth + 1, arr[:])
        if s1 > s2:
            return arr1, s1
        elif s1 == s2:
            for j in range(10, -1, -1):
                if arr1[j] > arr2[j]:
                    return arr1, s1
                elif arr1[j] < arr2[j]:
                    return arr2, s2
        return arr2, s2

    answer, ryan = dfs(n, 0, [0] * 11)
    if apeach >= ryan:
        return [-1]
    return answer
