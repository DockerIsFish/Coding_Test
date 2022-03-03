n = 3
input = '26 40 83 49 60 57 13 89 99'.split()

arr = []
for i in range(n):
    arr.append(input[i*3 : (i+1)*3])

for i in range(1,n):
	arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0] # 첫 줄이 빨강일때
	arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1] # 첫 줄이 초록일때
	arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2] # 첫 줄이 파랑일때

answer = min(arr[n-1])