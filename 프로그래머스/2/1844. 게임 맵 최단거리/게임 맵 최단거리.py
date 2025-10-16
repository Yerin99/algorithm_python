from collections import deque

def solution(maps):
    answer = -1
    
    n, m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]
    
    start = (0, 0, 1)
    visited[0][0] = 1
    queue = deque([start])
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    while queue:
        y, x, nums = queue.popleft()
        
        if x == m-1 and y == n-1:
            answer = nums
            break
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and maps[ny][nx]:
                    queue.append((ny, nx, nums+1))
                    visited[ny][nx] = 1
    
    return answer