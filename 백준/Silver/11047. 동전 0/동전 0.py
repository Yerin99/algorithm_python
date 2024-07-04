n, k = map(int, input().split())
answer = 0
a = []

for _ in range(n):
    a.append(int(input()))

while a:
    coin = a.pop()

    while k >= coin:
        answer += k // coin
        k = k % coin

    if k == 0:
        break

print(answer)
