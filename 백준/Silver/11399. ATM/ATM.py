n = int(input())
p = list(map(int, input().split()))
p.sort()

answer = 0
for i in range(n):
    answer += p[i] * (n-i)

print(answer)
