from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(int)
    
    for name, kind in clothes:
        clothes_dict[kind] += 1
    
    for value in clothes_dict.values():
        answer *= (value + 1)
        
    answer -= 1
    
    return answer