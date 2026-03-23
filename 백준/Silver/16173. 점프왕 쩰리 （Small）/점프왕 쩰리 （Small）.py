N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]


def dfs(x, y):
    if x >= N or y >= N:
        return False

    if visited[x][y]:
        return False

    if board[x][y] == -1:
        return True

    visited[x][y] = True
    jump = board[x][y]

    if jump == 0:
        return False

    return dfs(x + jump, y) or dfs(x, y + jump)


print("HaruHaru" if dfs(0, 0) else "Hing")