from collections import deque

def solution(numbers, target):
    answer = 0
    case = [0]
    
    for number in numbers:
        tmp_case = []
        for e in case:
            tmp_case.append(e + number)
            tmp_case.append(e - number)
            
        case = tmp_case[:]
    
    answer = case.count(target)
    
    return answer