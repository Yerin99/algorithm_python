import sys


def floyd_warshall():
    v = len(graph)

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    visited[i][j] = visited[i][k]


input = sys.stdin.readline
n, m = map(int, input().split())
inf = float('inf')
graph = [[inf]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
    visited[a-1][b-1] = b
    visited[b-1][a-1] = a

floyd_warshall()

for entry in visited:
    for number in entry:
        print('-' if number == 0 else number, end=" ")
    print()
