from collections import deque

num_of_v = int(input())
num_of_edge = int(input())

graph = [ [] for _ in range(num_of_v+1)]
for _ in range(num_of_edge):
    m, n = list(map(int, input().split()))
    graph[m].append(n)
    graph[n].append(m)

visited = [False] * (num_of_v+1)
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    count = -1 # except first node

    while queue:
        v = queue.popleft()
        # print(v, end=' ')
        count += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return count

print(bfs(graph, 1, visited))
