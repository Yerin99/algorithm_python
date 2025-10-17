from collections import defaultdict

def solution(participant, completion):
    people = defaultdict(int)
    
    for p in participant:
        people[p] += 1
    
    for c in completion:
        people[c] -= 1
    
    for key, value in people.items():
        if value == 1:
            answer = key
    
    return answer