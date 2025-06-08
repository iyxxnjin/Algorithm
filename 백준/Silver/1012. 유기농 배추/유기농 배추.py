import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y):
    ground[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and ground[ny][nx] == 1:
            dfs(nx, ny)


for _ in range(T):
    N, M, K = map(int, input().split())
    ground = [[0] * N for i in range(M)]

    for _ in range(K):
        row, col = map(int, input().split())
        ground[col][row] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if ground[i][j] == 1:
                dfs(j, i)
                count += 1

    print(count)
