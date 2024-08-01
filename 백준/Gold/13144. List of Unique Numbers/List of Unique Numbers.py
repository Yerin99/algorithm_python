n = int(input())
numbers = list(map(int, input().split()))

left = 0
seen = set()
result = 0

for right in range(n):
    while numbers[right] in seen:
        seen.remove(numbers[left])
        left += 1
    
    seen.add(numbers[right])
    result += right - left + 1

print(result)