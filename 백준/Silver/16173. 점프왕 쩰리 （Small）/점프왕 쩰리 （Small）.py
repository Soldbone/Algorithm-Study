### BFS - 벡터 개념 사용해보기
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
queue = deque([(0, 0)])
visited[0][0] = True

# r(ow), c(olumn)
while queue:
    r, c = queue.popleft()

    if board[r][c] == -1:
        print("HaruHaru")
        break

    jump = board[r][c]

    # 오른쪽, 아래
    moves = [(0, jump), (jump, 0)]

    for move in moves:
        dr, dc = move
        nr, nc = r + dr, c + dc
        if nr < n and nc < n and not visited[nr][nc]:
            visited[nr][nc] = True
            queue.append((nr, nc))
else:
    print("Hing")