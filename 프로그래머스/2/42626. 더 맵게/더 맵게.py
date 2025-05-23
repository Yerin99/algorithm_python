import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            answer = -1
            break
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new = first + second * 2
        answer += 1
        heapq.heappush(scoville, new)
        
    return answer