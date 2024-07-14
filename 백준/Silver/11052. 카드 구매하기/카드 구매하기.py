n = int(input())
p = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        p[i] = max(p[i], p[j] + p[i-j-1])

print(p[-1])
