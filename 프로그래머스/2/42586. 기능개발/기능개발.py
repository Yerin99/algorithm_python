def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    
    while progresses:
        num_of_released = 0
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        while progresses and progresses[-1] >= 100:
            progresses.pop()
            speeds.pop()
            num_of_released += 1
        
        if num_of_released:
            answer.append(num_of_released)
    
    return answer