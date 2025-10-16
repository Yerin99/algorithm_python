def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    stack = [0]
    
    for i in range(n):
        temp_stack = []
        for node in stack:
            temp_stack.append(node+numbers[i])
            temp_stack.append(node-numbers[i])
        stack = temp_stack[:]
    
    answer = stack.count(target)
    
    return answer