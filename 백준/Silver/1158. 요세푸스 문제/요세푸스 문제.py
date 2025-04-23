# 요세푸스 순열
# N = 사람 수, K = 제거할 이동 수
# 큐 -> K-1번 deque와 enque 반복 후, pop을 반복

from collections import deque

N, K = map(int, input().split())
# deque 초기화하여 queue라는 변수에 저장
queue = deque()
# range()는 끝 숫자를 포함 안 하기에 1부터 N까지 queue에 저장
for i in range(1, N + 1):
    queue.append(i)

result = []
# K-1까지 deque, K번째 enque
while queue:
    for j in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

# result에 str(문자열)로 변환한 값이 저장
print('<' + ', '.join(map(str, result)) + '>')



