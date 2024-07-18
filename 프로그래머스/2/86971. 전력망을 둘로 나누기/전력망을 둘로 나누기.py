from collections import defaultdict

def solution(n, wires):
    candidates = []
    
    for c1, c2 in wires:    
        visited = [False]*(n+1)
        graph = defaultdict(list)
        
        for v1, v2 in wires:
            if c1 == v1 and c2 == v2:
                continue
                
            graph[v1] += [v2]
            graph[v2] += [v1]
    
        nums = []
        
        for vertex in range(1, n+1):               
            num = 0
            stack = [vertex]
            
            while stack:
                node = stack.pop()
                
                if not visited[node]:
                    num += 1
                    for next_node in graph[node]:
                        stack += graph[node]
                        visited[node] = True
            
            if num:
                nums.append(num)
        
        candidates.append(abs(nums[0] - nums[-1]))
    
    return min(candidates)