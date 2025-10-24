def solution(n, computers):
    def dfs(node):
        visited[node] = True
        for i in range(n):
            if not visited[i] and computers[node][i]:
                dfs(i)
    
    answer = 0

    visited = [False]*n
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer