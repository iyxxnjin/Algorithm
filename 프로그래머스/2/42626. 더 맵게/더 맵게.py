import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while len(scoville) >= 2 and scoville[0] < K:
        s1 = heapq.heappop(scoville)      
        s2 = heapq.heappop(scoville)     
        
        mixed = s1 + (s2 * 2)
        
        heapq.heappush(scoville, mixed)   
        count += 1

    if scoville[0] >= K:
        return count
    else:
        return -1
    
