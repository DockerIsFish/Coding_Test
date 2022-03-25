
##background
## 지수법칙:A^m+n = A^m x A^n
## 나머지 분배 법칙: (AxB)%C = (A%C) *(B%C) % C
import sys
def multi(A,N):
    if N == 1:
        return A%C
    else:
        tmp = multi(A,N//2)
        if N %2 == 0:
            return (tmp*tmp)%C
        else:
            return (tmp*tmp*A)%C

A,B,C = map(int,sys.stdin.readline().split())
print(multi(A,B))