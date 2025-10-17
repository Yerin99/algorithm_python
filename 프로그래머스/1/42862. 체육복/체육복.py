def solution(n, lost, reserve):
    answer = 0
    students = [0]*n
    
    for l in lost:
        students[l-1] -= 1
    
    for r in reserve:
        students[r-1] += 1
    
    for i in range(n):
        if students[i] == -1:
            if i-1 >= 0 and students[i-1] == 1:
                students[i] += 1
                students[i-1] -= 1
            elif i+1 < n and students[i+1] == 1:
                students[i] += 1
                students[i+1] -= 1
                
    for student in students:
        if student != -1:
            answer += 1
    
    return answer