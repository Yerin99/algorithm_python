import sys

n, k = map(int, sys.stdin.readline().split())
coins = [0]*n
dp = [0]*(k+1)

for i in range(n):
    coins[i] = int(sys.stdin.readline())

coins.sort()

dp[0] = 1

for coin in coins:
    for i in range(1, k+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]

print(dp[k])
