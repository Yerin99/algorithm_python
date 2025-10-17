from collections import deque

def solution(operations):
    answer = [0, 0]
    queue = []
    
    for operation in operations:
        order, num = operation.split()
        num = int(num)
        
        if order == "I":
            queue.append(num)
            queue.sort()
        elif order == "D":
            if num == 1:
                queue = queue[:-1]
            else:
                queue = queue[1:]
    
    if queue:
        answer = queue[-1], queue[0]
    
    return answer