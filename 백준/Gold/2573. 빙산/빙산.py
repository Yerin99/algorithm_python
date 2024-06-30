from collections import deque

def bfs(start_x, start_y, visited, iceberg_map):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(iceberg_map) and 0 <= ny < len(iceberg_map[0]):
                if not visited[nx][ny] and iceberg_map[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def count_iceberg_groups(iceberg_map):
    n = len(iceberg_map)
    m = len(iceberg_map[0])
    years = 0
    
    while True:
        # Step 1: Count iceberg groups
        visited = [[False] * m for _ in range(n)]
        iceberg_groups = 0
        
        for i in range(n):
            for j in range(m):
                if iceberg_map[i][j] > 0 and not visited[i][j]:
                    bfs(i, j, visited, iceberg_map)
                    iceberg_groups += 1
        
        # Step 2: Check conditions for termination
        if iceberg_groups >= 2:
            return years
        elif iceberg_groups == 0:
            return 0
        
        # Step 3: Simulate melting for the next year
        next_year_map = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if iceberg_map[i][j] > 0:
                    count = 0
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < m:
                            if iceberg_map[ni][nj] == 0:
                                count += 1
                    next_year_map[i][j] = max(0, iceberg_map[i][j] - count)
        
        # Step 4: Update iceberg_map to the next year's map
        iceberg_map = next_year_map
        years += 1

# 입력 받기
n, m = map(int, input().split())
iceberg_map = []
for _ in range(n):
    iceberg_map.append(list(map(int, input().split())))

# 결과 출력
result = count_iceberg_groups(iceberg_map)
print(result)
