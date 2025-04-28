def solution(rank, attendance):
    answer = 0
    candidates = []
    
    for i in range(len(attendance)):
        if attendance[i]:
            candidates.append((rank[i], i))
                            
    candidates.sort()
    
    a = candidates[0][1]
    b = candidates[1][1]
    c = candidates[2][1]
    
    answer = 10000 * a + 100 * b + c
    return answer