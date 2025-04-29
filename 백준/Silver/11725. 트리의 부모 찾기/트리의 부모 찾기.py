from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

graph = [ [] for _ in range(n+1)]
for _ in range(n-1):
    x, y = list(map(int, sys.stdin.readline().split()))
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
result = {}
# def dfs(graph, v, visited):
#     stack = [v]
#     visited[v] = True
#     while stack:
#         value = stack.pop()
#         if not visited[value]:
#             visited[value] = True
#         for j in graph[value]:
#             if not visited[j]:
#                 result[j] = value
#                 stack.append(j)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        # print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                result[i] = v
                queue.append(i)
                visited[i] = True


# dfs(graph, 1, visited)
bfs(graph, 1, visited)
for i in range(2, n+1):
    print(result[i])
