# For문으로 n이하의 K배수를 answer에 저장
def solution(n, k):
    answer = []
    for i in range(1, n+1):
        # mul = k * i 
        # if mul <= n:
        #     answer.append(mul)
        if i % k == 0:
            answer.append(i)
    return answer