from collections import deque

N, M, start = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)

def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, len(graph)):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in range(1, len(graph)):
            if graph[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = 1

dfs(graph, start, visited_dfs)
print()
bfs(graph, start, visited_bfs)
