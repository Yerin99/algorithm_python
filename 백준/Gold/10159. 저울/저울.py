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
n, m = int(input()), int(input())
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

for i in range(n):
    answer = 0

    for j in range(n):
        if graph_result1[i][j] == graph_result2[i][j] == inf:
            answer += 1

    print(answer)
