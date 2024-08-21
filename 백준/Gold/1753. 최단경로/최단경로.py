import heapq


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


v, e = map(int, input().split())
s = int(input())
g = dict()

for i in range(v):
    g[i+1] = dict()

for _ in range(e):
    a, b, c = map(int, input().split())

    if b in g[a]:
        g[a][b] = min(g[a][b], c)
    else:
        g[a][b] = c

for value in dijkstra(g, s).values():
    print("INF" if value is float('inf') else value)
