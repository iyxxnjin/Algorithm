def solution(s):
    answer = True
    valid = []
    
    for i in s:
        if i == '(':
            valid.append(i)
            
        elif i == ')':
            if not valid:
                answer = False
                break
            else:
                valid.pop()
        
    if valid:
        answer = False
        
    return answer