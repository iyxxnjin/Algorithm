def solution(array, commands):
    result = []
    
    for command in range(len(commands)):
        i, j, k = commands[command]
        tmp = array[i-1:j]
        tmp.sort()
        result.append(tmp[k-1])
        
    return result