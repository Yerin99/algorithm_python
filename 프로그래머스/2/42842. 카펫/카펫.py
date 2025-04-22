def solution(brown, yellow):
    answer = []
    
    for x in range(10000):
        for y in range(x+1):
            current_brown = 2*(x+y) - 4
            current_yellow = (x-2)*(y-2)
            
            if current_brown == brown and current_yellow == yellow:
                answer = [x, y]
                return answer
    
    return answer