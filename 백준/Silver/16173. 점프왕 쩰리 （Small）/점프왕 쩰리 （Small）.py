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

    nr, nc = r + jump, c
    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
        visited[nr][nc] = True
        queue.append((nr, nc))

    nr, nc = r, c + jump
    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
        visited[nr][nc] = True
        queue.append((nr, nc))
else:
    print("Hing")