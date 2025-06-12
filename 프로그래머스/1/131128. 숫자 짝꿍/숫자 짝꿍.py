def solution(X, Y):
    answer = ''
    X_counter = [0] * 10
    Y_counter = [0] * 10
    
    for digit in X:
        X_counter[int(digit)] += 1
    for digit in Y:
        Y_counter[int(digit)] += 1
        
    result = []
    for i in range(9, -1, -1):
        common = min(X_counter[i], Y_counter[i])
        result.append(str(i) * common)
        
    answer = ''.join(result)
        
    if not answer:
        return '-1'
    elif answer[0] == '0':
        return '0'
    else:
        return answer
        