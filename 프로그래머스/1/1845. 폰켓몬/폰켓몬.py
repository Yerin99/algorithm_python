def solution(nums):
    nums_set = set(nums)
    answer = min(len(nums_set), len(nums)//2)
        
    return answer