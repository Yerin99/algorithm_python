from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))
nums = [0]*100000
indexes = [deque([]) for _ in range(100000)]

start, end = 0, 0
nums[a[start]-1] = 1
indexes[a[start]-1].append(start)
candidates = []
length = 1

while end < n-1:
    end += 1
    target = a[end]

    if nums[target-1] + 1 <= k:
        length += 1
    else:  # if the num is bigger than k
        candidates.append(length)
        new_start = indexes[target-1][0] + 1

        for i in range(start, new_start):
            if start <= indexes[a[i]-1][0] < new_start:
                indexes[a[i]-1].popleft()
                nums[a[i]-1] -= 1

        start = new_start
        length = end - start + 1

    nums[target - 1] += 1
    indexes[target-1].append(end)

candidates.append(length)

print(max(candidates))
