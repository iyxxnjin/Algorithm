import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력
left = deque(input().rstrip())  # 초기 문자열 입력 (줄바꿈 제거)
right = deque()

M = int(input())  # 명령어 수

for _ in range(M):
    command = input().split()

    if command[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.popleft())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])

# 최종 결과 출력
sys.stdout.write(''.join(left) + ''.join(right))
