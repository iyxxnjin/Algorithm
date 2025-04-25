# if문  > 최빈값이 여러개면 -1, 한 개면 해당 값 return
# for문 > 현재 Idx, 다음 inx 같으면 cnt++
# cnt 비교문으로 
def solution(array):
    count_dict = {}
    
    for num in array:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    max_count = 0
    for count in count_dict.values():
        if count > max_count:
            max_count = count
            
    max = []
    for num in count_dict:
        if count_dict[num] == max_count:
            max.append(num)
    
    if len(max) >= 2:
        return -1
    else:
        return max[0]