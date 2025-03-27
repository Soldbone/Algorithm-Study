# 최소 힙
import heapq
import sys

n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    cmd_input = int(sys.stdin.readline().rstrip())
    if cmd_input != 0:
        heapq.heappush(heap, cmd_input)
    elif len(heap) > 0:
        print(heapq.heappop(heap))
    else:
        print(0)