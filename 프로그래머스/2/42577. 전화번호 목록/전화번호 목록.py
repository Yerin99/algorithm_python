def solution(phone_book):
    answer = True
    
    phone_dict = dict()
    
    for phone_number in phone_book:
        phone_dict[phone_number] = True
    
    for phone_number in phone_book:
        for i in range(len(phone_number)-1):
            if phone_dict.get(phone_number[:i+1]):
                answer = False
                break
            
    return answer