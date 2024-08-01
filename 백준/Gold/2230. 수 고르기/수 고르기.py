import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = [0]*n

for i in range(n):
    a[i] = int(input())

a.sort()

left, right = 0, 1
answer = 1e90

while left < n:
    diff = abs(a[left] - a[right])

    if diff >= m:
        answer = min(diff, answer)
        left += 1
    else:
        right += 1
        if right > n-1:
            break

print(answer)
