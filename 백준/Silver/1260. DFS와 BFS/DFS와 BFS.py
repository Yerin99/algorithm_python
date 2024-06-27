from collections import defaultdict
from collections import deque

n, m, root = map(int, input().split())
graph = defaultdict(set)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

bfs_visited = set()
dfs_visited = set()
queue = deque([root])
stack = [root]

while stack:
    node = stack.pop()

    if node not in dfs_visited:
        stack += sorted(list(graph[node]))[::-1]
        dfs_visited.add(node)
        print(node, end=" ")

print()

while queue:
    node = queue.popleft()

    if node not in bfs_visited:
        queue += sorted(deque(graph[node]))
        bfs_visited.add(node)
        print(node, end=" ")