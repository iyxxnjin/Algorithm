def solution(lottos, win_nums):
    count = 0
    low = 0
    result = []
    
    rank_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    for i in lottos:
        if i in win_nums:
            low += 1
            
    zero = lottos.count(0)
    high = low + zero

    result.append(rank_dict[high])
    result.append(rank_dict[low])
    
    return result