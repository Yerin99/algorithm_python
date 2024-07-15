n = int(input())
dp = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i-1):
        dp[i] += dp[j]
    dp[i] += 1

print(dp[n])
