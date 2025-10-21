from collections import defaultdict


def solution(phone_book):
    answer = True
    is_prefix = defaultdict(bool)
    
    
    for phone_number in phone_book:
        n = len(phone_number)
        for i in range(n):
            prefix = phone_number[:i]
            is_prefix[prefix] = True
    
    for phone_number in phone_book:
        if is_prefix[phone_number]:
            answer = False
            break
    
    return answer