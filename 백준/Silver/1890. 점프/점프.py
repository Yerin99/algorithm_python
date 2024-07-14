import sys

# input
input = sys.stdin.readline
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# solve
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break

        distance = graph[i][j]

        if dp[i][j]:
            if j + distance < n:
                dp[i][j+distance] += dp[i][j]
            if i + distance < n:
                dp[i+distance][j] += dp[i][j]

# print
print(dp[-1][-1])
