import heapq

# input
N, M = map(int, input().split())
grid = []

for _ in range(N):
    grid.append(list(map(int, list(input()))))


# solve
def bfs(n, m, maze):
    bfs_heap = []
    heapq.heappush(bfs_heap, (1, 0, 0))  # 이동 거리, y좌표, x좌표

    ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while bfs_heap:
        d, y, x = heapq.heappop(bfs_heap)
        if y == n-1 and x == m-1:
            return d

        if maze[y][x]:
            maze[y][x] = False

            for dy, dx in ds:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and maze[ny][nx]:
                    heapq.heappush(bfs_heap, (d+1, ny, nx))


# print
print(bfs(N, M, grid))
