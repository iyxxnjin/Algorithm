def count_repaints(board, x, y):

    repaint_w = 0
    repaint_b = 0 
    
    for i in range(8):
        for j in range(8):

            current = board[x + i][y + j]

            if (i + j) % 2 == 0:
                if current != 'W':
                    repaint_w += 1
                if current != 'B':
                    repaint_b += 1
            else:
                if current != 'B':
                    repaint_w += 1
                if current != 'W':
                    repaint_b += 1
    return min(repaint_w, repaint_b)

M, N = map(int, input().split())
board = [input().strip() for _ in range(M)]

min_paint = 64 

for i in range(M - 7):
    for j in range(N - 7):
        min_paint = min(min_paint, count_repaints(board, i, j))

print(min_paint)
