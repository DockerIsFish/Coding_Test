# N개 자연수 입력
N = int(input())
N_list = list(map(int,input().split()))
tmp = 0 

# 자릿수의 합
for i in range(N):
    sum_ = sum([int(j) for j in str(N_list[i])])
    if sum_ > tmp:
        tmp = sum_
        ans = N_list[i]

print(ans)