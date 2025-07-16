# 적록색약
# [REF] good1588님 제출
import sys
input = sys.stdin.readline

def dfs(color, x, y):
    stk = [(x, y)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while stk:
        x, y = stk.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if ( 0 <= nx < N and 0 <= ny < N ) and (graph[nx][ny] == color):
                graph[nx][ny] = 'O' if graph[nx][ny] in "RG" else 'X'
                stk.append((nx, ny))

# Input
N = int(input().rstrip())
graph = [ list(input()) for _ in range(N) ]

non_blind_count_rg = 0
count_b = 0
blind_count_rg = 0

for i in range(N):
    for j in range(N):
        curr = graph[i][j]
        if curr not in "OX":
            if curr in "RG":
                graph[i][j] = 'O'
                non_blind_count_rg += 1
            else:
                graph[i][j] = 'X'
                count_b += 1
            dfs(curr, i, j)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'O':
            blind_count_rg += 1
            dfs('O', i, j)


print(non_blind_count_rg + count_b, blind_count_rg + count_b)
