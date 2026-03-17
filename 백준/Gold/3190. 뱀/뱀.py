# ChatGPT 코드 과연 돌아가는지 테스트

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]

# 사과 위치 저장
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

L = int(input())

turns = {}
for _ in range(L):
    x, c = input().split()
    turns[int(x)] = c

# 오른쪽, 아래, 왼쪽, 위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

direction = 0
time = 0

# 뱀의 몸: (행, 열)
snake = deque()
snake.append((0, 0))
board[0][0] = 2

while True:
    time += 1

    head_r, head_c = snake[-1]
    nr = head_r + dr[direction]
    nc = head_c + dc[direction]

    # 벽 충돌
    if not (0 <= nr < N and 0 <= nc < N):
        break

    # 자기 몸 충돌
    if board[nr][nc] == 2:
        break

    # 머리 이동
    if board[nr][nc] == 1:
        # 사과가 있으면 꼬리 유지
        board[nr][nc] = 2
        snake.append((nr, nc))
    else:
        # 사과가 없으면 꼬리 제거
        tail_r, tail_c = snake.popleft()
        board[tail_r][tail_c] = 0

        board[nr][nc] = 2
        snake.append((nr, nc))

    # 방향 전환
    if time in turns:
        if turns[time] == 'D':
            direction = (direction + 1) % 4
        else:  # 'L'
            direction = (direction - 1) % 4

print(time)