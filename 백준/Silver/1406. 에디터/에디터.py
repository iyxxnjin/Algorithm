# 에디터
# L: 커서 왼쪽 이동 / D: 커서 오른쪽 이동 / B: 왼쪽 문자 삭제 / P $: 문자 왼쪽에 추가
# 큐 생성 > B는 pop > P는 append
import sys
from collections import deque
# 자동 줄바꿈이 되어 .rstrip()로 문자 끝의 공백 문자나 \n을 잘라주는 함수 추가

read = sys.stdin.readline

# left = deque()
# for char in N:
#     left.append(char)
# left에 입력받은 문자열을 다 넣고, right에는 빈 문자열을 생성
left = deque(read().rstrip())
right = deque()

M = int(read())      # 명령어 개수

for _ in range(M):
    # 공백으로 구분된 입력값을 받음
    order = read().split()

    if order[0] == 'L':
        # 첫 문자가 아닐 시 실행
        # left에서 문자를 하나 꺼내 right의 맨 앞에 추가하여 커서를 왼쪽으로 이동시킴
        if left:
            right.appendleft(left.pop())
    elif order[0] == 'D':
        if right:
            left.append(right.popleft())
    elif order[0] == 'B':
        if left:
            left.pop()
    elif order[0] == 'P':
        # 공백으로 구분된 두 번째 인덱스
        left.append(order[1])

print(''.join(left) + ''.join(right))
# sys.stdout.write(''.join(left) + ''.join(right))
