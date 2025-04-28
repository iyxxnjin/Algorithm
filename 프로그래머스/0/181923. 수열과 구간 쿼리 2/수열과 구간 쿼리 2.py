def solution(arr, queries):
    result = []
    
    for s, e, k in queries:
        newArr = []
        for i in range(s, e+1):
            if arr[i] > k:
                newArr.append(arr[i])

        if newArr:
            newArr.sort()
            result.append(newArr[0])
        else:
            result.append(-1)
                
    return result               
            