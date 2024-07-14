import math

n = int(input())

dp = [1e90]*(n+1)
dp[0] = 0

for i in range(1, n+1):
    if math.sqrt(i).is_integer():
        dp[i] = 1
    else:
        maximum = int(math.sqrt(i))
        for num in range(maximum):
            square = num ** 2
            dp[i] = min(dp[i], 1 + dp[i - square])

print(dp[n])
