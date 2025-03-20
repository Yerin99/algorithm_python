def solution(phone_book):
    answer = True
    
    phone_prefix = dict()
    
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            phone_prefix[phone_number[:i]] = True
    
    for phone_number in phone_book:
        if phone_prefix.get(phone_number):
            answer = False
            break
            
    return answer