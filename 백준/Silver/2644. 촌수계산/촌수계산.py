from collections import defaultdict
from collections import deque

# input
n = int(input())
s, e = map(int, input().split())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

# solve
heap = [(0, s)]  # 거리, 좌표
visited = defaultdict(int)
queue = deque([s])
answer = -1

while queue:
    node = queue.popleft()
    if node == e:
        answer = visited[node]
        break

    for entry in graph[node]:
        if visited[entry] == 0:
            queue.append(entry)
            visited[entry] = visited[node] + 1

# print
print(answer)
