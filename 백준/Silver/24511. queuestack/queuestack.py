n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

results = []

for i in range(n):
    if a[i] == 0:
        results.append(b[i])

results = results[::-1]

if len(results) < m:
    results += c

print(*results[:m])
