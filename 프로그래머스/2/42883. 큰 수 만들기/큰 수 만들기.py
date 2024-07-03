def solution(number, k):
    answer = ''
    stack = []
    number = list(number)[::-1]
    org_length = len(number)
    
    while number:
        num = number.pop()
        while stack and stack[-1] < num:
            stack.pop()
            k -= 1
                
            if k == 0:
                stack.append(num)    
                stack += number[::-1]
                break
        
        if k == 0:
            break
            
        if len(stack) < org_length - k:
            stack.append(num)    
    
    answer = ''.join(stack)
    
    return answer