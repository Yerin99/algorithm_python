from collections import deque

# input
n, k = map(int, input().split())
visited = [-1] * (100000 + 1)

# solve (bfs)
queue = deque([n])
visited[n] = 0

while queue:
    x = queue.popleft()

    if x == k:
        break

    if 0 <= x-1 <= 100000 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        queue.append(x-1)

    if 0 <= x+1 <= 100000 and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        queue.append(x+1)

    if 0 <= 2*x <= 100000 and visited[2*x] == -1:
        visited[2*x] = visited[x] + 1
        queue.append(2*x)


# print
print(visited[k])
