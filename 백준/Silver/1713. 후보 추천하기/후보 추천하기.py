# 후보 추천하기
# reference : https://velog.io/@jajubal/파이썬백준-1713-후보-추천하기
# 복습하거나 나중에 다시 풀어보는 과정이 반드시 필요할 듯하다.
# 혹은 그냥 문제를 푸는 횟수 자체를 늘려야 할 것 같다.

import sys
input = sys.stdin.readline

N = int(input())
total_vote = int(input())
history = list(map(int, input().split()))

frame = []
score = []

for i in range(total_vote):
    # Frame에 있는 경우
    if history[i] in frame:
        for j in range(len(frame)):
            if history[i] == frame[j]:
                score[j] += 1
    # Frame에 없는 경우
    else:
        # Frame 꽉찬 경우
        if len(frame) == N:
            for j in range(len(frame)):
                if score[j] == min(score):
                    del score[j]
                    del frame[j]
                    break
        frame.append(history[i])
        score.append(1)

print(*sorted(frame), sep=' ')
# print(' '.join(map(str, sorted(frame))))