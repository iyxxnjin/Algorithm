def solution(ingredient):
    stack = []
    hamburger = 0
    
    for i in ingredient:
        stack.append(i)
        
        if i == 1:
            if stack[-4:] == [1,2,3,1]:
                for _ in range(4):
                    stack.pop()
                hamburger += 1
        
    return hamburger
