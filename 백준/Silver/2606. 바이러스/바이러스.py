from collections import defaultdict

computers = int(input())
n = int(input())
graph = defaultdict(list)

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 선택해서 풀이
visited = []
stack = [1]

while stack:
    node = stack.pop()
    if node not in visited:
        visited.append(node)
        stack.extend(graph[node])

print(len(visited)-1)
