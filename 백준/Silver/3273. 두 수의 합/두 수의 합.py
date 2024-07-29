n = int(input())
numbers = set(map(int, input().split()))
x = int(input())

answer = sum(1 for num in numbers if x - num in numbers and x - num > num)

print(answer)