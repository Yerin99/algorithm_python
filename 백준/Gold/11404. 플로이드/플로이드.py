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
graph = [[inf]*n for _ in range(n)]

for index in range(n):
    graph[index][index] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(c, graph[a-1][b-1])

answer = floyd_warshall(graph)

for entry in answer:
    for number in entry:
        print(0 if number == inf else number, end=" ")
    print()
