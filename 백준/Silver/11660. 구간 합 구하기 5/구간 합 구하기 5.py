import sys

# input
n, m = map(int, sys.stdin.readline().split())
table, targets = [], []

for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

for _ in range(m):
    targets.append(list(map(int, sys.stdin.readline().split())))

# solve
dp_sum = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dp_sum[i][j] += table[i][j]

        if i-1 >= 0:
            dp_sum[i][j] += dp_sum[i-1][j]
        if j-1 >= 0:
            dp_sum[i][j] += dp_sum[i][j-1]
        if i-1 >= 0 and j-1 >= 0:
            dp_sum[i][j] -= dp_sum[i - 1][j - 1]

for x1, y1, x2, y2 in targets:
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    answer = dp_sum[x2][y2]

    if x1-1 >= 0:
        answer -= dp_sum[x1-1][y2]
    if y1-1 >= 0:
        answer -= dp_sum[x2][y1-1]
    if x1-1 >= 0 and y1-1 >= 0:
        answer += dp_sum[x1-1][y1-1]

    print(answer)
