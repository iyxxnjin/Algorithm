def solution(arr):
    if not 2 in arr:
        return [-1]
    else:
        return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]

    