def solution(n):
    l = list(str(n))
    l.sort(reverse = True)
    sorted_n = "".join(l)
    
    return int(sorted_n)