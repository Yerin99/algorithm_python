s = list(map(int, list(input())))
answer = 0

nums = [[], []]

before = s[0]
count = 1

for i in range(1, len(s)):
    now = s[i]
    if before != now:
        nums[before].append(count)
        count = 1
    else:
        count += 1
    before = now

nums[before].append(count)

print(min(map(len, nums)))
