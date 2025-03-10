import sys


input = sys.stdin.readline
n = int(input())
graph = {node:[] for node in range(1, n+1)}

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

stack = [1]
results = [0] * (n+1)

while stack:
    node = stack.pop()

    for neighbor in graph[node]:
        if results[neighbor] == 0:
            results[neighbor] = node
            stack.append(neighbor)

for i in range(2, n+1):
    print(results[i])
