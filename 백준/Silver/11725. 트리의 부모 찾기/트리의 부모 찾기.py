n = int(input())

graph = [ [] for _ in range(n+1)]
for _ in range(n-1):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
result = {}
def dfs(graph, v, visited):
    stack = [v]
    visited[v] = True
    while stack:
        value = stack.pop()
        if not visited[value]:
            visited[value] = True
        for j in graph[value]:
            if not visited[j]:
                result[j] = value
                stack.append(j)

dfs(graph, 1, visited)
for i in range(2, n+1):
    print(result[i])
