def solution(progresses, speeds):
    release = []
    i = 0
    
    while i < len(progresses):
        day = 0
        count = 0
        while progresses[i] + speeds[i] * day < 100 :
            day += 1 
            
        while i < len(progresses) and progresses[i] + speeds[i] * day >= 100:
            count += 1
            i += 1
            
        release.append(count)
            
    return release