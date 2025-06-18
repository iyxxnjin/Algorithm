def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        low_value = min(arr)
        arr.remove(low_value)
        return arr
    