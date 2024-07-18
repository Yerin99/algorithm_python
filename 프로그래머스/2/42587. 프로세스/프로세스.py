from collections import deque
import heapq

def solution(priorities, location):
    answer = 0
    
    priority_queue = deque()
    priority_heap = []
    
    for i in range(len(priorities)):
        priority = priorities[i]
        heapq.heappush(priority_heap, -priority)
        priority_queue.append([i, priority])
    
    order = 1
    
    while priority_queue:
        process, priority = priority_queue.popleft()
        highest_priority = -priority_heap[0]
        
        if priority < highest_priority:
            priority_queue.append([process, priority])
        elif priority == highest_priority:
            if process == location:
                break
            else:
                heapq.heappop(priority_heap)
                order += 1
    
    return order