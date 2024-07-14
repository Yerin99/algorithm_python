import sys

input = sys.stdin.readline

dp = [0] * 11
dp[0], dp[1], dp[2] = 1, 2, 4

for i in range(3, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

t = int(input())

for _ in range(t):
    print(dp[int(input())-1])
