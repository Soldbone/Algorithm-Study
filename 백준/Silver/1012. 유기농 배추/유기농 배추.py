# 유기농 배추
# 이번에도 풀이를 보긴 했지만 내 아이디어로 구현했다.

import sys
from collections import deque
input = sys.stdin.readline

# 1697(숨바꼭질)에서 사용했던 bfs 코드 참고함
def bfs(napa_cabbage_coord: list):
    # Respectively, up/right/down/left
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque([napa_cabbage_coord[0]])
    del napa_cabbage_coord[0]
    while q:
        v = q.popleft()
    
        for i in range(4):
            if (v[0] + dx[i], v[1] + dy[i]) in napa_cabbage_coord:
                q.append((v[0] + dx[i], v[1] + dy[i]))
                napa_cabbage_coord.remove((v[0] + dx[i], v[1] + dy[i]))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    napa_cabbage_coord = [ tuple(map(int, input().split())) for _ in range(K) ]

    count = 0
    for i in range(K):
        if len(napa_cabbage_coord):
            bfs(napa_cabbage_coord)
            count += 1
        else:
            break

    print(count)
