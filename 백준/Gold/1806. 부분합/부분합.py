n, s = map(int, input().split())
a = list(map(int, input().split()))

f, b = 0, 0
total = a[0]
answer = 1e90

while f < n:
    if total >= s:
        answer = min(answer, b-f+1)
        total -= a[f]
        f += 1
    else:
        if b < n-1:
            b += 1
            total += a[b]
        else:
            total -= a[f]
            f += 1

print(0 if answer == 1e90 else answer)
