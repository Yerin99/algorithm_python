def solution(citations):
    answer = 0
    
    citations.sort()
    n = len(citations)
    
    print(citations)
    
    for i in range(n):
        h = citations[i]
        answer = max(answer, min(n - i, h))
        print(i, answer)
    
    return answer