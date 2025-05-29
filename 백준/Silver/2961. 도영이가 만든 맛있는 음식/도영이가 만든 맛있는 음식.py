# 도영이가 만든 맛있는 음식
# refer to : https://velog.io/@hygge/Python-백준-2961-도영이가-만든-맛있는-음식-Brute-Force

import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())

sours = []
bitters = []
for _ in range(N):
    sour, bitter = map(int, input().split())
    sours.append(sour)
    bitters.append(bitter)

diff = abs(sours[0] - bitters[0])

for i in range(1, N+1):
    cases = list(combinations(list(range(N)), i))

    for select in cases:
        sour = 1
        bitter = 0

        for j in range(i):
            sour *= sours[select[j]]
            bitter += bitters[select[j]]

        diff = min(diff, abs(sour - bitter))

print(diff)
