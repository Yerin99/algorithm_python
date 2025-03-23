from collections import deque

def solution(maps):
    answer = 0
    
    queue = deque()
    n, m = len(maps), len(maps[0])
    start = (0, 0, 1)
    
    queue.append(start)
    ds = [[1, 0], [0, 1], [0, -1], [-1, 0]]
    
    while queue:
        x, y, dist = queue.popleft()
        
        if maps[y][x] == 1:
            maps[y][x] = dist
        
            for dx, dy in ds:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    queue.append((nx, ny, dist + 1))
                
    if maps[n-1][m-1] > 1:
        answer = maps[n-1][m-1]
    else:
        answer = -1
    
    
    return answer