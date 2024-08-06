import heapq
from collections import defaultdict


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


n, m = map(int, input().split())
g = defaultdict(dict)

for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1


my_dict = dijkstra(g, 1)
longest_distance = max(my_dict.values())
candidates = []

for key, value in my_dict.items():
    if value == longest_distance:
        heapq.heappush(candidates, key)

print(candidates[0], longest_distance, len(candidates))
