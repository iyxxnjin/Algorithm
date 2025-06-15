def solution(s):
    answer = ''
    
    for i in s.split(' '):
        strange_word = ''
        
        for j in range(len(i)):
            if j % 2 == 0:
                strange_word += i[j].upper()
            else:
                strange_word += i[j].lower()
        
        answer += strange_word + ' '
    
    return answer[:-1]
        