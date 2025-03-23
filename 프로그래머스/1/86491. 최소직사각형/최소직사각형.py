def solution(sizes):
    answer = 0
    
    for size in sizes:
        size.sort()
        
    max_a, max_b = 0, 0 
    
    for a, b in sizes:
        max_a = max(a, max_a)
        max_b = max(b, max_b)
    
    answer = max_a * max_b
    
    return answer