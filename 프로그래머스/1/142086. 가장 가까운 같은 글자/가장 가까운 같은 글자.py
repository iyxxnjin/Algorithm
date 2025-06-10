def solution(s):
    answer = []
    for i in range(len(s)):
        first = True
        
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:
                answer.append(i - j)
                first = False
                break
                
        if first:
            answer.append(-1)
            
    return answer
