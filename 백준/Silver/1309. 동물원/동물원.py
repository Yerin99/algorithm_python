import sys

n = int(sys.stdin.readline())
dp = [0]*(n+1)
dp[0], dp[1] = 1, 1+2

for i in range(2, n+1):
    dp[i] = (dp[i-1]*2 % 9901 + dp[i-2]) % 9901

print(dp[n])
