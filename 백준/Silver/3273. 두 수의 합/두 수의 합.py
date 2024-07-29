n = int(input())
a = sorted(map(int, input().split()))
target = int(input())

front, back = 0, n-1
answer = 0

while front < back:
    total = a[front] + a[back]

    if total < target:
        front += 1
    elif total == target:
        front += 1
        back -= 1
        answer += 1
    else:
        back -= 1

print(answer)
