from collections import deque
import heapq

def solution(priorities, location):
    answer = 0
    max_heap = []
    processes = deque([])
    
    for i, priority in enumerate(priorities):
        max_heap.append(-priority)
        processes.append([i, priority])
    
    heapq.heapify(max_heap)
    is_running = True
    
    
    while is_running:
        highest_priority = -heapq.heappop(max_heap)
        n = len(processes)
        
        for _ in range(n):
            i, priority = processes.popleft()
            
            if priority == highest_priority:
                answer += 1
                if i == location:
                    is_running = False
                break    
            else:
                processes.append([i, priority])
            
        
    return answer