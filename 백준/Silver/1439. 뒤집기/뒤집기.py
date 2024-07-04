s = list(map(int, list(input())))

nums = [0, 0]
before = s[0]

for i in range(1, len(s)):
    now = s[i]
    if before != now:
        nums[before] += 1
    before = now

nums[before] += 1

print(min(nums))
