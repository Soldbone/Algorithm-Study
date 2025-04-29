# DFS와 BFS
from collections import deque

num_of_v, num_of_line, v = list(map(int, input().split()))

graph = [ [] for _ in range(num_of_v+1)]
for _ in range(num_of_line):
    m, n = list(map(int, input().split()))
    graph[m].append(n)
    graph[n].append(m)

for i in graph:
    i.sort()


visited = [False] * (num_of_v+1)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, visited)
visited = [False] * (num_of_v+1)
print()
bfs(graph, v, visited)