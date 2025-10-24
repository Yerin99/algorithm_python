def solution(n, computers):
    answer = 0

    visited = [False]*n
    
    for i in range(n):
        if not visited[i]:
            stack = [i]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    for j in range(n):
                        if node != j and computers[node][j]:
                            stack.append(j)
            answer += 1
    
    return answer