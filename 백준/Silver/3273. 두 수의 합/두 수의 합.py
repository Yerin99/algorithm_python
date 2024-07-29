n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

count = {}
answer = 0

for num in numbers:
    count[num] = 1

for num in numbers:
    complement = x - num
    if complement in count:
        if complement != num:
            answer += count[complement]
        else:
            answer += count[complement] - 1

print(answer // 2)