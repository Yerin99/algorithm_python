# input
n, m = map(int, input().split())
a = list(map(int, input().split()))
dp_sum = [0 for _ in range(n+1)]

# solve
answer = 0

for i in range(n):
    dp_sum[i+1] = dp_sum[i] + a[i]

for i in range(n+1):
    for j in range(i+1, n+1):
        if dp_sum[j] - dp_sum[i] == m:
            answer += 1

# print
print(answer)
