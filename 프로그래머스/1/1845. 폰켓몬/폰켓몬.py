def solution(nums):
    answer = 0
    
    n = len(nums)
    ponketmons = [0]*200001
    
    for num in nums:
        if ponketmons[num] == 0:
            answer += 1
        ponketmons[num] += 1
    
    answer = min(n//2, answer)
    
    return answer