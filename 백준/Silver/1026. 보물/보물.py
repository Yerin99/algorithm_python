n = int(input())
a, b = list(map(int, input().split())), list(map(int, input().split()))
a.sort()
b.sort()
b.reverse()

minimum_s = 0

for i in range(n):
    minimum_s += a[i]*b[i]

print(minimum_s)
