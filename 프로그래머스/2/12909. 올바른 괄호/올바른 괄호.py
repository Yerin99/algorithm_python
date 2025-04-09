def solution(s):
    answer = True
    
    stack = []
    
    for e in s:
        if e == "(":
            stack.append(e)
        elif e == ")":
            if stack:
                stack.pop()
            else:
                answer = False
    
    if stack:
        answer = False

    return answer