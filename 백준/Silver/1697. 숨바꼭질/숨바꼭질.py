from collections import deque

# input
n, k = map(int, input().split())
visited = [-1] * 100001

# solve (bfs) - 큐에 넣을 때 방문 처리 (중복 방지)
# bfs 초기화
queue = deque([n])
visited[n] = 0

# bfs 탐색
while queue:
    x = queue.popleft()

    if x == k:
        break

    for next_x in [x-1, x+1, 2*x]:
        if 0 <= next_x <= 100000 and visited[next_x] == -1:
            visited[next_x] = visited[x] + 1
            queue.append(next_x)

# print
print(visited[k])
