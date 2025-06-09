import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(x, y, symbol):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        if symbol == '-':
            ny = y + 1
            if ny < m and not visited[x][ny] and board[x][ny] == '-':
                visited[x][ny] = True
                queue.append((x, ny))

        elif symbol == '|':
            nx = x + 1
            if nx < n and not visited[nx][y] and board[nx][y] == '|':
                visited[nx][y] = True
                queue.append((nx, y))

count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j, board[i][j])
            count += 1

print(count)
