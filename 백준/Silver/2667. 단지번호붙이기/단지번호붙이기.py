n = int(input())

grid = []
visited_grid = [[False] * n for _ in range(n)]

town_number = 0
houses = []

for _ in range(n):
    grid.append(list(map(int, list(input()))))

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited_grid[i][j]:
            stack = [(i, j)]
            house_number = 0

            while stack:
                y, x = stack.pop()

                if grid[y][x] == 1 and not visited_grid[y][x]:
                    for dx, dy in d:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            stack.append([ny, nx])
                    visited_grid[y][x] = True
                    house_number += 1

            town_number += 1
            houses.append(house_number)


print(town_number)

for entry in sorted(houses):
    print(entry)
