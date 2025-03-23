def solution(arr):
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        before = answer[-1]
        current = arr[i]
        
        if before == current:
            continue
        else:
            answer.append(current)
    
    return answer