def solution(answers):
    giveup1 = [1,2,3,4,5]
    giveup2 = [2,1,2,3,2,4,2,5]
    giveup3 = [3,3,1,1,2,2,4,4,5,5]
    
    answer = []
    count1 = count2 = count3 = 0
    
    for i in range(len(answers)):
        if answers[i] == giveup1[i % len(giveup1)]:
            count1 += 1
            
        if answers[i] == giveup2[i % len(giveup2)]:
            count2 += 1
            
        if answers[i] == giveup3[i % len(giveup3)]:
            count3 += 1
            
    max_score = (max(count1, count2, count3))
    
    if count1 == max_score:
        answer.append(1)
    if count2 == max_score:
        answer.append(2)
    if count3 == max_score:
        answer.append(3)
        
    return answer
            
            
    