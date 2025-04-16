def solution(answers):
    answer = []
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        for student in range(3):
            if patterns[student][i % len(patterns[student])] == answers[i]:
                scores[student] += 1
    
    for student in range(3):
        if scores[student] == max(scores):
            answer.append(student + 1)
    
    return answer