import sys

n = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(n)]
ropes.sort()
maximum_weight = 0

for i in range(n):
    minimum_weight = ropes[i]
    maximum_weight = max(maximum_weight, minimum_weight * (n - i))

print(maximum_weight)