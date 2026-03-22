import sys

input = sys.stdin.readline

n, m = map(int, input().split())

edges = []

# 0번 정점에 리프 m개 연결
for i in range(1, m + 1):
    edges.append((0, i))

# 남는 정점들을 1번 정점부터 일렬로 이어붙이기
prev = 1
for i in range(m + 1, n):
    edges.append((prev, i))
    prev = i

for a, b in edges:
    print(a, b)