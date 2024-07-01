# input
n = int(input())
grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))


# solve
flooded = [[False] * n for _ in range(n)]
maximum = min(100, max(map(max, grid)))
safe_zones = [0]

for h in range(maximum + 1):
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] <= h:
                flooded[i][j] = True

    safe_zone = 0
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for i in range(n):
        for j in range(n):
            stack = []

            if not visited[i][j] and not flooded[i][j]:
                stack.append((i, j))

                while stack:
                    y, x = stack.pop()
                    visited[y][x] = True

                    for dy, dx in d:
                        ny, nx = y + dy, x + dx

                        if 0 <= ny < n and 0 <= nx < n:
                            if not visited[ny][nx] and not flooded[ny][nx]:
                                stack.append((ny, nx))

                safe_zone += 1

    safe_zones.append(safe_zone)


# print
print(max(safe_zones))
