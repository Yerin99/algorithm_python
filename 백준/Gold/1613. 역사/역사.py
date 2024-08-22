import sys


def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


input = sys.stdin.readline
n, m = map(int, input().split())
inf = float('inf')
graph1 = [[inf]*n for _ in range(n)]
graph2 = [[inf]*n for _ in range(n)]

for index in range(n):
    graph1[index][index] = 0
    graph2[index][index] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph1[a-1][b-1] = 1
    graph2[b-1][a-1] = 1


graph_result1 = floyd_warshall(graph1)
graph_result2 = floyd_warshall(graph2)

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())

    if graph_result1[a-1][b-1] != inf:
        print(-1)
    elif graph_result2[a-1][b-1] != inf:
        print(1)
    else:
        print(0)
