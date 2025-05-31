def solution(lottos, win_nums):
    count = 0
    zero = 0
    result = []
    
    for i in lottos:
        if i == 0:
            zero += 1
        for j in win_nums:
            if i == j:
                count += 1
                break

    low = count
    high = count + zero
    
    def get_rank(n):
        if n == 6:
            return 1
        elif n == 5:
            return 2
        elif n == 4:
            return 3
        elif n == 3:
            return 4
        elif n == 2:
            return 5
        else:
            return 6

    result.append(get_rank(high))
    result.append(get_rank(low))
    
    return result