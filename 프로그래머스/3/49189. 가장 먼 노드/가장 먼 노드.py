from collections import deque
from collections import defaultdict


def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [-1]*(n+1)
    queue = deque([[1, 0]])
    
    while queue:
        node, distance = queue.popleft()
        if visited[node] == -1:
            visited[node] = distance
            for next_node in graph[node]:       
                queue.append([next_node, distance+1])
    
    answer = visited.count(max(visited))
    
    return answer