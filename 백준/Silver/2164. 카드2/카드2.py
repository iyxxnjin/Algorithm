# deque 사용
# 입력: 정수 N장의 카드
# 1부터 N까지 queue에 삽입
# 카드 한 장 남을때까지 반복하므로 while문 사용
# pop -> pop + append -> (반복)
# 출력: deque는 인덱싱이 가능하므로 deque[0]값 출력

import sys
from collections import deque

read = sys.stdin.readline
N = int(read())
# 초기화
queue = deque()

for i in range(1, N+1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])