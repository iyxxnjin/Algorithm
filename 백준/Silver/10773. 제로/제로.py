from collections import deque
import sys

input = sys.stdin.readline
queue = deque()

K = int(input())

for _ in range(K):
    num = int(input())
    if num == 0:
        if queue:
            queue.pop()
    else:
        queue.append(num)
        
print(sum(queue))


