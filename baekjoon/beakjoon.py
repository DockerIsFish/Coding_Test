import sys

def pow(A,B):
    if B == 1:
        return A%C
    else:
        temp = pow(A,B//2)
        if B%2 == 0:
            return temp * temp %C ## B가 짝수인 경우
        else:
            return temp*temp*A%C ## B가 홀수 인 경우



A,B,C = map(int,sys.stdin.readline().split())

result = pow(A,B)
print(result)