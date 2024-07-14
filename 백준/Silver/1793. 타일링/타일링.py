import sys

dp = [0] * 251
dp[0], dp[1], dp[2] = 1, 1, 3

for i in range(3, 251):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

while True:
    try:
        n = int(sys.stdin.readline())
        print(dp[n])
    except:
        break
