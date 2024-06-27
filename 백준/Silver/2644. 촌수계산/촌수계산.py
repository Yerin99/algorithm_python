from collections import defaultdict
import heapq

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
visited = set()
answer = -1

while heap:
    distance, node = heapq.heappop(heap)
    if node not in visited:
        if node == e:
            answer = distance
            break

        for entry in graph[node]:
            heapq.heappush(heap, (distance + 1, entry))
        visited.add(node)


# print
print(answer)
