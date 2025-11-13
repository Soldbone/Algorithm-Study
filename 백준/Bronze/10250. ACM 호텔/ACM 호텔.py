# ACM 호텔
import sys
from math import ceil

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    room_number = ceil(N/H)

    if (floor) == 0: floor = H
    print(f"{floor}{room_number:02}")
