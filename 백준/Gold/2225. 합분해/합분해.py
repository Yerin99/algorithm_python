# input
n, k = map(int, input().split())
MOD = int(1e9)

# solve
dp = [[0]*(n+1) for _ in range(k)]

for i in range(1):
    for j in range(n+1):
        dp[i][j] = 1

for i in range(1, k):
    for j in range(n+1):
        for l in range(j+1):
            dp[i][j] += dp[i-1][l] % MOD


print(dp[k-1][n] % MOD)
