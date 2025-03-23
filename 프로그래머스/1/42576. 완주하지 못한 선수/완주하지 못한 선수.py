def solution(participant, completion):
    answer = ''
    
    people_dict = dict()
    
    for p in participant:
        people_dict[p] = people_dict.get(p, 0) + 1
    
    for c in completion:
        people_dict[c] = people_dict[c] - 1
        
    for k in people_dict.keys():
        if people_dict[k] == 1:
            answer = k
            break
    
    return answer