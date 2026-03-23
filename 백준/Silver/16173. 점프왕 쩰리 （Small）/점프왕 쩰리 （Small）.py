# DFS 개선 ver2. w/ ChatGPT
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

def dfs(x, y):
    if visited[x][y]:
        return False

    if board[x][y] == -1:
        return True

    visited[x][y] = True
    jump = board[x][y]

    if jump == 0:
        return False

    nx = x + jump
    ny = y + jump

    if nx < N and dfs(nx, y):
        return True
    if ny < N and dfs(x, ny):
        return True

    return False

print("HaruHaru" if dfs(0, 0) else "Hing")