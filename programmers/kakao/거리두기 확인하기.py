def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer


def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] != 'P':
                continue
            if 0<=j+1<5 and place[i][j+1] == 'P': # 바로 오른쪽이 사람일 때
                return 0
            if 0<=i+1<5 and place[i+1][j] == 'P': # 바로 아래가 사람일 때
                return 0
            if 0<=i+1<5 and 0<=j+1<5 and place[i+1][j+1] == 'P': # 오른쪽 아래 대각선이 사람일 때
                if place[i+1][j] == 'O' or place[i][j+1] == 'O':
                    return 0
            if 0<=i+1<5 and 0<=j-1<5 and place[i+1][j-1] == 'P': # 왼쪽 아래 대각선이 사람일 때
                if place[i+1][j] == 'O' or place[i][j-1] == 'O':
                    return 0
            if 0<=i+2<5 and place[i+2][j] == 'P' and place[i+1][j] == 'O':# 두칸 밑이 사람일 때
                return 0
            if 0<=j+2<5 and place[i][j+2] == 'P' and place[i][j+1] == 'O':# 두칸 오른쪽이 사람일 때
                return 0
    return 1