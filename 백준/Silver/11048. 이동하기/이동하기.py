import sys

# input
input = sys.stdin.readline
n, m = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(n)]

# solve
d = [[-1, 0], [0, -1], [-1, -1]]

for y in range(n):
    for x in range(m):
        candidates = []
        max_candy = candies[y][x]

        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                candidates.append(candies[ny][nx])

        if candidates:
            max_candy += max(candidates)

        candies[y][x] = max_candy

# print
print(candies[n-1][m-1])
