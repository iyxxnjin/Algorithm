from collections import Counter
def solution(nums):
    select = len(nums) / 2
    
    count = Counter(nums)
    if len(count) < select:
        return len(count)
    else:
        return select