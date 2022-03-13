import re


def solution(m, musicinfos):
    answer = ''
    ans_time = 0
    m = re.findall(r'[A-Z]#*', m)
    for music in musicinfos:
        music = music.split(',')
        music[0] = music[0].split(':')
        music[1] = music[1].split(':')
        start = int(music[0][0]) * 60 + int(music[0][1])
        end = int(music[1][0]) * 60 + int(music[1][1])
        time = end - start
        title = music[2]
        mel = re.findall(r'[A-Z]#*', music[3])
        total_mel = mel * (time // len(mel)) + mel[:(time % len(mel))]
        for i in range(time - len(m) + 1):
            if total_mel[i:i + len(m)] == m:
                if time > ans_time:
                    answer = music[2]
                    ans_time = time
                    break
    if answer == '':
        return "(None)"
    return answer
