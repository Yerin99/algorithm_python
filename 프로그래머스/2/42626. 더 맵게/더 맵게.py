import heapq 

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    
    while scoville:
        first = heapq.heappop(scoville)
        
        if first >= K:
            break
        else:
            if not scoville:
                answer = -1
                break
        
        second = heapq.heappop(scoville)
        
        new = first + second * 2
        heapq.heappush(scoville, new)
        answer += 1
    
    return answer