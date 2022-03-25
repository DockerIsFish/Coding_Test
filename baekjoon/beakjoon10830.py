## divide 부분 독립적으로 수행 가능한 부분을 찾는다.
## A^2 = A*A
import sys
def mul(n,matrix1,matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j]%= 1000
    return result

def divide(n,b,matrix):
    if b == 1:
        return matrix
    elif b== 2:
        return mul(n,matrix,matrix)
    else:
        tmp = divide(n,b//2,matrix)
        if b%2 == 0: ##expotential이 짝수인 경우
            return mul(n,tmp,tmp)
        else: ## expotential이 홀수인 경우
            return mul(n,mul(n,tmp,tmp),matrix)

N,B = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

result = divide(N,B,arr)

for row in result:
    for num in row:
        print(num%1000, end=' ')
    print()