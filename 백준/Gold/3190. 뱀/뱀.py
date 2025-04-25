import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
K = int(read())
board = [[0] * N for _ in range(N)]

for _ in range(K):
    row, col = map(int, read().split())
    board[row - 1][col - 1] = 1

L = int(read())
turn = {}

for _ in range(L):
    X, C = read().split()
    turn[int(X)] = C

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0

snake = deque()
snake.append((0, 0))
x, y = 0, 0
time = 0

while True:
    time += 1
    
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= N or y < 0 or y >= N or (x, y) in snake:
        break

    snake.append((x, y))
    
    if board[x][y] == 1:
        board[x][y] = 0
    else:
        snake.popleft()

    if time in turn:
        if turn[time] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

print(time)
