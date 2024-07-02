def solution(name):
    n = len(name)
    
    # 각 문자를 'A'로부터 변경하는 횟수를 저장
    change = [min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name]
    
    answer = sum(change)
    
    min_move = n - 1  # 최소 좌우 이동 횟수는 기본적으로 n-1 (맨 끝에서 시작)
    
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        # 앞쪽으로 이동 후 뒤쪽으로 이동
        min_move = min(min_move, i + n - next_i + min(i, n - next_i))
    
    answer += min_move
    
    return answer
