def solution(number, k):
    answer = ''
    
    n = len(number)
    stack = []
    
    # 앞에서부터 숫자 하나씩 순회
    for i in range(n):
        current = number[i]
        
        '''
        push 하기 전에:
        스택 마지막 숫자가 지금 숫자보다 작고,
        k > 0이면 pop (숫자 제거), k -= 1
        '''
        
        while stack and stack[-1] < current and k > 0:
            stack.pop()
            k -= 1

        stack.append(current)
           
    '''
    다 돌고 나서 k가 남아 있으면?
    → 그만큼 뒤에서 제거
    '''
    
    answer = ''.join(stack[:n-k])

    
    return answer