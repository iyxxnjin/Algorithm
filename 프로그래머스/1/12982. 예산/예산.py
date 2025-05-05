def solution(d, budget):
    d.sort()
    sum = 0
    count = 0
    
    for amount in d:
        sum += amount
        if sum <= budget:
            count += 1

    return count
