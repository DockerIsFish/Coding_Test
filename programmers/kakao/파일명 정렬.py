import re


def solution(files):
    answer = []
    t = []
    for f in files:
        a = re.match(r'([^0-9]+)([0-9]{1,5})([0-9a-zA-Z .-]*)', f)
        t.append(a.groups())
    t.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for s in t:
        answer.append(s[0] + s[1] + s[2])
    return answer
